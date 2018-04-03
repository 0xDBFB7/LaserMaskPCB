cd input_files
for f in *.pdf; do
  gs -o "fixed_$f" -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite "$f"
done
