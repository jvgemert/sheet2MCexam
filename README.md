# sheet2MCexam: Create multiple choice exam in LaTeX from a spreadsheet.

Read a CSV file and output a .tex file with LaTeX tables for multiple choice questions for importing in a parent LaTeX file.

### Requirements:

    - python 3     https://en.wikipedia.org/wiki/Python_(programming_language)
    - (pdf)latex   https://en.wikipedia.org/wiki/LaTeX

### Organization

    final.xlsx              # Spreadsheet that has the questions
    final.csv               # Exported CSV file from the spreadsheet
    final_images.csv        # Exported CSV file from the spreadsheet using images with links
    readQuestions.py        # Python script to run on the CSV file
    final.tex               # Output of readQuestions.py: converted CSV to latex tables
    exam.tex                # Parent Latex document that imports the questions
    exam.pdf                # Final exam, obtained by running pdflatex on exam.tex
    Makefile                # Makefile that runs everything for simplicity
    example.png             # Example image linked to from final_images.csv

### How to use

A full example is included which was created as follows:

    1. Export the final.xlsx spreadsheet with the questions to a CSV file final.csv
    2. Run readQuestions.py to convert final.csv to a .tex file called final.tex.
    3. Run pdflatex on exam.tex to create the exam.pdf

Or using the Makefile:

    1. Run "make"

### Spreadsheet layout

The first line in the CSV file is the column header, named as:

    ID = Some identifier (such as lecture number/title)
    info = Extra information (such as sub-topic)
    Q = Question
    A = Option A
    B = Option B
    C = Option C
    D = Option D
    answer = The correct option. Make sure to use "Option A", "Option B", "Option C", "Option D" 

For open questions:

    Make sure to start the question with: "Open question: ..."
    Write: N.A. at the Options A, B, C, D
    Write the grading rubric under the "answer" column.

- Do not use "&" or other characters unescaped in the text. 

- Write all the formulas in latex format: e.g. $\theta = \frac{a}{b}$. 

- Use double new lines when you want them to appear and none for the rest.

See the included final.xlsx sheet converted to final.csv for an example.


### How to use images

#### Using Dropbox:

    - Upload images to Dropbox and make them sharebale for "Everyone with this link".
    - Copy the sharable link in the question or answer and make sure to replace "dl=0" with "dl=1": e.g. https://www.dropbox.com/s/zth9509ppmdlxsl/example.png?dl=1

#### Using direct links to images:
   
    - Simply use the image link in the question or answer: e.g. https://raw.githubusercontent.com/jvgemert/sheet2MCexam/master/example.png 
 
### About

I created this to make it easier to store, share, manage multiple choice questions. 

Do freely with the script as you please, no rights can be obtained from it, and if you improve it, it would be great to share.

By Jan van Gemert, http://jvgemert.github.io/

