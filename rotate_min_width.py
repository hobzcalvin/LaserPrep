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
from math import cos, pi, sin
import sys

import inkex
import simpletransform

debug = False

error = lambda msg: inkex.errormsg(gettext.gettext(msg))
if debug:
    stderr = lambda msg: sys.stderr.write(msg + '\n')
else:
    stderr = lambda msg: None

STEPS = 360

class RotateMinWidth(inkex.Effect):

    def effect(self):
        for node in self.selected.values():
            bbox = simpletransform.computeBBox([node])
            cx = (bbox[0] + bbox[1]) / 2.0
            cy = (bbox[2] + bbox[3]) / 2.0

            def rotateMatrix(a):
                return simpletransform.composeTransform(
                    [[cos(a), -sin(a), cx], [sin(a), cos(a), cy]],
                    [[1, 0, -cx], [0, 1, -cy]])

            step = pi / float(STEPS)
            minwidth = bbox[1] - bbox[0]
            minangle = 0
            for i in range(STEPS):
                angle = -pi/2.0 + i*step
                rotated = simpletransform.computeBBox(
                    [node], rotateMatrix(angle))
                width = rotated[1] - rotated[0]
                if width < minwidth:
                    minwidth = width
                    minangle = angle
            if minangle != 0:
                simpletransform.applyTransformToNode(
                    rotateMatrix(minangle), node)


if __name__ == '__main__':
    rmw = RotateMinWidth()
    rmw.affect()
