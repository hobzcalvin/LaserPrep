# Laser Prep Tools

Two simple extensions for use with Inkscape.

Copy or symlink the .py and .inx files to your Inkscape extensions folder,
usually `C:\Users\your-user-name\AppData\Roaming\inkscape\extensions` on a PC
or `~/.config/inkscape/extensions` on MacOS/Linux, or whatever location
is set in *Inkscape Preferences > System > User extensions*.
If you checkout this repository inside your user's `extensions` folder,
`ln -s LaserPrep/*.* .` will symlink all necessary files and makes it easy
to `git pull` updates.

The following extensions will appear under *Extensions > Laser Prep*:

## Flatten Strokes to Path

This allows you to specify kerf compensation in your document on a per-piece
basis, which may be necessary for exacting fits. First, use the *Stroke Width*
of paths to specify the width of kerf you want. Using the *Join: Round* stroke
style setting is recommended for smoother results.

When you're ready to cut your design, select the shapes you want to process
and run *Flatten Strokes to Path*. As basic cleanup, the extension unlinks
any clones from their parent objects and converts all objects to paths.
Then it duplicates the selected objects and uses *Stroke to Path* on the
duplicates. Then it *Union*s the duplicates with their originals,
creating new paths that have been expanded by half their stroke width.
These paths are set to black fill, no stroke, 25% opacity.

## Laser Prep

This is designed specifically for export to .DXF files, particularly for use
with RDWorks and the
[Noisebridge laser cutter](https://www.noisebridge.net/wiki/Laser_Cutter).
Use it when you're ready to save a .DXF file. This extension works on all
objects in the document, so you do not need to select anything.

This attemps to deep-ungroup all groups, converts all objects to paths,
unlinks clones from their parent objects, and then flattens all Bezier
paths. Note that this will use the last-used *Flatness* setting from
*Extensions > Modify Path > Flatten Beziers*, so make sure this is turned
all the way down to 0.1 (or how you want it) before running this extension.
That setting is preserved between Inkscape restarts, so setting it once
should be sufficient.

## Rotate for Minimum Width

Helpful when trying to nest objects, this extension rotates all selected
objects to minimize their width.

## Rotate for Minimum Bounding Box Area

Similarly, this rotates all selected objects to minimize the area of their
bounding boxes.

## Find All Optimal Rotations

This rotates the selected objects to minimize the width and area of their
bounding boxes. If these are optimized at different angles, the objects
are duplicated and rotated accordingly.

# Future
Lots more is possible here, and this was a quick and dirty solution to
speed up my workflow. It's python-only, but much more can be done with a
C++ extension. It has its hacky moments and relies on other extensions
which may change.
