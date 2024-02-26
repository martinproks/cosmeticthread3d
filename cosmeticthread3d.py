# -*- coding: utf-8 -*-
#
# cosmeticthread3d.py
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
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External

"""

import os
import FreeCAD as App
import Part

___title__   = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'



# +--------------------------------------------------------+
# |                                                        |
# | get_module_path() - internal function                  |
# |                                                        |
# +--------------------------------------------------------+
def get_module_path():
    """Returns the current module path."""
    
    return os.path.dirname(__file__)



# **************************************************************** #
# **************************************************************** #
# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread Internal ...                     #
#                                                                  #
# **************************************************************** #
# **************************************************************** #
# **************************************************************** #

# +--------------------------------------------------------+
# |                                                        |
# | ct3di_params_class - internal thread parameters class  |
# |                                                        |
# +--------------------------------------------------------+
# There is a lot of parameters around cosmetic thread internal for exchange
# informations on function calls and returns. I decide to wrap them into a class.
# It will be more easy to handle with one object than many separate
# variables...
class ct3di_params_class:
    def __init__(self):
        self.name           = "M10"    # [string]     Thread designation
        self.D_nominal      = 10.0     # [float - mm] Nominal diameter
        self.pitch          =  1.5     # [float - mm] Pitch - coarse
        self.D              = 10.0     # [float - mm] Major diameter (used for thread show) - tolerance = 0
        self.D1             =  8.376   # [float - mm] Minor diameter - tolerance = 0 (used for helix and thread stop)
        self.D_drill        =  8.5     # [float - mm] Recommended pre-driled hole diameter
        self.tolerance      = "6H"     # [string]     Hole thread tolerance (empty string allowed)
        self.roughness      = "Ra 1.6" # [string]     Hole thread roughness (empty string allowed)
        self.length         = 18.0     # [float - mm] Thread length
        self.length_through = False    # [Bool]       Default value No. If Yes, thread does not have end shell.
        self.length_tol     = "H17"    # [string]     Length tolerance (empty string allowed). For example "H17" or "0/+1.8" or ""
        #
        return None


# +---------------------------------------------------------+
# |                                                         |
# | internal_p0() - create internal thread object and geometry |
# |                                                         |
# +---------------------------------------------------------+
def internal_p0(name='CosmeticThread3DInternal', ct3di_params=None, aPart=None):
    """
    internal_p0(name, ct3di_params, aPart) -> obj

    It creates Cosmetic Thread 3D Internal (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3di_params - [ct3di_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None

    if ct3di_params == None:
        App.Console.PrintError('internal(name, ct3di_params) - Check ctide_params\n')
    else:
        if name == None:
            name = ct3di_params.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart != None:
            aPart.addObject(obj)
        CosmeticThread3DInternal_p0(obj, ct3di_params)
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
    """CosmeticThread3DInternal_p0 class

    The geometry and all handlers are defined here.
    Service function for thread creation is internal() above.
    """
    
    def __init__(self, obj, ct3di_params):
        """
        __init__(obj, ct3di_params)
        
        constructor of a CosmeticThread3DInternal class / internall function
        """
        #
        self.Type = 'CosmeticThread3DInternal_p0'
        obj.Proxy = self
        # Description - Read and Write
        obj.addProperty('App::PropertyString', 'Description', 'Base', \
                        'Thread designation.', 0).Description \
                        = ct3di_params.name
        # D nominal - Read and Write
        obj.addProperty('App::PropertyLength', 'D_nominal', 'ct3di_data', \
                        'Nominal diameter.', 0).D_nominal \
                        = ct3di_params.D_nominal
        # Pitch - Read and Write
        obj.addProperty('App::PropertyLength', 'pitch', 'ct3di_data', \
                        'Thread pitch.', 0).pitch \
                        = ct3di_params.pitch
        # Major diameter - Read and Write
        obj.addProperty('App::PropertyLength', 'D', 'ct3di_data', \
                        'Thread major diameter.', 0).D \
                        = ct3di_params.D
        # Minor diameter - Read and Write
        obj.addProperty('App::PropertyLength', 'D1', 'ct3di_data', \
                        'Thread minor diameter.', 0).D1 \
                        = ct3di_params.D1
        # Pre drilled recomendation - Read and Write
        obj.addProperty('App::PropertyLength', 'D_drill', 'ct3di_data', \
                        'Recommended pre-driled hole diameter.', 0).D_drill \
                        = ct3di_params.D_drill
        # Thread tolerance - Read and Write
        obj.addProperty('App::PropertyString', 'tolerance', 'ct3di_data', \
                        'Hole thread tolerance. For example "6H" or just nothing.', 0).tolerance \
                        = ct3di_params.tolerance
        # Roughness - Read and Write
        obj.addProperty('App::PropertyString', 'roughness', 'ct3di_data', \
                        'Hole thread roughness. For example "Ra 1.6" or "Rz 2" or just nothing.', 0).roughness \
                        = ct3di_params.roughness
        # Length of thread - Read and Write
        obj.addProperty('App::PropertyLength', 'length', 'ct3di_data', \
                        'Thread length.', 0).length \
                        = ct3di_params.length
        # Is the thread throught? - Read and Write
        obj.addProperty('App::PropertyBool', 'length_through', 'ct3di_data', \
                        'Thread is through whole body?', 0).length_through \
                        = ct3di_params.length_through
        # Length tolerance - Read and Write
        obj.addProperty('App::PropertyString', 'length_tol', 'ct3di_data', \
                        'Length tolerance. For example "H17" or "0/+1.8" or just nothing.', 0).length_tol \
                        = ct3di_params.length_tol 
        # Attachement extension
        self.makeAttachable(obj)
        #
        return None

    def makeAttachable(self, obj):
        if int(App.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)
        obj.setEditorMode('Placement', 0) #non-readonly non-hidden
        return None

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")
        return None

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """
        # Helix of the thread
        # *******************
        # Well, I'm fighting with the helix. There is no problem to create
        # an helix according parameters, but the helix is not a shape.
        # It is a Wire and I do not how (if any) to connect it with shapes.
        # I'm trying an uggly hack - make shape by rotating the helix wire
        # for a few degree and add this shape to the rest shapes.
        #
        h = Part.makeHelix(obj.pitch, obj.length, 0.5*obj.D1)

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.D, 0, 0)
        v1 = App.Vector(0.5*obj.D, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0, e0.FirstParameter, e0.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
        if obj.length_through == True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D1, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, e1.FirstParameter, e1.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
            r  = Part.makeCompound([h, r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r
        #
        return None



# +---------------------------------------------------------+
# |                                                         |
# | ViewProviderCosmeticThread3DInternal class.             |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DInternal        |
# |                                                         |
# +---------------------------------------------------------+
class ViewProviderCosmeticThread3DInternal:
    """FreeCAD_Gui part of the CosmeticThread3DInternal"""

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """
        obj.Proxy = self
        return None

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return None

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return None

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")
        return None

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
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
        return None

    def loads(self,state):
        """
        Called during document restore.
        """
        return None



# **************************************************************** #
# **************************************************************** #
# **************************************************************** #
#                                                                  #
#                 Cosmetic Thread External ...                     #
#                                                                  #
# **************************************************************** #
# **************************************************************** #
# **************************************************************** #

# +--------------------------------------------------------+
# |                                                        |
# | ct3de_params_class - external thread parameters class  |
# |                                                        |
# +--------------------------------------------------------+
# There is a lot of parameters around cosmetic thread external for exchange
# informations on function calls and returns. I decide to wrap them into a class.
# It will be more easy to handle with one object than many separate
# variables...
class ct3de_params_class:
    def __init__(self):
        self.name           = "M10"    # [string]     Thread designation
        self.D_nominal      = 10.0     # [float - mm] Nominal diameter
        self.pitch          =  1.5     # [float - mm] Pitch - coarse
        self.D              = 10.0     # [float - mm] Big diameter (used for helix and thread stop) - tolerance = 0
        self.d3             =  8.160   # [float - mm] Small diameter - tolerance = 0 (used for thread shell)
        self.tolerance      = "6g"     # [string]     Hole thread tolerance (empty string allowed)
        self.roughness      = "Ra 1.6" # [string]     Hole thread roughness (empty string allowed)
        self.length         = 18.0     # [float - mm] Thread length
        self.length_through = False    # [Bool]       Default value No. If Yes, thread does not have end shell.
        self.length_tol     = "H17"    # [string]     Length tolerance (empty string allowed). For example "H17" or "0/+1.8" or ""
        #
        return None



# +---------------------------------------------------------+
# |                                                         |
# | external() - create external thread object and geometry |
# |                                                         |
# +---------------------------------------------------------+
def external_p0(name='CosmeticThread3DExternal', ct3de_params=None, aPart=None):
    """
    external(name, ct3de_params) -> obj

    creates Cosmetic Thread 3D External (Part version, type 0)
    and returns obj.

    This function is mentioned to be used for object creation.

    name         - [string]             name of the object in the model tree
    ct3de_params - [ct3de_params_class] parameters of the cosmetic thread
    aPart        - [text link]          active Part object
    """

    obj = None
    
    if ct3de_params == None:
        App.Console.PrintError('internal(name, ct3de_params) - Check ct3de_params\n')
    else:
        if name == None:
            name = ct3de_params.name
        obj = App.ActiveDocument.addObject('Part::FeaturePython', name)
        if aPart != None:
            aPart.addObject(obj)
        CosmeticThread3DExternal_p0(obj, ct3de_params)
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
    def __init__(self, obj, ct3de_params):
        """
        __init__(obj, ct3de_params)
        
        constructor of a CosmeticThread3DExternal class / internall function
        """
        
        self.Type = 'CosmeticThread3DExternal_p0'
        obj.Proxy = self
        # Description - Read and Write
        obj.addProperty('App::PropertyString', 'Description', 'Base', \
                        'Thread designation.', 0).Description \
                        = ct3de_params.name
        # D nominal - Read and Write
        obj.addProperty('App::PropertyLength', 'D_nominal', 'ct3de_data', \
                        'Nominal diameter.', 0).D_nominal \
                        = ct3de_params.D_nominal
        # Pitch - Read and Write
        obj.addProperty('App::PropertyLength', 'pitch', 'ct3de_data', \
                        'Thread pitch.', 0).pitch \
                        = ct3de_params.pitch
        # Major diameter - Read and Write
        obj.addProperty('App::PropertyLength', 'D', 'ct3de_data', \
                        'Thread major diameter.', 0).D \
                        = ct3de_params.D
        # Minor diameter - Read and Write
        obj.addProperty('App::PropertyLength', 'd3', 'ct3de_data', \
                        'Thread minor diameter.', 0).d3 \
                        = ct3de_params.d3
        # Thread tolerance - Read and Write
        obj.addProperty('App::PropertyString', 'tolerance', 'ct3de_data', \
                        'Extenal thread tolerance. For example "6g" or just nothing.', 0).tolerance \
                        = ct3de_params.tolerance
        # Roughness - Read and Write
        obj.addProperty('App::PropertyString', 'roughness', 'ct3de_data', \
                        'External thread roughness. For example "Ra 1.6" or "Rz 2" or just nothing.', 0).roughness \
                        = ct3de_params.roughness
        # Length of thread - Read and Write
        obj.addProperty('App::PropertyLength', 'length', 'ct3de_data', \
                        'Thread length.', 0).length \
                        = ct3de_params.length
        # Is the thread throught? - Read and Write
        obj.addProperty('App::PropertyBool', 'length_through', 'ct3de_data', \
                        'Thread is through whole body?', 0).length_through \
                        = ct3de_params.length_through
        # Length tolerance - Read and Write
        obj.addProperty('App::PropertyString', 'length_tol', 'ct3de_data', \
                        'Length tolerance. For example "H17" or "0/+1.8" or just nothing.', 0).length_tol \
                        = ct3de_params.length_tol 
        # Attachement extension
        self.makeAttachable(obj)
        #
        return None
        
    def makeAttachable(self, obj):
        if int(App.Version()[1]) >= 19:
            obj.addExtension('Part::AttachExtensionPython')
        else:
            obj.addExtension('Part::AttachExtensionPython', obj)
        obj.setEditorMode('Placement', 0) #non-readonly non-hidden
        #
        return None

    def onChanged(self, obj, prop):
        """
        Do something when a property has changed
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")
        return None

    def execute(self, obj):
        """
        Do something when doing a recomputation, this method is mandatory
        """
        # Helix of the thread
        # *******************
        # Well, I'm fighting with the helix. There is no problem to create
        # an helix according parameters, but the helix is not a shape.
        # It is a Wire and I do not how (if any) to connect it with shapes.
        # I'm trying an uggly hack - make shape by rotating the helix wire
        # for a few degree and add this shape to the rest shapes.
        #
        h = Part.makeHelix(obj.pitch, obj.length, 0.5*obj.D)

        # Add shape of the thread
        # ***********************
        v0 = App.Vector(0.5*obj.d3, 0, 0)
        v1 = App.Vector(0.5*obj.d3, 0, obj.length)
        e0 = Part.makeLine(v0, v1)
        r0 = Part.makeRevolution(e0, e0.FirstParameter, e0.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
        if obj.length_through == True:
            # Thread is going throught whole body - there is no ending anulus
            r = Part.makeCompound([h, r0])
        else:
            # Ending annulus...
            v2 = App.Vector(0.5*obj.D, 0, obj.length)
            e1 = Part.makeLine(v1, v2)
            r1 = Part.makeRevolution(e1, e1.FirstParameter, e1.LastParameter, 360.0, App.Vector(0,0,0), App.Vector(0,0,1), Part.Face)
            r  = Part.makeCompound([h, r0, r1])

        # Apply attachement to the r
        if not hasattr(obj, "positionBySupport"):
            self.makeAttachable(obj)
        obj.positionBySupport()
        r.Placement = obj.Placement

        # And assotiate it to the 'obj'
        # *****************************
        obj.Shape = r
        #
        return None



# +---------------------------------------------------------+
# |                                                         |
# | ViewProviderCosmeticThread3DExternal class.             |
# |                                                         |
# | FreeCAD_Gui part of the CosmeticThread3DExternal        |
# |                                                         |
# +---------------------------------------------------------+
class ViewProviderCosmeticThread3DExternal:
    """FreeCAD_Gui part of the CosmeticThread3DExternal"""

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """
        obj.Proxy = self
        return None

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return None

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return None

    def getDisplayModes(self,obj):
        """
        Return a list of display modes.
        """
        return []

    def getDefaultDisplayMode(self):
        """
        Return the name of the default display mode. It must be defined in getDisplayModes.
        """
        return "Shaded"

    def setDisplayMode(self,mode):
        """
        Map the display mode defined in attach with those defined in getDisplayModes.
        Since they have the same names nothing needs to be done.
        This method is optional.
        """
        return mode

    def onChanged(self, vp, prop):
        """
        Print the name of the property that has changed
        """
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")
        return None

    def getIcon(self):
        """
        Return the icon in XMP format which will appear in the tree view. This method is optional and if not defined a default icon is shown.
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
        return None

    def loads(self,state):
        """
        Called during document restore.
        """
        return None

