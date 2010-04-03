TEXFILE = tmp.tex

main:
	./mt.py > $(TEXFILE)
	xelatex $(TEXFILE)

copy:
	cp $(TEXFILE:.tex=.pdf) ../doc/jpn.pdf

view:
	evince $(TEXFILE:.tex=.pdf)

clean :
	rm -f *.tex *.log *.toc *.aux *.pdf *~ 


