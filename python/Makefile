TEXFILE = tmp.tex

main:
	./mt.py > $(TEXFILE)
	xelatex $(TEXFILE)

copy:
	cp $(TEXFILE:.tex=.pdf) ../doc/jpn.pdf

clean :
	rm *.log *.toc *.aux *.pdf
