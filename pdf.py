import PyPDF2
# add watermark in a pdf file

# variables

# the pdf file
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# watermark file
wtr = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# 
output = PyPDF2.PdfFileWriter()

# loop all the pages from the pdf
for i in range(template.getNumPages()):
    # set the variable
    page = template.getPage(i)
    # merge the pages with the watermark
    page.mergePage(wtr.getPage(0))
    # add it
    output.addPage(page)

    # save it and open it
    with open('wtr_output.pdf', 'wb') as file:
        output.write(file)
    