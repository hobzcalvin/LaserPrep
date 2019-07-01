#! /usr/bin/env python
'''
Copyright (C) 2019 Grant Patterson <grant@revoltlabs.co>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import gettext
import sys

import inkex
import rotate_helper
import simpletransform

debug = False

error = lambda msg: inkex.errormsg(gettext.gettext(msg))
if debug:
    stderr = lambda msg: sys.stderr.write(msg + '\n')
else:
    stderr = lambda msg: None

class RotateMinBBox(inkex.Effect):
    def effect(self):
        for node in self.selected.values():
            min_bbox_angle = rotate_helper.optimal_rotations(node)[1]
            if min_bbox_angle is not None:
                simpletransform.applyTransformToNode(
                    rotate_helper.rotate_matrix(node, min_bbox_angle), node)


if __name__ == '__main__':
    rmw = RotateMinBBox()
    rmw.affect()
