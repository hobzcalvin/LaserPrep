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
from pathmodifier import PathModifier
import rotate_helper
import simpletransform

debug = False

error = lambda msg: inkex.errormsg(gettext.gettext(msg))
if debug:
    stderr = lambda msg: sys.stderr.write(msg + '\n')
else:
    stderr = lambda msg: None

class RotateMinAll(inkex.Effect):
    def effect(self):
        pm = PathModifier()
        pm.document = self.document

        for nid, node in self.selected.iteritems():
            # set() removes duplicates
            angles = set(
                # and remove Nones
                [x for x in rotate_helper.optimal_rotations(node)
                    if x is not None])
            # Go backwards so we know if we need to duplicate the node for
            # multiple rotations. (We don't want to rotate the main node
            # before duplicating it.)
            for i, angle in reversed(list(enumerate(angles))):
                if i > 0:
                    # Rotate a duplicate of the node
                    rotate_node = pm.duplicateNodes({nid: node}).items()[0][1]
                else:
                    rotate_node = node
                simpletransform.applyTransformToNode(
                    rotate_helper.rotate_matrix(rotate_node, angle),
                    rotate_node)


if __name__ == '__main__':
    rma = RotateMinAll()
    rma.affect()
