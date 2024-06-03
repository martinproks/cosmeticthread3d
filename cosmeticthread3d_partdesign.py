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
___title__ = 'Cosmetic Thread 3D Work Bench'
__author__ = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__ = 'https://github.com/martinproks/cosmeticthread3d'
"""
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External
"""

import FreeCAD as App
import Part
import ct3d_params

# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread Internal ...                     #
#                                                                  #
# **************************************************************** #

# +---------------------------------------------------------+
# | ViewProvider_ct3di class.                               |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DInternal        |
# +---------------------------------------------------------+
class ViewProvider_ct3di:
    """
    FreeCAD_Gui part of the CosmeticThread3DInternal.
    This class is common for all types and versions of internal threads.
    """

    def __init__(self, obj, body):
        """
        Set this object to the proxy object of the actual view provider.
        """
        obj.Proxy = self
        # obj.DisplayMode = body.DisplayMode
        # obj.DrawStyle = body.DrawStyle
        # obj.LineColor = body.LineColor
        # obj.LineWidth = body.LineWidth
        # obj.PointColor = body.PointColor
        # obj.PointSize = body.PointSize
        # if int(App.Version()[1]) >= 22:
        #     obj.ShapeAppearance = body.ShapeAppearance
        # else:
        #     obj.ShapeColor = body.ShapeColor
        # obj.Transparency = body.Transparency
        obj.DrawStyle = 'Dashed'
        obj.LineColor = (0, 0, 0)
        obj.LineWidth = 1.0
        obj.PointColor = (25, 25, 25)
        obj.PointSize = 1.0
        obj.Transparency = 0

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

    def getDisplayModes(self, obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined
        in getDisplayModes.
        """
        return "Wireframe"

    def setDisplayMode(self, mode):
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

    def loads(self, state):
        """
        Called during document restore.
        """

# +-------------------------------------------------------------+
# | internal() - create internal thread object and geometry     |
# +-------------------------------------------------------------+
def internal(name, ct3di_prms, doc, body):
    """
    internal(name, ct3di_prms, doc, body) -> obj

    It creates Cosmetic Thread 3D Internal (PartDesign version)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]                 name of the object in the model tree
    ct3di_prms - [ct3di_params_class]     parameters of the cosmetic thread
    doc        - [text link]              document for thread creating
    body       - [PartDesign body object] body object for the thread
    """
    doc.openTransaction('undo000')
    obj = None
    if doc is None:
        App.Console.PrintError("Document has to be set.\n")
    elif not body:
        App.Console.PrintError("Body has to be set.\n")
    elif body.Tip is None:
        App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
    elif ct3di_prms is None:
        App.Console.PrintError('internal_pd(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    else:
        if (name is None) or (name == ''):
            name = ct3di_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        ViewProvider_ct3di(obj.ViewObject, body.ViewObject)
        CosmeticThread3DInternal(obj, ct3di_prms)
        body.addObject(obj) # optionally we can also use body.insertObject()
    doc.commitTransaction()
    return obj

# +---------------------------------------------------------+
# | CosmeticThread3DInternal class.                         |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal:
    """
    CosmeticThread3DInternal class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """
    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal class / internall
        function.
        """
        self.Type = 'CosmeticThread3DInternalPartDesign'
        obj.Proxy = self
        # Add property of internal thread into obj
        ct3d_params.addProperty_internal_thread(obj, ct3di_prms)

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed.
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory.
        """
        ct3dGeo = []
        # helix
        tmp = Part.makeHelix(obj.pitch.Value,
                             obj.length.Value,
                             0.5*obj.D1.Value)
        ct3dGeo.append(tmp)
        # Major diameter at z=0
        tmp = Part.makeCircle(0.5*obj.D.Value)
        ct3dGeo.append(tmp)
        # Major diameter at z = Thread Length
        tmp = Part.makeCircle(0.5*obj.D.Value)
        tmp.Placement.translate(App.Vector(0, 0, obj.length.Value))
        ct3dGeo.append(tmp)
        if not obj.length_through:
            # Minor diameter at z = obj.length
            tmp = Part.makeCircle(0.5*obj.D1.Value)
            tmp.Placement.translate(App.Vector(0, 0, obj.length.Value))
            ct3dGeo.append(tmp)
        # resulting geometry
        rslt = Part.makeCompound(ct3dGeo)

        # Apply attachement to the obj
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()

        rslt.Placement = obj.Placement
        obj.Shape = rslt



# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread External ...                     #
#                                                                  #
# **************************************************************** #

# +---------------------------------------------------------+
# | ViewProvider_ct3de class.                               |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DExternal        |
# +---------------------------------------------------------+
class ViewProvider_ct3de:
    """
    FreeCAD_Gui part of the CosmeticThread3DExternal.
    This class is common for all types and versions of internal threads.
    """

    def __init__(self, obj, body):
        """
        Set this object to the proxy object of the actual view provider.
        """
        obj.Proxy = self
        # obj.DisplayMode = body.DisplayMode
        # obj.DrawStyle = body.DrawStyle
        # obj.LineColor = body.LineColor
        # obj.LineWidth = body.LineWidth
        # obj.PointColor = body.PointColor
        # obj.PointSize = body.PointSize
        # if int(App.Version()[1]) >= 22:
        #     obj.ShapeAppearance = body.ShapeAppearance
        # else:
        #     obj.ShapeColor = body.ShapeColor
        # obj.Transparency = body.Transparency
        obj.DrawStyle = 'Dashed'
        obj.LineColor = (0, 0, 0)
        obj.LineWidth = 1.0
        obj.PointColor = (25, 25, 25)
        obj.PointSize = 1.0
        obj.Transparency = 0

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

    def getDisplayModes(self, obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined
        in getDisplayModes.
        """
        return "Wireframe"

    def setDisplayMode(self, mode):
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

    def loads(self, state):
        """
        Called during document restore.
        """

