"""
Multiple choice exam in LaTeX from a spreadsheet.

Read a CSV file and output a .tex file with LaTeX tables for multiple choice questions for importing in a parent LaTeX file.

The first line in the CSV file is the column header, named as:

ID = Some identifier (such as lecture number/title)
info = Extra information (such as sub-topic)
Q = Question
A = Option A
B = Option B
C = Option C
D = Option D

See the included final.xlsx sheet converted to final.csv for an example.

By Jan van Gemert, http://jvgemert.github.io/

"""

import csv


# the latex formatted table used for each question
strQ = """
\\begin{tabular}{p{6cm}p{12.5cm}|} 
\\textbf{Question %i} & \\emph{%s \hfill %s}  \\\\ \\toprule  
%s & 
\\textbf{A:} %s \\newline 
\\textbf{B:} %s \\newline  
\\textbf{C:} %s \\newline  
\\textbf{D:} %s \\\\ \\bottomrule 
\\end{tabular}
"""

# apply the formatting to each question
def formatQ(i, row):
    outQ = strQ % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
    print('----Output: ', outQ)
    return outQ

# File name of the output .tex file
fNameOut = 'final.tex'
fOut = open(fNameOut, 'wt')

# start with question i=1
i = 1
with open('final.csv', 'rt') as fIn:
    reader = csv.DictReader(fIn, delimiter=';',)
    for row in reader:
        print('Question %d' % i)
        formatted = formatQ(i, row)
        fOut.write( formatted )
        i = i + 1
fOut.close()

        
        
        
