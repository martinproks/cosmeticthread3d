# -*- coding: utf-8 -*-
#
# cosmeticthread3d_part.py
#
#*****************************************************************************
#* Cosmetic Thread 3D Work Bench - tools for cosmetic threads creation       *
#* Copyright (C) 2024 Martin Prokš / martin(dot)proks(at)proks-martin(dot)cz *
#*                                                                           *
#* This file is part of the FreeCAD CAx development system.                  *
#*                                                                           *
#* This library is free software; you can redistribute it and/or             *
#* modify it under the terms of the GNU Lesser General Public                *
#* License as published by the Free Software Foundation; either              *
#* version 2.1 of the License, or (at your option) any later version.        *
#*                                                                           *
#* This library is distributed in the hope that it will be useful,           *
#* but WITHOUT ANY WARRANTY; without even the implied warranty of            *
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU         *
#* Lesser General Public License for more details.                           *
#*                                                                           *
#* You should have received a copy of the GNU Lesser General Public          *
#* License along with this library; if not, write to the Free Software       *
#* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 *
#* USA                                                                       *
#*****************************************************************************
"""
Definition of PythonFeature for each Part version of thread geometry type.
"""

import os # needed just for _p4 threads
from pivy import coin # needed just for _p4 threads
import FreeCAD as App
import Part
import ct3d_params

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
    """FreeCAD_Gui part of the CosmeticThread3DInternal.
    This class is common for all types and versions of internal threads.
    """

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider.
        """
        obj.Proxy = self
        obj.DrawStyle = 'Dashed'
        obj.LineColor = (0, 0, 0)
        obj.LineWidth = 1.0
        obj.PointColor = (25, 25, 25)
        obj.PointSize = 1.0
        obj.Transparency = 80

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method
        is mandatory.
        """

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance
        to handle this here.
        """

    def getDisplayModes(self, obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in
        getDisplayModes.
        """
        return "Wireframe"

    def setDisplayMode(self, mode):
        """
        Map the display mode defined in attach with those defined in
        getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """

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



