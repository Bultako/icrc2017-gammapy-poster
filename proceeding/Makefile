TARGET=gammapy-icrc2017
LATEX=pdflatex
BIBTEX=bibtex

all: $(TARGET).pdf

$(TARGET).pdf: *.tex $(TARGET).bib

%.pdf: %.tex
	$(LATEX) $<
	$(BIBTEX) $*
	$(LATEX) $<
	$(LATEX) $<

make clean:
	- rm -f $(TARGET).pdf $(TARGET).aux $(TARGET).log $(TARGET).bbl $(TARGET).blg *.aux $(TARGET).tar.gz

# Tarball for ArXiv submission
tarball:
	- tar -cvzf $(TARGET).tar.gz \
	$(TARGET).tex \
	$(TARGET).bib \
	$(TARGET).bbl \
	figures/gammapy-stack.pdf \
	figures/gammapy_example_sky_image.png \
	examples/code_events_image.pdf \
	PoSlogo.pdf \
	JHEP.bst \
	PoS.cls \
	Makefile \
