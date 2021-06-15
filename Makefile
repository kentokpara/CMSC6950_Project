report.pdf: Report.tex
		latexmk -pdf

Report.tex: JUL_DEC.png JAN_JUN.png
		

JUL_DEC.png:
		python3 index.py

.PHONY: clean almost_clean

clean:
		rm report.pdf
		rm JUL_DEC.png 
		rm JAN_JUN.png
		
almost_clean: 
		latexmk -c
	

