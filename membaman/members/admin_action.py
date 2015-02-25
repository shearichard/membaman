import logging
import os
import pytz
import tempfile
import time
import datetime
import zipfile
import csv
try:
    import zlib
    COMPRESSION = zipfile.ZIP_DEFLATED
except:
    COMPRESSION = zipfile.ZIP_STORED

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.conf import settings
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Sample platypus document
# From the FAQ at reportlab.org/oss/rl-toolkit/faq/#1.1

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "Hello world"
pageinfo = "platypus example"

def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.restoreState()
    
def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.drawString(inch, 0.75 * inch,"Page %d %s" % (doc.page, pageinfo))
    canvas.restoreState()
    
def make_start_year_invoice_pdf_platypus(buffer):

    doc = SimpleDocTemplate(buffer)
    Story = [Spacer(1,2*inch)]
    style = styles["Normal"]
    for i in range(100):
        bogustext = ("Paragraph number %s. " % i) *20
        p = Paragraph(bogustext, style)
        Story.append(p)
        Story.append(Spacer(1,0.2*inch))
    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

    pdfbytes = buffer.getvalue()
    buffer.close()
    return pdfbytes
    
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def get_local_iso():
    tz_in_use = pytz.timezone(settings.TIME_ZONE)
    dtnow = datetime.datetime.now(tz_in_use)
    return dtnow.strftime('%Y%m%dT%H%M%S')

def make_start_year_invoice_pdf(mem):
    '''
    Creates a start year invoice for the member in question
    '''
    buffer = BytesIO()
    use_platypus = True

    if use_platypus:
        pdfbytes = make_start_year_invoice_pdf_platypus(buffer)
    else:
        # Create the PDF object, using the BytesIO object as its "file."
        p = canvas.Canvas(buffer)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        p.drawString(100, 100, "Hello %s" % mem.last_first_name())
        p.drawString(100, 200, "Hello %s" % mem.primary_caregiver_email())
        # Close the PDF object cleanly.
        p.showPage()
        p.save()
        # Get the value of the BytesIO buffer and write it to the response.
        pdfbytes = buffer.getvalue()

    buffer.close()

    return pdfbytes

def print_start_year_invoices(modeladmin, request, queryset):
    '''
    An Admin action to Download a zip file of invoices for
    all selected Members suitable for start of year use
    '''

    print "print_start_year_invoices starts"
    
    run_date_time = get_local_iso()
    temp = tempfile.NamedTemporaryFile(prefix="membaman-startyear-invoices-", suffix="-%s.zip" % run_date_time, delete=False)
    pdf_paths = []
    with zipfile.ZipFile(temp, mode='w', compression=COMPRESSION) as zf:
        with BytesIO() as csvfile:
            csv_invoice_manifest = csv.writer(csvfile)
            csv_invoice_manifest.writerow(['''Family Name''',
                                           '''Given Name''',
                                           '''Member ID''',
                                           '''PDF invoice file name''',
                                           '''Email to send invoice to''' ])
            for memb in queryset:
                pdfbytes = make_start_year_invoice_pdf(memb)
                zip_component_name = '%s-%s-%s.pdf' % (memb.name_given.replace(' ', '_').lower(), 
                                                       memb.name_family.replace(' ', '_').lower(), 
                                                       str(memb.id))
                zf.writestr(zip_component_name, pdfbytes)
                csv_invoice_manifest.writerow([memb.name_family, 
                                               memb.name_given,
                                               memb.id,
                                               zip_component_name,
                                               memb.primary_caregiver_email() ])

            zf.writestr("Invoice-manifest-%s.csv" % run_date_time, csvfile.getvalue())


    temp.seek(0)
    response = HttpResponse(temp.read(), 'application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(temp.name)
    response['Content-Length'] = os.path.getsize(temp.name)
    print "print_start_year_invoices ends"
    return response        
        

print_start_year_invoices.short_description = "Download Start Year invoices in a single zip file"