# +-------------------------------------------------------------+
# | external() - create external thread object and geometry     |
# +-------------------------------------------------------------+
def external(name, ct3de_prms, doc, body):
    """
    external(name, ct3de_prms, doc, body) -> obj

    creates Cosmetic Thread 3D External (Part Design version)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]                 name of the object in the model tree
    ct3de_prms - [ct3de_params_class]     parameters of the cosmetic thread
    doc        - [text link]              document for thread creating
    body       - [PartDesign body object] body object for the thread
    """
    doc.openTransaction('undo000')
    obj = None
    if doc is None:
        App.Console.PrintError("Document has to be set.\n")
    elif not body:
        App.Console.PrintError("Body has to be set.\n")
    elif body.Tip is None:
        App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
    elif ct3de_prms is None:
        App.Console.PrintError('external_pd(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    else:
        obj = None
        if (name is None) or (name == ''):
            name = ct3de_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        ViewProvider_ct3de(obj.ViewObject, body.ViewObject)
        CosmeticThread3DExternal(obj, ct3de_prms)
        body.addObject(obj) # optionally we can also use body.insertObject()
    doc.commitTransaction()
    return obj

# +---------------------------------------------------------+
# | CosmeticThread3DExternal class.                         |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal:
    """
    CosmeticThread3DExternal class

    The geometry and all handlers are defined here.
    Service function for thread creation is external() above.
    """

    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal class / internall
        function.
        """
        self.Type = 'CosmeticThread3DExternalPartDesign'
        obj.Proxy = self
        # Add property of external thread into obj
        ct3d_params.addProperty_external_thread(obj, ct3de_prms)

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed.
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory.
        """
        ct3dGeo = []
        # helix
        tmp = Part.makeHelix(obj.pitch.Value,
                             obj.length.Value,
                             0.5*obj.D.Value)
        ct3dGeo.append(tmp)
        # Minor diameter at z=0
        tmp = Part.makeCircle(0.5*obj.d3.Value)
        ct3dGeo.append(tmp)
        # Minor diameter at z = Thread Length
        tmp = Part.makeCircle(0.5*obj.d3.Value)
        tmp.Placement.translate(App.Vector(0, 0, obj.length.Value))
        ct3dGeo.append(tmp)
        if not obj.length_through:
            # Major diameter at z = obj.length
            tmp = Part.makeCircle(0.5*obj.D.Value)
            tmp.Placement.translate(App.Vector(0, 0, obj.length.Value))
            ct3dGeo.append(tmp)
        # resulting geometry
        rslt = Part.makeCompound(ct3dGeo)

        # Apply attachement to the obj
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()

        rslt.Placement = obj.Placement
        obj.Shape = rslt
