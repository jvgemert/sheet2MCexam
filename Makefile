exam.pdf: exam.tex
	python readQuestions.py

	pdflatex exam.tex

	rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *.blg *.bbl *.png
clean:
	rm -f *.ps *.dvi *.aux *.toc *.idx *.ind *.ilg *.log *.out *.blg *.bbl *.png
