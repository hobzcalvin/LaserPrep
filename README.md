# Laser Prep Tools

Two simple extensions for use with Inkscape.

Copy or symlink the .py and .inx files to your Inkscape extensions folder,
usually `C:\Users\your-user-name\AppData\Roaming\inkscape\extensions` on a PC
or `~/.config/inkscape/extensions` on MacOS/Linux, or whatever location
is set in `Inkscape Preferences > System > User extensions`.

The following extensions will appear under `Extensions > Laser Prep`:

## Flatten Strokes to Path

This allows you to specify kerf compensation in your document on a per-piece
basis, which may be necessary for exacting fits. First, use the Stroke Width
of paths to specify the width of kerf you want. Using the Round Join setting
is recommended for smoother results.

When you're ready to cut your design, select the shapes you want to process
and run *Flatten Strokes to Path*. As basic cleanup, the extension unlinks
any clones from their parent objects and converts all objects to paths.
Then it duplicates the selected objects and uses *Stroke to Path* on the
duplicates. Then it *Union*s the duplicates with their originals,
creating new paths that have been expanded by half their stroke width.
These paths are set to black fill, no stroke, 25% opacity.

