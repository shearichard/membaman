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
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.units import mm, pica, inch 
from reportlab.lib.colors import pink, black, red, blue, green, grey
from reportlab.platypus import Paragraph, Frame
from reportlab.platypus.flowables import HRFlowable, XBox, Spacer, Image 
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import mm, pica, inch 
from reportlab.platypus import Paragraph, Frame
from reportlab.platypus.flowables import HRFlowable, XBox, Spacer, Image 
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import HexColor, CMYKColor, PCMYKColor, Color

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
Title = "Hello world"
pageinfo = "platypus example"
ANNUALPAYINFULLTERMS = '''Pay in full by 31st March (discounted by 10%)'''
ANNUALPAYINFULLAMOUNT = '''$898'''
ANNUALPAYONETERMTERMS = '''Pay $99 per term (due 1-Mar-15, 1-Jun-15, 1-Aug-15, 1-Nov-15)'''
ANNUALPAYONETERMAMOUNT = '''$897'''
ANNUALFEE = "$996"
PAYOPTIONBANKTRANSFER = "Pay online into the Eastern Bay Scouts Group Account. Our bank account number is : 00000 00000. Please use your reference : %s ."
PAYOPTIONBANKCHEQUE = "Some stuff about how to pay by cheque. Please write the name(s) of the child/children and your reference %s on the back of the cheque."

def makeFrame():
    objFrameTOP = Frame(pageStructure['TOP']['OffsetFromLeft'], 
                    pageStructure['TOP']['OffsetFromBottom'], 
                    pageStructure['TOP']['Width'], 
                    pageStructure['TOP']['Height'], 
                    leftPadding=0, 
                    bottomPadding=0, 
                    rightPadding=0, 
                    topPadding=0, 
                    id=None, 
                    showBoundary=pageStructure['TOP']['ShowBorder'], 
                    overlapAttachedSpace=None, 
                    _debug=None)

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


def buildHowToPayTable(mem, dic_styles):    

    data= [[Paragraph('How to pay ?', dic_styles['BIG'])],
           [Paragraph('1.', dic_styles['SMALL']), Paragraph(PAYOPTIONBANKTRANSFER % (mem.id), dic_styles['SMALL'])],
           [Paragraph('2.', dic_styles['SMALL']), Paragraph(PAYOPTIONBANKCHEQUE % (mem.id), dic_styles['SMALL'])]]

    t=Table(data,colWidths=(10*mm, None))
    t.setStyle(TableStyle([
                           ('BOTTOMPADDING',   (0, 0),  (-1, 0), 12), 
                           ('TOPPADDING',      (0, 1),  (-1, 1), 12), 
                           ('BOTTOMPADDING',   (0, 1),  (-1, 1), 12), 
                           ('VALIGN',          (0, 1),  (-1, -1), 'TOP'), 
                           ('SPAN',            (0, 0),  (-1, 0)), 
                          ]))
    return t
 
def buildPriceTable(dic_styles):
    data= [[Paragraph("Annual Fee", dic_styles['BIG']), "", Paragraph(ANNUALFEE, dic_styles['BIG'])],
           [Paragraph("Options", dic_styles['MEDIUM'])],
           [Paragraph('1.', dic_styles['SMALL']), Paragraph(ANNUALPAYINFULLTERMS, dic_styles['SMALL']), Paragraph(ANNUALPAYINFULLAMOUNT, dic_styles['SMALL'])],
           [Paragraph('2.', dic_styles['SMALL']), Paragraph(ANNUALPAYONETERMTERMS, dic_styles['SMALL']), Paragraph(ANNUALPAYONETERMAMOUNT, dic_styles['SMALL'])]]
    
    t=Table(data,colWidths=(10*mm, None, 30*mm))

#############################################################
#                          ('INNERGRID',       (0,0),   (-1,-1), 0.25, black),
#                          ('BOX',             (0,0),   (-1,-1), 0.25, black),
#############################################################

    t.setStyle(TableStyle([
                           ('TOPPADDING',      (0, 0),  (-1, 0), 12), 
                           ('BOTTOMPADDING',   (0, 0),  (-1, 0), 12), 
                           ('TOPPADDING',      (0, 1),  (-1, 1), 12), 
                           ('BOTTOMPADDING',   (0, 1),  (-1, 1), 12), 
                           ('TOPPADDING',      (0, 1),  (-1, 1), 9), 
                           ('BOTTOMPADDING',   (0, 1),  (-1, 1), 9), 
                           ('SPAN',            (0, 1),  (-1, 1)), 
                           ('SPAN',            (0, 0),  ( 1, 0)), 
                           ('VALIGN',          (0, 0),  (-1, -1), 'TOP'), 
                          ]))
    return t
def make_styles():
    BIGSIZE = 16
    MEDIUMSIZE = 14
    SMALLSIZE = 12
    TINYSIZE = 8

    dic_styles= {}

    dic_styles['BIG'] = ParagraphStyle( name='BIG', 
                        fontName = 'Helvetica-Bold', 
                        fontSize= BIGSIZE, 
                        leading = BIGSIZE*1.2) 

    dic_styles['MEDIUM'] = ParagraphStyle( name='MEDIUM', 
                        fontName = 'Helvetica-Bold', 
                        fontSize= MEDIUMSIZE, 
                        leading = MEDIUMSIZE*1.2) 

    dic_styles['SMALL'] = ParagraphStyle( name='SMALL', 
                        fontName = 'Helvetica', 
                        fontSize= SMALLSIZE, 
                        leading = SMALLSIZE*1.2) 

    dic_styles['TINY'] = ParagraphStyle( name='TINY', 
                        fontName = 'Helvetica', 
                        fontSize= TINYSIZE, 
                        leading = TINYSIZE*1.2) 

    return dic_styles


def make_start_year_invoice_pdf_platypus(buffer, mem):

    from os.path import abspath, basename, dirname, join, normpath
    from sys import path
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']
    dic_styles = make_styles()

    story = []
    #add some flowables
    path_to_hdr_img = normpath(join(settings.SITE_ROOT, 'static', 'ebsg-invoice-header.png'))
    story.append(Image(path_to_hdr_img, width=155*mm, height=42*mm))
    story.append(Spacer(width=10*mm, height=5*mm))
    story.append(Paragraph("EASTERN BAY SCOUTS GROUP INVOICE",styleH))
    story.append(Spacer(width=10*mm, height=5*mm))
    story.append(Paragraph("Hi and welcome to Scouts for 2015!", dic_styles['SMALL']))
    story.append(Spacer(width=10*mm, height=5*mm))
    story.append(buildPriceTable(dic_styles))
    story.append(Spacer(width=10*mm, height=10*mm))
    story.append(buildHowToPayTable(mem, dic_styles))
    story.append(Spacer(width=10*mm, height=10*mm))
    story.append(Paragraph("Thank you for your prompt payment", dic_styles['SMALL']))
    story.append(Spacer(width=10*mm, height=30*mm))
    story.append(Paragraph(get_local_iso(), dic_styles['TINY']))

    doc = SimpleDocTemplate(buffer,pagesize = A4)
    doc.build(story)

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
        pdfbytes = make_start_year_invoice_pdf_platypus(buffer, mem)
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
