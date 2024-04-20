# -*- coding: utf-8 -*-
#
# cosmeticthread3d_partdesign.py
#
#******************************************************************************
#* Cosmetic Thread 3D Work Bench - tools for cosmetic threads creation        *
#* Copyright (C) 2024  Martin Prokš / martin(dot)proks(at)proks-martin(dot)cz *
#*                                                                            *
#* This file is part of the FreeCAD CAx development system.                   *
#*                                                                            *
#* This library is free software; you can redistribute it and/or              *
#* modify it under the terms of the GNU Lesser General Public                 *
#* License as published by the Free Software Foundation; either               *
#* version 2.1 of the License, or (at your option) any later version.         *
#*                                                                            *
#* This library is distributed in the hope that it will be useful,            *
#* but WITHOUT ANY WARRANTY; without even the implied warranty of             *
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU          *
#* Lesser General Public License for more details.                            *
#*                                                                            *
#* You should have received a copy of the GNU Lesser General Public           *
#* License along with this library; if not, write to the Free Software        *
#* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  *
#* USA                                                                        *
#******************************************************************************
"""
Definition of PythonFeature for each PartDesign version of thread geometry type.
"""

___title__  = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'

"""
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import ct3d_params



# **************************************************************** #
# **************************************************************** #
# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread Internal ...                     #
#                                                                  #
# **************************************************************** #
# **************************************************************** #
# **************************************************************** #



# +---------------------------------------------------------+
# |                                                         |
# | ViewProviderCosmeticThread3DInternal class.             |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DInternal        |
# |                                                         |
# +---------------------------------------------------------+
class ViewProviderCosmeticThread3DInternal:
    """
    FreeCAD_Gui part of the CosmeticThread3DInternal.
    This class is common for all types and versions of internal threads.
    """

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider.
        """
        obj.Proxy = self

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method
        is mandatory.
        """
        self.vobj = obj

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have
        the chance to handle this here.
        """

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        modes=[]
        modes.append('Flat Lines')
        modes.append('Shaded')
        modes.append('Wireframe')
        modes.append('Points')
        return modes

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined
        in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined
        in getDisplayModes. Since they have the same names nothing
        needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view.
        This method is optional and if not defined a default icon is shown.
        """
        return """
        /* XPM */
        static char * aaa_xpm[] = {
        "16 16 4 1",
        " 	c None",
        ".	c #000000",
        "+	c #C2C2C2",
        "@	c #0000FF",
        "                ",
        " .............. ",
        " +.@@.   .@@.++ ",
        " +.@@.   .@@.++ ",
        " +.@@.   .@@.++ ",
        " +.@@.   .@@.++ ",
        " +.@@.   .@@.++ ",
        " +.@@.   .@@.++ ",
        " +...........++ ",
        " ++++.   .+++++ ",
        " ++++.   .+++++ ",
        " ++++.   .+++++ ",
        " ++++.   .+++++ ",
        " +++++. .++++++ ",
        " ++++++.+++++++ ",
        "                "};
        """

    def dumps(self):
        """
        Called during document saving.
        """

    def loads(self,state):
        """
        Called during document restore.
        """



# +------------------------------------------------------------+
# |                                                            |
# | internal_p0() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_pd0(name='CosmeticThread3DInternal', ct3di_prms=None):
    """
    internal_pd0(name, ct3di_prms) -> obj

    It creates Cosmetic Thread 3D Internal (PartDesign version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]               name of the object in the model tree
    ct3di_prms - [ct3di_params_class]   parameters of the cosmetic thread
    """

    body = None
    obj = None
    #
    body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
    if not body:
        App.Console.PrintError("No active body.\n")
    elif body.Tip is None:
        App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
    elif ct3di_prms is None:
        App.Console.PrintError('internal_pd0(name, ct3di_prms, aPart) - Check ct3di_prms\n')
    else:
        obj = None
        if (name is None) or (name == ''):
            name = ct3di_prms.name
        obj = App.ActiveDocument.addObject('PartDesign::FeatureSubtractivePython', name)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        obj.ViewObject.ShapeColor=body.ViewObject.ShapeColor
        obj.ViewObject.LineColor=body.ViewObject.LineColor
        obj.ViewObject.PointColor=body.ViewObject.PointColor
        obj.ViewObject.Transparency=body.ViewObject.Transparency
        obj.ViewObject.DisplayMode=body.ViewObject.DisplayMode
        obj.ViewObject.makeTemporaryVisible(True)
        CosmeticThread3DInternal_pd0(obj, ct3di_prms)
        body.addObject(obj) # optionally we can also use body.insertObject()
        # App.ActiveDocument.recompute()
    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p0 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_pd0:
    """
    CosmeticThread3DInternal_pd0 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal_pd0() above.
    """
    
    # https://wiki.freecad.org/Scripted_objects - PartDesign, pay attention to attachment...
    
    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)
        
        constructor of a CosmeticThread3DInternal_pd0 class / internall
        function.
        """
        #
        self.Type = 'CosmeticThread3DInternal_pd0'
        obj.Proxy = self
        # Add property of internal thread into obj 
        ct3d_params.addProperty_internal_thread(obj, ct3di_prms)
        # Attachement extension
        self.makeAttachable(obj)

    def makeAttachable(self, obj):
        if int(App.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)
        obj.setEditorMode('Placement', 0) # non-readonly non-hidden

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed.
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory.
        """
        # Three 1/3 of annulus with small gaps and upper disk...
        ct3dSolid = None
        t = 0.01 # something small
        #
        # revolved shape - solid
        v = []
        v.append(App.Vector(0, 0, -4*t))
        v.append(App.Vector(0.5*obj.D.Value, 0, -4*t))
        v.append(App.Vector(0.5*obj.D.Value, 0, obj.length.Value))
        v.append(App.Vector(0.5*obj.D1.Value - 1.5*t, 0, obj.length.Value))
        v.append(App.Vector(0.5*obj.D1.Value - 1.5*t, 0, obj.length.Value - t))
        v.append(App.Vector(0.5*obj.D.Value - t, 0, obj.length.Value - t))
        v.append(App.Vector(0.5*obj.D.Value - t, 0, -3*t))
        v.append(App.Vector(0, 0, -3*t))
        v.append(App.Vector(0, 0, -4*t))
        wire = Part.makePolygon(v)
        face = Part.Face(wire)
        revolved_shape = face.revolve(App.Vector(0, 0, 0), \
                                      App.Vector(0, 0, 1), \
                                      360)
        # slots
        v = []
        v.append(App.Vector(0.5*obj.D1.Value - 3*t, -1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D1.Value - 3*t, 1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D.Value + 1.5*t, 1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D.Value + 1.5*t, -1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D1.Value - 3*t, -1.5*t, -5*t))
        wire = Part.makePolygon(v)
        face = Part.Face(wire)
        slot = face.extrude(App.Vector(0, 0, obj.length.Value + 10*t))
        slot0 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0)
        slot1 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0 + 120)
        slot2 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0 + 240)
        # final solid of cosmetic thread
        ct3dSolid = revolved_shape.cut([slot0, slot1, slot2])
        #
        # Apply attachement to the ct3dSolid
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        ct3dSolid.Placement = obj.Placement
        #
        # remove cosmetic thread from body
        full_shape = obj.BaseFeature.Shape.cut(ct3dSolid)
        full_shape.transformShape(obj.Placement.inverse().toMatrix(), True)
        obj.Shape = full_shape
        #
        # Subshape for patterns
        ct3dSolid.transformShape(obj.Placement.inverse().toMatrix(), True)
        obj.AddSubShape = ct3dSolid



# **************************************************************** #
# **************************************************************** #
# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread External ...                     #
#                                                                  #
# **************************************************************** #
# **************************************************************** #
# **************************************************************** #



# +---------------------------------------------------------+
# |                                                         |
# | ViewProviderCosmeticThread3DExternal class.             |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DExternal        |
# |                                                         |
# +---------------------------------------------------------+
class ViewProviderCosmeticThread3DExternal:
    """
    FreeCAD_Gui part of the CosmeticThread3DExternal.
    This class is common for all types and versions of internal threads.
    """

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider.
        """
        obj.Proxy = self

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method
        is mandatory.
        """
        self.vobj = obj

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have
        the chance to handle this here.
        """

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        modes=[]
        modes.append('Flat Lines')
        modes.append('Shaded')
        modes.append('Wireframe')
        modes.append('Points')
        return modes

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined
        in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined
        in getDisplayModes. Since they have the same names nothing
        needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed.
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view.
        This method is optional and if not defined a default icon is shown.
        """

        return """
        /* XPM */
        static char * external_thread_xpm[] = {
        "16 16 9 1",
        " 	c #FFFFFF",
        ".	c #000000",
        "+	c #2597FB",
        "@	c #2494F7",
        "#	c #3C98F6",
        "$	c #080808",
        "%	c #2493F4",
        "&	c #388FE7",
        "*	c #2495F7",
        "       ..       ",
        "     ......     ",
        "    ..++++..    ",
        "   ..++++++..   ",
        "   ...@+++...   ",
        "   .+......#.   ",
        "   .+.+..+.+.   ",
        "   .+.++++.+.   ",
        "   .+.++++.+.   ",
        "   $+.++++.+.   ",
        "   ...%+++...   ",
        "   .+......+.   ",
        "   .+%&..+*+.   ",
        "   .++++++++.   ",
        "   .++++++++.   ",
        "      ++++      "};
        """

    def dumps(self):
        """
        Called during document saving.
        """

    def loads(self,state):
        """
        Called during document restore.
        """



# +-------------------------------------------------------------+
# |                                                             |
# | external_pd0() - create external thread object and geometry |
# |                                                             |
# +-------------------------------------------------------------+
def external_pd0(name='CosmeticThread3DExternal', ct3de_prms=None):
    """
    external_pd0(name, ct3de_prms) -> obj

    creates Cosmetic Thread 3D External (Part Design version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]               name of the object in the model tree
    ct3de_prms   - [ct3de_params_class]   parameters of the cosmetic thread
    """

    body = None
    obj = None
    #
    body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
    if not body:
        App.Console.PrintError("No active body.\n")
    elif body.Tip is None:
        App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
    elif ct3de_prms is None:
        App.Console.PrintError('external_pd0(name, ct3de_prms, aPart) - Check ct3de_prms\n')
    else:
        obj = None
        if (name is None) or (name == ''):
            name = ct3de_prms.name
        obj = App.ActiveDocument.addObject('PartDesign::FeatureSubtractivePython', name)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        obj.ViewObject.ShapeColor=body.ViewObject.ShapeColor
        obj.ViewObject.LineColor=body.ViewObject.LineColor
        obj.ViewObject.PointColor=body.ViewObject.PointColor
        obj.ViewObject.Transparency=body.ViewObject.Transparency
        obj.ViewObject.DisplayMode=body.ViewObject.DisplayMode
        obj.ViewObject.makeTemporaryVisible(True)
        CosmeticThread3DExternal_pd0(obj, ct3de_prms)
        body.addObject(obj) # optionally we can also use body.insertObject()
        # App.ActiveDocument.recompute()
    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_pd0 class.                     |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_pd0:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)
        
        constructor of a CosmeticThread3DExternal class / internall function
        """
        
        self.Type = 'CosmeticThread3DExternal_pd0'
        obj.Proxy = self
        ct3d_params.addProperty_external_thread(obj, ct3de_prms)
        # Attachement extension
        self.makeAttachable(obj)
        
    def makeAttachable(self, obj):
        if int(App.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)
        obj.setEditorMode('Placement', 0) #non-readonly non-hidden

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed.
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory.
        """
        # Three 1/3 of annulus with small gaps and upper disk...
        ct3dSolid = None
        t = 0.01 # something small
        #
        # revolved shape - solid
        v = []
        v.append(App.Vector(0.5*obj.d3.Value, 0, -4*t))
        v.append(App.Vector(0.5*obj.d3.Value, 0, obj.length.Value))
        v.append(App.Vector(0.5*obj.D.Value + 1.5*t, 0, obj.length.Value))
        v.append(App.Vector(0.5*obj.D.Value + 1.5*t, 0, obj.length.Value - t))
        v.append(App.Vector(0.5*obj.d3.Value + t, 0, obj.length.Value - t))
        v.append(App.Vector(0.5*obj.d3.Value + t, 0, -4*t))
        v.append(App.Vector(0.5*obj.d3.Value, 0, -4*t))
        wire = Part.makePolygon(v)
        face = Part.Face(wire)
        revolved_shape = face.revolve(App.Vector(0, 0, 0), \
                                      App.Vector(0, 0, 1), \
                                      360)
        # slots
        v = []
        v.append(App.Vector(0.5*obj.D.Value + 3*t, -1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D.Value + 3*t, 1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.d3.Value - 1.5*t, 1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.d3.Value - 1.5*t, -1.5*t, -5*t))
        v.append(App.Vector(0.5*obj.D.Value + 3*t, -1.5*t, -5*t))
        wire = Part.makePolygon(v)
        face = Part.Face(wire)
        slot = face.extrude(App.Vector(0, 0, obj.length.Value + 10*t))
        slot0 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0)
        slot1 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0 + 120)
        slot2 = slot.rotated(App.Vector(0, 0, 0), \
                             App.Vector(0, 0, 1), \
                             360.0/13.0 + 240)
        # final solid of cosmetic thread
        ct3dSolid = revolved_shape.cut([slot0, slot1, slot2])
        #
        # Apply attachement to the ct3dSolid
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        ct3dSolid.Placement = obj.Placement
        #
        # remove cosmetic thread from body
        full_shape = obj.BaseFeature.Shape.cut(ct3dSolid)
        full_shape.transformShape(obj.Placement.inverse().toMatrix(), True)
        obj.Shape = full_shape
        #
        # Subshape for patterns
        ct3dSolid.transformShape(obj.Placement.inverse().toMatrix(), True)
        obj.AddSubShape = ct3dSolid

