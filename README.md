# sheet2MCexam: Create multiple choice exam in LaTeX from a spreadsheet.

Read a CSV file and output a .tex file with LaTeX tables for multiple choice questions for importing in a parent LaTeX file.

### Requirements:

    - python 3     https://en.wikipedia.org/wiki/Python_(programming_language)
    - (pdf)latex   https://en.wikipedia.org/wiki/LaTeX

### Organization

    final.xlsx              # Spreadsheet that has the questions
    final.csv               # Exported CSV file from the spreadsheet
    readQuestions.py        # Python script to run on the CSV file
    final.tex               # Output of readQuestions.py: converted CSV to latex tables
    exam.tex                # Parent Latex document that imports the questions
    exam.pdf                # Final exam, obtained by running pdflatex on exam.tex

     
### How to use

A full example is included which was created as follows:

    1. Export the final.xlsx spreadsheet with the questions to a CSV file final.csv
    2. Run readQuestions.py to convert final.csv to a .tex file called final.tex.
    3. Run pdflatex on exam.tex to create the exam.pdf

### Spreadsheet layout

The first line in the CSV file is the column header, named as:

    ID = Some identifier (such as lecture number/title)
    info = Extra information (such as sub-topic)
    Q = Question
    A = Option A
    B = Option B
    C = Option C
    D = Option D

See the included final.xlsx sheet converted to final.csv for an example.

 
### About

I created this to make it easier to store, share, manage multiple choice questions. 

Do freely with the script as you please, no rights can be obtained from it, and if you improve it, it would be great to share.

By Jan van Gemert, http://jvgemert.github.io/

