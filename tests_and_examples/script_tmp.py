# -*- coding: utf-8 -*-
__title__   = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'

# import aaa
# from importlib import reload
# reload(aaa)

# import cosmeticthread3d_Gui
# from importlib import reload
# reload(cosmeticthread3d_Gui)
# a = cosmeticthread3d_Gui.ct3di_menu_command
# cosmeticthread3d_Gui.ct3di_menu_command.Activated(a)
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




# Attachement GUI report...
doc = App.ActiveDocument
obj = App.getDocument('testing_model_for_TechDraw').getObject('M10')
# obj = xxxxx

import Show
from Show.Containers import isAContainer

obj_tv = Show.TempoVis(doc, tag= 'PartGui::TaskAttacher')
dep_features = obj_tv.get_all_dependent(obj, '')
dep_features = [o for o in dep_features if not isAContainer(o)]
if obj.isDerivedFrom('PartDesign::CoordinateSystem'):
	visible_features = [feat for feat in obj.InList if feat.isDerivedFrom('PartDesign::FeaturePrimitive')]
	dep_features = [feat for feat in dep_features if feat not in visible_features]
	del(visible_features)
obj_tv.hide(dep_features)
del(dep_features)
if not obj.isDerivedFrom('PartDesign::CoordinateSystem'):
		if len(obj.Support) > 0:
			obj_tv.show([lnk[0] for lnk in obj.Support])
obj.AttachmentOffset = App.Placement(App.Vector(0.0000000000, 0.0000000000, 0.0000000000),  App.Rotation(0.0000000000, 0.0000000000, 0.0000000000))
obj.MapReversed = True
obj.Support = [(doc.getObject('Cut'),'Edge14')]
obj.MapPathParameter = 0.000000
obj.MapMode = 'Concentric'
obj.recompute()
doc.resetEdit()
obj_tv.restore()
del(obj_tv)

obj_tmp = doc.addObject("Part::Cone","Cone")
obj_tmp.Label = "Cone"
doc.recompute()
obj_tmp.Radius1 = '0 mm'
obj_tmp.Radius2 = '2 mm'
obj_tmp.Height = '5 mm'

