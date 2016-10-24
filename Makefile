# stop echo of command on termianl
.SILENT: all		

FILES := lv_model_report.tex
AUXFILES := $(FILES:.tex=.aux)
LOGFILES := $(FILES:.tex=.log)
BBLFILES := $(FILES:.tex=.bbl)
BLGFILES := $(FILES:.tex=.blg)

# && \ used to run command as it is running in single shell.
all:
	cd source/ && \
	python frequencyplot.py && \
	python phase_plot.py && \
	python animation.py && \
	pdflatex lv_model_report && \
	bibtex lv_model_report && \
	pdflatex lv_model_report  && \
	pdflatex lv_model_report && \
	mv *.pdf ../output/153076005.pdf && \
	mv *.mp4 ../output/animation.mp4 && \
	cp *.html ../output/153076005.html 

clean:
	cd source/ && \
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) && \
	rm -f *.pyc && \
	rm -f *.out && \
	rm -f *.jpg 
	rm -rf output/
