all: textbook.pdf

textbook.pdf: textbook.tex functions.tex notes.tex $(wildcard lessons/*/*.tex)
	xelatex textbook.tex

clean:
	-rm -f textbook.pdf
	-rm -f *.aux
	-rm -f *.log
	-rm -f *.toc
	-rm -f *.out
	-rm -f lessons/*/*.aux
