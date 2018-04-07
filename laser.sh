

echo "repairing PDF files"
./fix_pdfs.sh

echo "exporting files as SVG"
inkscape --without-gui \
	--file="input_files/fixed_board_top.pdf" \
	--export-plain-svg="output_files/fixed_board_top.svg"

inkscape --without-gui \
	--file="input_files/fixed_board_bottom.pdf" \
	--export-plain-svg="output_files/fixed_board_bottom.svg"

inkscape --without-gui \
	--file="input_files/fixed_stencil.pdf" \
	--export-plain-svg="output_files/fixed_stencil.svg"

inkscape --without-gui \
	--file="input_files/fixed_stencil.pdf" \
	--export-plain-svg="output_files/fixed_stencil.svg"

inkscape --without-gui \
	--file="input_files/fixed_fudicials.pdf" \
	--export-plain-svg="output_files/fixed_fudicials.svg"

echo "Simplifying SVGs" 

inkscape \
	--file="output_files/fixed_board_top.svg" \
	--select="g12" \
	--verb=SelectionUnGroup \
	--select="g14" \
	--verb=SelectionUnGroup \
	--select="g16" \
	--verb=SelectionUnGroup \
	--verb=StrokeToPath \
	--verb=SelectionUnion \
	--verb=FileSave \
	--verb=FileQuit 

inkscape \
	--file="output_files/fixed_board_bottom.svg" \
	--select="g12" \
	--verb=SelectionUnGroup \
	--select="g14" \
	--verb=SelectionUnGroup \
	--select="g16" \
	--verb=SelectionUnGroup \
	--verb=StrokeToPath \
	--verb=SelectionUnion \
	--verb=FileSave \
	--verb=FileQuit 

inkscape --without-gui \
	--file="input_files/fixed_board_top.pdf" \
	--export-dpi=500 \
	--export-id="g12" \
	--export-png="output_files/fixed_board_top.png"

inkscape --without-gui \
	--file="input_files/fixed_board_top_inverted.pdf" \
	--export-dpi=500 \
	--export-id="g12" \
	--export-png="output_files/fixed_board_top_inverted.png"

inkscape --without-gui \
	--file="input_files/fixed_board_bottom_inverted.pdf" \
	--export-dpi=500 \
	--export-id="g12" \
	--export-png="output_files/fixed_board_bottom_inverted.png"

python via_drills.py
python locator_drills.py
./binarize.sh
