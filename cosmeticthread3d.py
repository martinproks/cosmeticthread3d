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

# Just hint how to manually reload and test it in python console...
# import cosmeticthread3d
# from importlib import reload
# reload(cosmeticthread3d)
# a = cosmeticthread3d.internal('', '')

import os
import FreeCAD as App
import Part

___title__   = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL 2.1'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'



def get_module_path():
    """Returns the current module path."""
    return os.path.dirname(__file__)



# ****************************************************************
# ****************************************************************
#
# Cosmetic Thread Internal ...
#
# ****************************************************************
# ****************************************************************

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
        self.length_trought = False    # [Bool]       Default value No. If Yes, thread does not have end shell.
        self.length_tol     = "H17"    # [string]     Length tolerance (empty string allowed). For example "H17" or "0/+1.8" or ""
        # metric_thread_params.attachement ???????       # Attachement to hole starting point and direction....


def internal(obj, obj_name=''):
    """
    obj = internal(name, ct3di_params) -> obj

    creates Cosmetic Thread 3D Internal and returns obj

    name         - [string]             name of the object in the model tree
    ct3di_params - [ct3di_params_class] parameters of the cosmetic thread
    """

    # First, define parameters for the thread... It should came from GUI, but now for starting
    # of the developement I put something constant here temporary.
    ct3di_params = ct3di_params_class()

    if obj_name == '':
        obj_name = ct3di_params.name

    obj = App.ActiveDocument.addObject('Part::FeaturePython', obj_name)
    CosmeticThread3DInternal(obj, ct3di_params)
    ViewProviderCosmeticThread3DInternal(obj.ViewObject)
    App.ActiveDocument.recompute()
    return obj



class CosmeticThread3DInternal:
    def __init__(self, obj, ct3di_params):
        """
        __init__(obj, ct3di_params)
        
        constructor of a CosmeticThread3DInternal class / internall function
        """
        self.Type = 'CosmeticThread3DInternal'
        obj.Proxy = self
        # Description - Read Only
        obj.addProperty('App::PropertyString', 'Description', 'Base', \
                        'Thread designation.', 1).Description \
                        = ct3di_params.name
        # D nominal - Read Only
        obj.addProperty('App::PropertyLength', 'D_nominal', 'ct3di_data', \
                        'Nominal diameter.', 1).D_nominal \
                        = ct3di_params.D_nominal
        # Pitch - Read only
        obj.addProperty('App::PropertyLength', 'pitch', 'ct3di_data', \
                        'Thread pitch.', 1).pitch \
                        = ct3di_params.pitch
        # Major diameter - Read only
        obj.addProperty('App::PropertyLength', 'D', 'ct3di_data', \
                        'Thread major diameter.', 1).D \
                        = ct3di_params.D
        # Minor diameter - Read only
        obj.addProperty('App::PropertyLength', 'D1', 'ct3di_data', \
                        'Thread minor diameter.', 1).D1 \
                        = ct3di_params.D1
        # Pre drilled recomendation - Read Only
        obj.addProperty('App::PropertyLength', 'D_drill', 'ct3di_data', \
                        'Recommended pre-driled hole diameter.', 1).D_drill \
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
        obj.addProperty('App::PropertyBool', 'length_trought', 'ct3di_data', \
                        'Thread is trought whole body?', 0).length_trought \
                        = ct3di_params.length_trought
        # Length tolerance - Read and Write
        obj.addProperty('App::PropertyString', 'length_tol', 'ct3di_data', \
                        'Length tolerance. For example "H17" or "0/+1.8" or just nothing.', 0).length_tol \
                        = ct3di_params.length_tol 
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
        # App.Console.PrintMessage("Change property: " + str(prop) + "\n")

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
        if obj.length_trought == True:
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



class ViewProviderCosmeticThread3DInternal:

    def __init__(self, obj):
        """
        Set this object to the proxy object of the actual view provider
        """
        obj.Proxy = self

    def attach(self, obj):
        """
        Setup the scene sub-graph of the view provider, this method is mandatory
        """
        return

    def updateData(self, fp, prop):
        """
        If a property of the handled feature has changed we have the chance to handle this here
        """
        return

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
        return

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



# ****************************************************************
# ****************************************************************
#
# Cosmetic Thread External ...
#
# ****************************************************************
# ****************************************************************



# There is a lot of parameters around cosmetic thread external for exchange
# informations on function calls and returns. I decide to wrap them into a class.
# It will be more easy to handle with one object than many separate
# variables...
class ct3de_params_class:
    def __init__(self):
        self.name           = "M10"    # [string]     Thread designation
        self.d_nominal      = 10.0     # [float - mm] Nominal diameter
        self.pitch          =  1.5     # [float - mm] Pitch - coarse
        self.d              = 10.0     # [float - mm] Big diameter (used for helix and thread stop) - tolerance = 0
        self.d3             =  8.160   # [float - mm] Small diameter - tolerance = 0 (used for thread shell)
        self.tolerance      = "6g"     # [string]     Hole thread tolerance (empty string allowed)
        self.roughness      = "Ra 1.6" # [string]     Hole thread roughness (empty string allowed)
        self.length         = 18.0     # [float - mm] Thread length
        self.length_trought = False    # [Bool]       Default value No. If Yes, thread does not have end shell.
        self.length_tol     = "H17"    # [string]     Length tolerance (empty string allowed). For example "H17" or "0/+1.8" or ""
        # metric_thread_params.attachement ???????       # Attachement to hole starting point and direction....



def external(obj_name=''):
    """
    Object creation method - Cosmetic Thread 3D Internal
    """
    
    # *** Fixme ***
    # *** Fixme ***
    # *** Fixme ***

    App.ActiveDocument.recompute()
    return obj

