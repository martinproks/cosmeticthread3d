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
        return "Shaded"

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
# | internal_p0() - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p0(name='CosmeticThread3DInternal', \
                ct3di_prms=None, \
                aPart=None):
    """
    internal_p0(name, ct3di_prms, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name       - [string]               name of the object in the model tree
    ct3di_prms - [ct3di_params_class]   parameters of the cosmetic thread
    aPart      - [text link]            active Part object
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p0(name, ct3di_prms, aPart) - Check ct3di_prms\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DInternal_p0(obj, ct3di_prms)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, \
                                     e1.FirstParameter, \
                                     e1.LastParameter, \
                                     360.0, \
                                     App.Vector(0, 0, 0), \
                                     App.Vector(0, 0, 1), \
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
def internal_p1(name='CosmeticThread3DInternal', \
                ct3di_prms=None, \
                aPart=None):
    """
    internal_p1(name, ct3di_prms, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 1)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]              name of the object in the model tree
    ct3di_prms   - [ct3di_params_class]  parameters of the cosmetic thread
    aPart        - [text link]           active Part object
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p1(name, ct3di_prms, aPart) - Check ct3di_prms\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DInternal_p1(obj, ct3di_prms)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, \
                                     e1.FirstParameter, \
                                     e1.LastParameter, \
                                     360.0, \
                                     App.Vector(0, 0, 0), \
                                     App.Vector(0, 0, 1), \
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
def internal_p2(name='CosmeticThread3DInternal', \
                ct3di_prms=None, \
                aPart=None):
    """
    internal_p2(name, ct3di_prms, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 2)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3di_prms   - [ct3di_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p2(name, ct3di_prms, aPart) - Check ct3di_prms\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DInternal_p2(obj, ct3di_prms)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Solid)
        r1 = Part.makeRevolution(e1, \
                                 e1.FirstParameter, \
                                 e1.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
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
# | internal_p4) - create internal thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def internal_p4(name='CosmeticThread3DInternal', \
                ct3di_prms=None, \
                aPart=None):
    """
    internal_p4(name, ct3di_prms, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 4)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3di_prms   - [ct3di_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3di_prms is None:
        App.Console.PrintError('internal_p4(name, ct3di_prms, aPart) - Check ct3di_prms\n')
    else:
        if name is None:
            name = ct3di_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DInternal_p4(obj, ct3di_prms)
        ViewProviderCosmeticThread3DInternal(obj.ViewObject)
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

        constructor of a CosmeticThread3DInternal_p2 class,
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
        r = Part.makeRevolution(e0, \
                                e0.FirstParameter, \
                                e0.LastParameter, \
                                360.0, \
                                App.Vector(0, 0, 0), \
                                App.Vector(0, 0, 1), \
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
        tex.filename = os.path.join(os.path.dirname(__file__), \
                                    'CosmeticThread3D.png')
        obj.ViewObject.Transparency = 0
        obj.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
        obj.ViewObject.RootNode.insertChild(tex, 1)



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
        return "Shaded"

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



# +------------------------------------------------------------+
# |                                                            |
# | external_p0() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p0(name='CosmeticThread3DExternal', \
                ct3de_prms=None, \
                aPart=None):
    """
    external_p0(name, ct3de_prms) -> obj

    creates Cosmetic Thread 3D External (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3de_prms   - [ct3de_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p0(name, ct3de_prms, aPart) - Check ct3de_prms\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DExternal_p0(obj, ct3de_prms)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, \
                                     e1.FirstParameter, \
                                     e1.LastParameter, \
                                     360.0, \
                                     App.Vector(0, 0, 0), \
                                     App.Vector(0, 0, 1), \
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
def external_p1(name='CosmeticThread3DExternal', \
                ct3de_prms=None, \
                aPart=None):
    """
    external_p1(name, ct3de_prms) -> obj

    creates Cosmetic Thread 3D External (Part version, type 1)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3de_prms   - [ct3de_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p1(name, ct3de_prms, aPart) - Check ct3de_prms\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DExternal_p1(obj, ct3de_prms)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Face)
        if obj.length_through is True:
            # Thread is going throught whole body, there is no ending anulus
            r = Part.makeCompound([r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, \
                                     e1.FirstParameter, \
                                     e1.LastParameter, \
                                     360.0, \
                                     App.Vector(0, 0, 0), \
                                     App.Vector(0, 0, 1), \
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
def external_p2(name='CosmeticThread3DExternal', \
                ct3de_prms=None, \
                aPart=None):
    """
    external_p2(name, ct3de_prms) -> obj

    creates Cosmetic Thread 3D External (Part version, type 2)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3de_prms   - [ct3de_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p2(name, ct3de_prms, aPart) - Check ct3de_prms\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DExternal_p2(obj, ct3de_prms)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
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
        r0 = Part.makeRevolution(e0, \
                                 e0.FirstParameter, \
                                 e0.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
                                 Part.Solid)
        r1 = Part.makeRevolution(e1, \
                                 e1.FirstParameter, \
                                 e1.LastParameter, \
                                 360.0, \
                                 App.Vector(0, 0, 0), \
                                 App.Vector(0, 0, 1), \
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
# | external_p4() - create external thread object and geometry |
# |                                                            |
# +------------------------------------------------------------+
def external_p4(name='CosmeticThread3DExternal', \
                ct3de_prms=None, \
                aPart=None):
    """
    external_p4(name, ct3de_prms) -> obj

    creates Cosmetic Thread 3D External (Part version, type 4)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3de_prms   - [ct3de_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3de_prms is None:
        App.Console.PrintError('external_p2(name, ct3de_prms, aPart) - Check ct3de_prms\n')
    else:
        if name is None:
            name = ct3de_prms.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart is not None:
            aPart.addObject(obj)
        CosmeticThread3DExternal_p4(obj, ct3de_prms)
        ViewProviderCosmeticThread3DExternal(obj.ViewObject)
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
        r = Part.makeRevolution(e0, \
                                e0.FirstParameter, \
                                e0.LastParameter, \
                                360.0, \
                                App.Vector(0, 0, 0), \
                                App.Vector(0, 0, 1), \
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
        tex.filename = os.path.join(os.path.dirname(__file__), \
                                    'CosmeticThread3D.png')
        obj.ViewObject.Transparency = 0
        obj.ViewObject.ShapeColor = (1.0, 1.0, 1.0)
        obj.ViewObject.RootNode.insertChild(tex, 1)
