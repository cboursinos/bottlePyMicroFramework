# -*- coding: utf-8 -*-

from settings import membershost
import os
from xhtml2pdf import pisa
from StringIO import StringIO


def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
    pisaStatus = pisa.CreatePDF(
        sourceHtml,                # the HTML to convert
        dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    return pisaStatus.err