# -*- coding: utf-8 -*-

# import aaa
# from importlib import reload
#
# reload(aaa)
#
# a_object = ct3d.internal()
# 

import FreeCAD as App
import Part

D1_half = 0.5*8.376
h = Part.makeHelix(1.5, 18, D1_half)
# r1 = Part.makeRevolution(h, h.FirstParameter, h.LastParameter, 30.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
r0 = h.revolve(App.Vector(0,0,0), App.Vector(0,0,1), 30.0)

v0 = App.Vector(5, 0, 0)
v1 = App.Vector(5, 0, 12)
v2 = App.Vector(4, 0, 12)
e0 = Part.makeLine(v0, v1)
e1 = Part.makeLine(v1, v2)
r1 = Part.makeRevolution(e0, e0.FirstParameter, e0.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
r2 = Part.makeRevolution(e1, e1.FirstParameter, e1.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)

pc = Part.makeCompound([h, r1, r2])
Part.show(pc)


doc = App.ActiveDocument
if not doc:
    print('No open... ')
else:
    print('Open ...')

import FreeCADGui as Gui
from PySide import QtGui
window = Gui.getMainWindow()
items = ["Additive","Subtractive","Neither additive nor subtractive"]
item,ok =QtGui.QInputDialog.getItem(window,"Select tube type","Select whether you want additive, subtractive, or neither:",items,0,False)
