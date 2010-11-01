TEXFILE = tmp.tex

main:
	./mt.py > $(TEXFILE)
	xelatex $(TEXFILE)
	xelatex $(TEXFILE)        # run it twice
	cp $(TEXFILE:.tex=.pdf) ../doc/jpn.pdf

copy:
	cp $(TEXFILE:.tex=.pdf) ../doc/jpn.pdf

view:
	evince $(TEXFILE:.tex=.pdf) &

clean :
	rm -f $(TEXFILE:.tex=*) *~ *.pyc


