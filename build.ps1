Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Compiling Springer LNCS Paper (main.tex)..." -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex

Write-Host "==========================================" -ForegroundColor Green
Write-Host "Compilation completed. Generated: main.pdf" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

