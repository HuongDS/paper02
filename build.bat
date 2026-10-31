@echo off
echo ==========================================
echo Compiling Springer LNCS Paper (main.tex)...
echo ==========================================

pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

echo ==========================================
echo Compilation completed. Generated: main.pdf
echo ==========================================

