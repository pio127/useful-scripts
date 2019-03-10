import PyPDF2 as pdf2
import sys

num_of_args = len(sys.argv)
arg = sys.argv
if num_of_args < 4:
    print("3 arguments needed:\n  1. Filename \n  2. First page number\n  3. Last page number")
    exit()

pdf_obj = open(arg[1], 'rb')
pdf_input = pdf2.PdfFileReader(pdf_obj)
pdf_output = open('output.pdf', 'wb')
pdf_writer = pdf2.PdfFileWriter()

for page in range(int(arg[2])-1, int(arg[3])+1):
    page_obj = pdf_input.getPage(page)
    pdf_writer.addPage(page_obj)

pdf_writer.write(pdf_output)
pdf_output.close()
pdf_obj.close()