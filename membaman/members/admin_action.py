import logging
import os
import pytz
import tempfile
import time
import datetime
import zipfile
try:
    import zlib
    COMPRESSION = zipfile.ZIP_DEFLATED
except:
    COMPRESSION = zipfile.ZIP_STORED

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.conf import settings


def get_local_iso():
    tz_in_use = pytz.timezone(settings.TIME_ZONE)
    dtnow = datetime.datetime.now(tz_in_use)
    return dtnow.strftime('%Y%m%dT%H%M%S')

def make_start_year_invoice_pdf(mem):
    '''
    Creates a start year invoice for the member in question
    '''
    buffer = BytesIO()

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
    
    csv_invoice_manifest = BytesIO()

    temp = tempfile.NamedTemporaryFile(prefix="membaman-startyear-invoices-", suffix="-%s.zip" % get_local_iso(), delete=False)
    pdf_paths = []
    with zipfile.ZipFile(temp, mode='w', compression=COMPRESSION) as zf:
        for memb in queryset:
            pdfbytes = make_start_year_invoice_pdf(memb)
            zip_component_name = '%s-%s-%s.pdf' % (memb.name_given.replace(' ', '_').lower(), 
                                                   memb.name_family.replace(' ', '_').lower(), 
                                                   str(memb.id))
            zf.writestr(zip_component_name, pdfbytes)


    temp.seek(0)
    response = HttpResponse(temp.read(), 'application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(temp.name)
    response['Content-Length'] = os.path.getsize(temp.name)
    print "print_start_year_invoices ends"
    return response        
        

print_start_year_invoices.short_description = "Download Start Year invoices in a single zip file"
