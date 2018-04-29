![Test 1](/test_1.jpg)
![Test 2](/test_2.jpg)

### Some background

After watching [this video](https://www.youtube.com/watch?v=1hFNj86L7sk) from Marco Reps on using an Eleksmaker A3 laser cutter with a paint mask technique for PCB manufacturing, I figured I'd try to set up a system for prototype production.

This led me down a rabbit hole that ended with me getting sprayed in the face by a jet of chlorine gas and hydrochloric acid.

#### But why

###### boards are so cheap these days, just order them in

In my style of R&D (that is, "be disorganized and fail every time at everything"), the rate at which you can iterate designs seems to be essential. After each board revision, you gather more data and characterize your design slightly more - and any lag between new information and new hardware seems to impede the process significantly. This lag component only be an issue for me, though - someone more competent may have other predictors for success.

Over the last few years, I've tried off-and-on to etch my own boards - however, all the techniques I'd tried had serious repeatability issues. 

We generally use a local PCB supplier for our prototype boards, meaning that our hardware lag is about 3 days.

With the laser cutter, we were able to build a complete, populated PCB in under 3 hours.

It still isn't worth it.

#### Code

Like CNC trace milling, Marco produced his boards using a single, laser-width isolation, using a vector file of his board. Because of the small dot size of the laser cutter, I found this very difficult to solder, even with a reflow oven. I wanted something with a configurable isolation region.

This repo includes an Eagle CAM job for generating all the files required to build a double-sided board, a set of scripts for generating G-code for drilling, a set of bash scripts for processing the CAM generated files, and a LaserWeb4 workspace file that etches all the layers (and a paste stencil!).

To use, just:

	1. Buy a LaserWeb compatible laser
	2. Install ghostscript and inkscape on a Debian-like distro
	3. Run laser.cam on your board using Eagle.
	4. Copy over the generated files
	5. Run laser.sh
	6. Import the laserweb workspace
	7. Select the workspace layers
	9. Put a pre-masked board in your laser cutter [see below]
	8. Put on your goggles
	9. Laser!
	10. Etch the board in your choice of solution [see below]
	11. Cut the stencil on the laser
	12. Reflow
	13. Profit!


#### Process parameters

I have several pages of notes that I have yet to transfer into a human-readable form.





