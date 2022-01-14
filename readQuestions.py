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

import wget

# the latex formatted table used for each question
strQ_open_ans = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\
\\midrule 
\\begin{tabular}{p{8cm}} %s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{Rubric:} \\newline 
%s  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""

strQ_open = """
\\begin{tabular}{|p{19cm}|} 
\\toprule  
\\textbf{Question %i}\\hfill \\emph{%s \\hfill %s}  \\\\
\\midrule 
%s \\\\ 
\\bottomrule
\\end{tabular}
"""

strQ = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\ 
\\midrule 
\\begin{tabular}{p{8cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{\\unchecked A:} %s \\newline 
\\textbf{\\unchecked B:} %s \\newline  
\\textbf{\\unchecked C:} %s \\newline  
\\textbf{\\unchecked D:} %s \\newline  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""

strQ_A = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\ 
\\midrule 
\\begin{tabular}{p{8cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{\\checked A:} %s \\newline 
\\textbf{\\unchecked B:} %s \\newline  
\\textbf{\\unchecked C:} %s \\newline  
\\textbf{\\unchecked D:} %s \\newline  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""

strQ_B = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\  
\\midrule 
\\begin{tabular}{p{8cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{\\unchecked A:} %s \\newline 
\\textbf{\\checked B:} %s \\newline  
\\textbf{\\unchecked C:} %s \\newline  
\\textbf{\\unchecked D:} %s \\newline  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""

strQ_C = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\ 
\\midrule 
\\begin{tabular}{p{8cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{\\unchecked A:} %s \\newline 
\\textbf{\\unchecked B:} %s \\newline  
\\textbf{\\checked C:} %s \\newline  
\\textbf{\\unchecked D:} %s \\newline  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""

strQ_D = """
\\begin{tabular}{|p{8cm}@{\\hskip 0.5cm}p{10.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\ 
\\midrule 
\\begin{tabular}{p{8cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{10.5cm}}
\\textbf{\\unchecked A:} %s \\newline 
\\textbf{\\unchecked B:} %s \\newline  
\\textbf{\\unchecked C:} %s \\newline  
\\textbf{\\checked D:} %s \\newline  
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""
    
fig = """
\\includegraphics[width=7cm,height=6cm,keepaspectratio]{%s} 
"""


# apply the formatting to each question
def formatQ(i, row, ans):
    row['Q'] = processQ(row['Q'])
    row['A'] = processQ(row['A'])
    row['B'] = processQ(row['B'])
    row['C'] = processQ(row['C'])
    row['D'] = processQ(row['D'])

    if not ANSWER:
        outQ = strQ % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
        if row['Q'].startswith("Open"):
            outQ = strQ_open % (i, row['ID'], row['info'], row['Q']) + '\n'

    else:
        if ans == "Option A":
            outQ = strQ_A % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
        elif ans == "Option B":
            outQ = strQ_B % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
        elif ans == "Option C":
            outQ = strQ_C % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
        elif ans == "Option D":
            outQ = strQ_D % (i, row['ID'], row['info'], row['Q'], row['A'], row['B'], row['C'], row['D']) + '\n'
        elif row['Q'].startswith("Open"):
            outQ = strQ_open_ans % (i, row['ID'], row['info'], row['Q'], row['answer']) + '\n'
        
    print('----Output: ', outQ)
    return outQ


def processQ(que):
    splits = que.split();
    for i in range(0, len(splits)):
        if splits[i].strip().startswith("http"):
            print("Link|",splits[i].strip(),"|") 
            filename = wget.download(splits[i].strip()) 
            splits[i] = fig % (filename) + '\n'
        splits[i] = splits[i].replace('\n','\\newline')
    return " ".join(splits) 

# File name of the output .tex file
fNameOut = 'final.tex'
fOut = open(fNameOut, 'wt')


ANSWER=True # NOTE: Set to False for the final exam

# start with question i=1
i = 1
with open('final_images.csv', 'rt') as fIn:
    reader = csv.DictReader(fIn, delimiter=';',)
    #reader = csv.DictReader(fIn)
    for row in reader:
        print('Question %d' % i)
        ans = (row['answer']).strip()
        formatted = formatQ(i, row, ans)
        fOut.write( formatted )
        i = i + 1
fOut.close()

        
        
        
