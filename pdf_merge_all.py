import PyPDF2 as pdf2
import glob
import sys

num_of_args = len(sys.argv)
arg = sys.argv

if num_of_args < 2:
    print("Path needed as argument\n")
    exit()

merger = pdf2.PdfFileMerger()
paths = glob.glob(arg[1]+'/*.pdf')
paths.sort()

for path in paths:
    merger.append(path)

output = open(arg[1]+'/merged.pdf', 'wb')
merger.write(output)