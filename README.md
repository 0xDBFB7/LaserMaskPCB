PS_INVERTED in eagle gives you a nice negative of the board. Select via layer!

Use gs -o repaired.pdf -dPDFSETTINGS=/prepress -sDEVICE=pdfwrite output.pdf to fix the output pdf.

Use inkscape's "stroke to path" feature to make the traces thicc.

Export the svg using inkscape.

Ensure that the DPI in LW's file settings matches Inkscape's png export dpi. I like 500. Also make sure the SVG px per inch is 90. Save as a png.

Use convert output.svg.png -threshold 50% thres_colored.png to flatten out the image.

Compare the final png to the svg in LaserWeb to make sure the scale didn't get messed up.

Raster at 300/100.

Make a non-inverted board mask with the dimension layer enabled. Cut outside.

The PS_inverted function puts a 0.01 in rim around the dimension layer, so you'll need to add that in when doing the finishing pass.
