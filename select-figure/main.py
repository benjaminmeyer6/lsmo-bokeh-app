# -*- coding: utf-8 -*-
# pylint: disable=unsubscriptable-object, too-many-locals
from __future__ import print_function
from os.path import dirname, join

from bokeh.layouts import layout
import bokeh.models as bmd
from bokeh.io import curdoc

html = bmd.Div(
    text=open(join(dirname(__file__), "static", "table.html")).read(),
    width=960)

# Put the tabs in the current document for display
curdoc().title = "C-C Cross-Coupling Genome"
curdoc().add_root(layout([html]))