# +------------------------------------------------------------+
# |                                                            |
# | internal() - create internal thread object and geometry    |
# |                                                            |
# +------------------------------------------------------------+
def internal(name, ct3di_prms, doc, aPart):
    """
    internal(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """
    obj = None
    if ct3di_prms is None:
        App.Console.PrintError('internal(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal(obj, ct3di_prms)
        App.ActiveDocument.recompute()
    return obj



# +------------------------------------------------------+
# |                                                      |
# | CosmeticThread3DInternal class.                      |
# |                                                      |
# | The geometry and all handlers are defined here.      |
# |                                                      |
# +------------------------------------------------------+
class CosmeticThread3DInternal:
    """
    CosmeticThread3DInternal class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p0 class,
        internall function.
        """
        #
        self.Type = 'CosmeticThread3DInternalPart'
        obj.Proxy = self
        # Add property of internal thread into obj
        ct3d_params.addProperty_internal_thread(obj, ct3di_prms)
        ##### # Attachement extension
        ##### self.makeAttachable(obj)
        ##### 
        # def makeAttachable(self, obj):
        ##### if int(App.Version()[1]) >= 19:
        #####     obj.addExtension('Part::AttachExtensionPython')
        ##### else:
        #####     obj.addExtension('Part::AttachExtensionPython', obj)
        ##### obj.setEditorMode('Placement', 0) # non-readonly non-hidden

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
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
        #
        # Apply attachement to the obj
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()

        rslt.Placement = obj.Placement
        obj.Shape = rslt



# +------------------------------------------------------------+
# |                                                            |
# | internal_p0() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p0(name, ct3di_prms, doc, aPart):
    """
    internal_p0(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p0(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p0(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal_p0(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p0 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p0:
    """
    CosmeticThread3DInternal_p0 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p0 class,
        internall function.
        """
        #
        self.Type = 'CosmeticThread3DInternal_p0'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """
        # Helix of the thread
        # *******************
        h = Part.makeHelix(obj.pitch, obj.length, 0.5*obj.D1)

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending annulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1,
                                     e1.FirstParameter,
                                     e1.LastParameter,
                                     360.0,
                                     App.Vector(0, 0, 0),
                                     App.Vector(0, 0, 1),
                                     Part.Face)
            r = Part.makeCompound([h, r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | internal_p1() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p1(name, ct3di_prms, doc, aPart):
    """
    internal_p1(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 1)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p1(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p1(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal_p1(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p1 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p1:
    """
    CosmeticThread3DInternal_p1 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p1 class,
        internall function
        """
        #
        self.Type = 'CosmeticThread3DInternal_p1'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending annulus
            r = Part.makeCompound([r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1,
                                     e1.FirstParameter,
                                     e1.LastParameter,
                                     360.0,
                                     App.Vector(0, 0, 0),
                                     App.Vector(0, 0, 1),
                                     Part.Face)
            r = Part.makeCompound([r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | internal_p2() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p2(name, ct3di_prms, doc, aPart):
    """
    internal_p2(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 2)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p2(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p2(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal_p2(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p2 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p2:
    """
    CosmeticThread3DInternal_p2 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p2 class,
        internall function
        """
        #
        self.Type = 'CosmeticThread3DInternal_p2'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        v2 = App.Vector(0.5*obj.D1, 0, 0)
        v3 = App.Vector(0.5*obj.D1, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        e1 = Part.makeLine(v2, v3)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Solid)
        r1 = Part.makeRevolution(e1,
                                 e1.FirstParameter,
                                 e1.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Solid)
        r = r0.cut(r1)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | internal_p3() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p3(name, ct3di_prms, doc, aPart):
    """
    internal_p3(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 3)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p3(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p3(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal_p3(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p3 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p3:
    """
    CosmeticThread3DInternal_p3 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p3 class,
        internall function.
        """
        #
        self.Type = 'CosmeticThread3DInternal_p3'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """
        # Outside shell - D
        ri = []
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        ri.append(Part.makeRevolution(e0,
                                      e0.FirstParameter,
                                      e0.LastParameter,
                                      360.0,
                                      App.Vector(0, 0, 0),
                                      App.Vector(0, 0, 1),
                                      Part.Face))

        # Zig-Zag shell between D1 and D
        [n_rings, mod_rings] = divmod(obj.length.Value, obj.pitch.Value)
        if n_rings < 1.0:
            n_rings = 1.0
        d_z = 0.5 * obj.length.Value / n_rings
        n_v = int(n_rings * 2 + 1)
        for i in range(n_v):
            x = 0.5*obj.D1 if i % 2 else 0.5*obj.D
            y = 0
            z = i*d_z
            if i == 0:
                vi1 = App.Vector(x, y, z)
            else:
                vi = vi1
                vi1 = App.Vector(x, y, z)
                ei = Part.makeLine(vi, vi1)
                ri.append(Part.makeRevolution(ei,
                                              ei.FirstParameter,
                                              ei.LastParameter,
                                              360.0,
                                              App.Vector(0, 0, 0),
                                              App.Vector(0, 0, 1),
                                              Part.Face))

        # Ending anulus and compound object:
        if obj.length_through is not True:
            # Append ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            ri.append(Part.makeRevolution(e1,
                                          e1.FirstParameter,
                                          e1.LastParameter,
                                          360.0,
                                          App.Vector(0, 0, 0),
                                          App.Vector(0, 0, 1),
                                          Part.Face))
        r = Part.makeCompound(ri)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | internal_p4() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p4(name, ct3di_prms, doc, aPart):
    """
    internal_p4(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 4)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p4(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p4(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        # change displaymode to Shaded - this is texture based thread
        obj.ViewObject.DisplayMode = "Shaded"
        CosmeticThread3DInternal_p4(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p4 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p4:
    """
    CosmeticThread3DInternal_p4 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p4 class,
        internall function
        """
        #
        self.Type = 'CosmeticThread3DInternal_p4'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D1, 0, 0)
        v1 = App.Vector(0.5*obj.D1, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r = Part.makeRevolution(e0,
                                e0.FirstParameter,
                                e0.LastParameter,
                                360.0,
                                App.Vector(0, 0, 0),
                                App.Vector(0, 0, 1),
                                Part.Face)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r

        # Load and apply texture
        # **********************
        tex = coin.SoTexture2()
        tex.filename = os.path.join(os.path.dirname(__file__),
                                    'CosmeticThread3D.png')
        obj.ViewObject.Transparency = 0
        obj.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
        obj.ViewObject.RootNode.insertChild(tex, 1)



# +------------------------------------------------------------+
# |                                                            |
# | internal_p5() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p5(name, ct3di_prms, doc, aPart):
    """
    internal_p5(name, ct3di_prms, doc, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 5)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3di_prms - [ct3di_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p5(name, ct3di_prms, doc, aPart) - Check ct3di_prms\n')
    elif doc is None:
        App.Console.PrintError('internal_p5(name, ct3di_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
        CosmeticThread3DInternal_p5(obj, ct3di_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DInternal_p5 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DInternal_p5:
    """
    CosmeticThread3DInternal_p5 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """

    def __init__(self, obj, ct3di_prms):
        """
        __init__(obj, ct3di_prms)

        constructor of a CosmeticThread3DInternal_p5 class,
        internall function
        """
        #
        self.Type = 'CosmeticThread3DInternal_p5'
        obj.Proxy = self
        # Add property of internal thread into obj
        ct3d_params.addProperty_internal_thread(obj, ct3di_prms)

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
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
        #
        # Apply attachement to the obj
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()

        rslt.Placement = obj.Placement
        obj.Shape = rslt



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
        Set this object to the proxy object of the actual view provider
        """
        obj.Proxy = self
        obj.DrawStyle = 'Dashed'
        obj.LineColor = (0, 0, 0)
        obj.LineWidth = 1.0
        obj.PointColor = (25, 25, 25)
        obj.PointSize = 1.0
        obj.Transparency = 80

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is
        mandatory
        """

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance
        to handle this here
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
        in getDisplayModes. Since they have the same names nothing needs
        to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """

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



# +---------------------------------------------------------+
# |                                                         |
# | external() - create external thread object and geometry |
# |                                                         |
# +---------------------------------------------------------+
def external(name, ct3de_prms, doc, aPart):
    """
    external(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None

    """
    obj = None
    if ct3de_prms is None:
        App.Console.PrintError('external(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p0(obj, ct3de_prms)
        App.ActiveDocument.recompute()
    return obj



# +------------------------------------------------------+
# |                                                      |
# | CosmeticThread3DExternal class.                      |
# |                                                      |
# | The geometry and all handlers are defined here.      |
# |                                                      |
# +------------------------------------------------------+
class CosmeticThread3DExternal:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternalPart'
        obj.Proxy = self
        ct3d_params.addProperty_external_thread(obj, ct3de_prms)
        ##### # Attachement extension
        ##### self.makeAttachable(obj)
        ##### 
        # def makeAttachable(self, obj):
        ##### if int(App.Version()[1]) >= 19:
        #####     obj.addExtension('Part::AttachExtensionPython')
        ##### else:
        #####     obj.addExtension('Part::AttachExtensionPython', obj)
        ##### obj.setEditorMode('Placement', 0) #non-readonly non-hidden

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
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



# +------------------------------------------------------------+
# |                                                            |
# | external_p0() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p0(name, ct3de_prms, doc, aPart):
    """
    external_p0(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None

    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p0(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p0(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p0(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p0 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p0:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p0 class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternal_p0'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """
        # Helix of the thread
        # *******************
        h = Part.makeHelix(obj.pitch, obj.length, 0.5*obj.D)

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.d3, 0, 0)
        v1 = App.Vector(0.5*obj.d3, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1,
                                     e1.FirstParameter,
                                     e1.LastParameter,
                                     360.0,
                                     App.Vector(0, 0, 0),
                                     App.Vector(0, 0, 1),
                                     Part.Face)
            r = Part.makeCompound([h, r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | external_p1() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p1(name, ct3de_prms, doc, aPart):
    """
    external_p1(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 1)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p1(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p1(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p1(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p1 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p1:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p1 class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternal_p1'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.d3, 0, 0)
        v1 = App.Vector(0.5*obj.d3, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body, there is no ending anulus
            r = Part.makeCompound([r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1,
                                     e1.FirstParameter,
                                     e1.LastParameter,
                                     360.0,
                                     App.Vector(0, 0, 0),
                                     App.Vector(0, 0, 1),
                                     Part.Face)
            r = Part.makeCompound([r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | external_p2() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p2(name, ct3de_prms, doc, aPart):
    """
    external_p2(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 2)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p2(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p2(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p2(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p2 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p2:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p2 class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternal_p2'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        v2 = App.Vector(0.5*obj.d3, 0, 0)
        v3 = App.Vector(0.5*obj.d3, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        e1 = Part.makeLine(v2, v3)
        r0 = Part.makeRevolution(e0,
                                 e0.FirstParameter,
                                 e0.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Solid)
        r1 = Part.makeRevolution(e1,
                                 e1.FirstParameter,
                                 e1.LastParameter,
                                 360.0,
                                 App.Vector(0, 0, 0),
                                 App.Vector(0, 0, 1),
                                 Part.Solid)
        r = r0.cut(r1)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | external_p3() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p3(name, ct3de_prms, doc, aPart):
    """
    external_p3(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 3)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p3(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p3(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p3(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p3 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p3:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p3 class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternal_p3'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        ri = []
        v0 = App.Vector(0.5*obj.d3, 0, 0)
        v1 = App.Vector(0.5*obj.d3, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        ri.append(Part.makeRevolution(e0,
                                      e0.FirstParameter,
                                      e0.LastParameter,
                                      360.0,
                                      App.Vector(0, 0, 0),
                                      App.Vector(0, 0, 1),
                                      Part.Face))

        # Zig-Zag shell between d3 and D
        [n_rings, mod_rings] = divmod(obj.length.Value, obj.pitch.Value)
        if n_rings < 1.0:
            n_rings = 1.0
        d_z = 0.5 * obj.length.Value / n_rings
        n_v = int(n_rings * 2 + 1)
        for i in range(n_v):
            x = 0.5*obj.D if i % 2 else 0.5*obj.d3
            y = 0
            z = i*d_z
            if i == 0:
                vi1 = App.Vector(x, y, z)
            else:
                vi = vi1
                vi1 = App.Vector(x, y, z)
                ei = Part.makeLine(vi, vi1)
                ri.append(Part.makeRevolution(ei,
                                              ei.FirstParameter,
                                              ei.LastParameter,
                                              360.0,
                                              App.Vector(0, 0, 0),
                                              App.Vector(0, 0, 1),
                                              Part.Face))

        if obj.length_through is not True:
            # Append ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            ri.append(Part.makeRevolution(e1,
                                          e1.FirstParameter,
                                          e1.LastParameter,
                                          360.0,
                                          App.Vector(0, 0, 0),
                                          App.Vector(0, 0, 1),
                                          Part.Face))
            r = Part.makeCompound(ri)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r



# +------------------------------------------------------------+
# |                                                            |
# | external_p4() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p4(name, ct3de_prms, doc, aPart):
    """
    external_p4(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 4)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p4(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p4(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        # change displaymode to Shaded - this is texture based thread
        obj.ViewObject.DisplayMode = "Shaded"
        CosmeticThread3DExternal_p4(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p4 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p4:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p4 class,
        internall function
        """

        self.Type = 'CosmeticThread3DExternal_p4'
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
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r = Part.makeRevolution(e0,
                                e0.FirstParameter,
                                e0.LastParameter,
                                360.0,
                                App.Vector(0, 0, 0),
                                App.Vector(0, 0, 1),
                                Part.Face)

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r

        # Load and apply texture
        # **********************
        tex = coin.SoTexture2()
        tex.filename = os.path.join(os.path.dirname(__file__),
                                    'CosmeticThread3D.png')
        obj.ViewObject.Transparency = 0
        obj.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
        obj.ViewObject.RootNode.insertChild(tex, 1)



# +------------------------------------------------------------+
# |                                                            |
# | external_p5() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p5(name, ct3de_prms, doc, aPart):
    """
    external_p5(name, ct3de_prms, doc, aPart) -> obj

    creates Cosmetic Thread 3D External (Part version, type 5)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]             name of the object in the model tree
    ct3de_prms - [ct3de_params_class] parameters of the cosmetic thread
    doc        - [text link]          document for thread creating
    aPart      - [text link]          Part object for thread creating or None
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p5(name, ct3de_prms, doc, aPart) - Check ct3de_prms\n')
    elif doc is None:
        App.Console.PrintError('external_p5(name, ct3de_prms, doc, aPart) - doc has to be some FreeCAD document!\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = doc.addObject('Part::Part2DObjectPython', name)
        if aPart is not None:
            aPart.addObject(obj)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
        CosmeticThread3DExternal_p5(obj, ct3de_prms)
        App.ActiveDocument.recompute()

    return obj



# +---------------------------------------------------------+
# |                                                         |
# | CosmeticThread3DExternal_p5 class.                      |
# |                                                         |
# | The geometry and all handlers are defined here.         |
# |                                                         |
# +---------------------------------------------------------+
class CosmeticThread3DExternal_p5:
    def __init__(self, obj, ct3de_prms):
        """
        __init__(obj, ct3de_prms)

        constructor of a CosmeticThread3DExternal_p5 class,
        internall function
        """
        self.Type = 'CosmeticThread3DExternal_p5'
        obj.Proxy = self
        ct3d_params.addProperty_external_thread(obj, ct3de_prms)

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
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
