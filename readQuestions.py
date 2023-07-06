"""
Exam parsing to LaTeX from a spreadsheet.
Read a CSV file and output a .tex file with LaTeX tables for multiple choice questions for importing in a parent LaTeX file.

The first line in the CSV file is the column header, named as:

ID = Some identifier (such as lecture number/title)
info = Extra information (such as sub-topic)
Q = Question
answer = The answer or the rubric
A = Option A
B = Option B
...

The script supports multiple variants:

- Variant 1: everything as is
- Variant 2: A replaced with D
- Variant 3: C replaced with B
- Variant 4: B replaced with D



See the included final.csv or final_images.csv for an example.
By Jan van Gemert, http://jvgemert.github.io/

"""

import csv
import wget
from string import ascii_uppercase


"""Latex strings for open questions with or without answers."""
strQ_open_ans = """\\begin{tabular}{|p{9cm}@{\\hskip 0.5cm}p{9.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\
\\midrule 
\\begin{tabular}{p{9cm}} %s 
\\end{tabular} &
\\begin{tabular}{p{9.5cm}}
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

"""Latex strings for beginning and ending MCQs with or without answers."""
strQ_begin = """\\begin{tabular}{|p{9cm}@{\\hskip 0.5cm}p{9.5cm}|} 
\\toprule  
\\textbf{Question %i} & \\emph{%s \\hfill %s}  \\\\ 
\\midrule 
\\begin{tabular}{p{9cm}}
%s 
\\end{tabular} &
\\begin{tabular}{p{9.5cm}}
"""

strQ_end = """
\\end{tabular} \\\\ \\bottomrule
\\end{tabular}
"""


strQ_boxed = """
\\textbf{\\qedsymbol %s:} %s \\\\ 
"""
strQ_checked = """
\\textbf{\\checked %s:} %s \\\\ 
"""
strQ_unchecked = """
\\textbf{\\unchecked %s:} %s \\\\ 
"""

"""Latex string for including images."""
fig = """\\includegraphics[width=9cm,height=5cm,keepaspectratio]{%s} """
fig_ans = """\\includegraphics[width=5cm,height=3cm,keepaspectratio]{%s} """


""" Parses the questions ('Q'), answers ('answer') and the multiple choice 
options ('A-..') and the open questions and formates each question.
"""
def formatQ(i, row, ans):
    # Parsing open questions
    if row['question'].startswith("Open question"):
        row['question'] = processQ('question',row['question'], isopen=True)
        if not ANSWER:
            outQ = strQ_open % (i, row['ID'], row['info'], row['question']) 
        else:  
            row['answer'] = processQ('answer',row['answer']).strip()
            outQ = strQ_open_ans % (i, row['ID'], row['info'], row['question'], row['answer']) 
    else:
        row['question'] = processQ('question', row['question'], isopen=False)
        # Add the beginning of the string
        outQ = strQ_begin % (i, row['ID'], row['info'], row['question']) 

        # Access all possible options
        for c in ascii_uppercase:
            try:
                row[c] = processQ(c, row[c]).strip()
                if len(row[c])>0:
                    if not ANSWER:
                        outQ = printQuest(outQ, c, row[c], strQ_boxed)
                    else:
                        if (row['answer'].strip()).find('Option '+c)>=0:
                            outQ = printQuest(outQ, c, row[c], strQ_checked)
                        else:
                            outQ = printQuest(outQ, c, row[c], strQ_unchecked)

            except Exception as e: 
                print("Option ",c," not implemented: ", e)
        # Add the ending of the string
        outQ = outQ + strQ_end
        
    print('----Output: ', outQ)
    return outQ
                        
def printQuest(outQ, c, rowC, str2use):
    outQ = outQ + (str2use % (c, rowC) + '\n')
    return  outQ

def processQ(key, que, isopen=False):
    que = que.strip().replace('\n','\\newline ')
    splits = que.split();
    for i in range(0, len(splits)):
        if splits[i].startswith("http"):
            splits[i] = splits[i].replace('\\newline','')
            print("Link|",splits[i],"|") 
            filename = wget.download(splits[i]) 
            if key.strip()=='answer':
                splits[i] = fig_ans % (filename) + ' '
            else:
                splits[i] = fig % (filename) + ' '

    que = " ".join(splits) 
    return que

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
        fOut.write(formatted)
        i = i + 1
fOut.close()

        
        
        
