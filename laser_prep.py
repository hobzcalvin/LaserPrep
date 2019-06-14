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
import re
import sys

import inkex
import simplepath
#import simplestyle

from synfig_prepare import InkscapeActionGroup, SynfigExportActionGroup
from pathmodifier import PathModifier

debug = True

error = lambda msg: inkex.errormsg(gettext.gettext(msg))
if debug:
    stderr = lambda msg: sys.stderr.write(msg + '\n')
else:
    stderr = lambda msg: None


class LaserPrep(inkex.Effect):

    def effect(self):
        a = SynfigExportActionGroup(self.document)

        for i in range(10):
            a.select_xpath('//svg:g')
            a.verb('SelectionUnGroup')

        a.objects_to_paths()
        a.unlink_clones()
        self.document = a.run_document()

        a = InkscapeActionGroup(self.document)
        a.select_xpath('//svg:path')
        a.verb('org.ekips.filter.flatten.noprefs')
        self.document = a.run_document()


if __name__ == '__main__':
    lp = LaserPrep()
    lp.affect()
