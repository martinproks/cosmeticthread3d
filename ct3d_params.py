# -*- coding: utf-8 -*-
#
# ct3d_params.py
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

"""Parameters of internal and external threads. This is common for Part and
 PartDesign versions of threads."""

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



import os
import Part



# +--------------------------------------------------------+
# |                                                        |
# | get_module_path() - internal function                  |
# |                                                        |
# +--------------------------------------------------------+
def get_module_path():
    """Returns the current module path."""
    
    return os.path.dirname(__file__)



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
    """Definition class for internal thread parameters."""
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



# +--------------------------------------------------------+
# |                                                        |
# | addProperty_internal_thread()                          |
# |                                                        |
# +--------------------------------------------------------+
def addProperty_internal_thread(obj, ct3di_params):
    """addProperty_internal_thread(obj, ct3di_params) -> None.
    This function adds property into obj.
    This function is common for all internal threads types and variants."""

    # Description - Read and Write
    obj.addProperty('App::PropertyString', 'Description', 'Base', 'Thread designation.', 0).Description = ct3di_params.name
    # D nominal - Read and Write
    obj.addProperty('App::PropertyLength', 'D_nominal', 'ct3di_data', 'Nominal diameter.', 0).D_nominal = ct3di_params.D_nominal
    # Pitch - Read and Write
    obj.addProperty('App::PropertyLength', 'pitch', 'ct3di_data', 'Thread pitch.', 0).pitch = ct3di_params.pitch
    # Major diameter - Read and Write
    obj.addProperty('App::PropertyLength', 'D', 'ct3di_data', 'Thread major diameter.', 0).D = ct3di_params.D
    # Minor diameter - Read and Write
    obj.addProperty('App::PropertyLength', 'D1', 'ct3di_data', 'Thread minor diameter.', 0).D1 = ct3di_params.D1
    # Pre drilled recomendation - Read and Write
    obj.addProperty('App::PropertyLength', 'D_drill', 'ct3di_data', 'Recommended pre-driled hole diameter.', 0).D_drill = ct3di_params.D_drill
    # Thread tolerance - Read and Write
    obj.addProperty('App::PropertyString', 'tolerance', 'ct3di_data', 'Hole thread tolerance. For example "6H" or just nothing.', 0).tolerance = ct3di_params.tolerance
    # Roughness - Read and Write
    obj.addProperty('App::PropertyString', 'roughness', 'ct3di_data', 'Hole thread roughness. For example "Ra 1.6" or "Rz 2" or just nothing.', 0).roughness = ct3di_params.roughness
    # Length of thread - Read and Write
    obj.addProperty('App::PropertyLength', 'length', 'ct3di_data', 'Thread length.', 0).length = ct3di_params.length
    # Is the thread throught? - Read and Write
    obj.addProperty('App::PropertyBool', 'length_through', 'ct3di_data', 'Thread is through whole body?', 0).length_through = ct3di_params.length_through
    # Length tolerance - Read and Write
    obj.addProperty('App::PropertyString', 'length_tol', 'ct3di_data', 'Length tolerance. For example "H17" or "0/+1.8" or just nothing.', 0).length_tol = ct3di_params.length_tol 

    return None



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
    """Definition class for external thread parameters."""
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



# +--------------------------------------------------------+
# |                                                        |
# | addProperty_external_thread()                          |
# |                                                        |
# +--------------------------------------------------------+
def addProperty_external_thread(obj, ct3de_params):
    """addProperty_external_thread(obj, ct3de_params) -> None.
    This function adds property into obj.
    This function is common for all external threads types and variants."""

    # Description - Read and Write
    obj.addProperty('App::PropertyString', 'Description', 'Base', 'Thread designation.', 0).Description = ct3de_params.name
    # D nominal - Read and Write
    obj.addProperty('App::PropertyLength', 'D_nominal', 'ct3de_data', 'Nominal diameter.', 0).D_nominal = ct3de_params.D_nominal
    # Pitch - Read and Write
    obj.addProperty('App::PropertyLength', 'pitch', 'ct3de_data', 'Thread pitch.', 0).pitch = ct3de_params.pitch
    # Major diameter - Read and Write
    obj.addProperty('App::PropertyLength', 'D', 'ct3de_data', 'Thread major diameter.', 0).D = ct3de_params.D
    # Minor diameter - Read and Write
    obj.addProperty('App::PropertyLength', 'd3', 'ct3de_data', 'Thread minor diameter.', 0).d3 = ct3de_params.d3
    # Thread tolerance - Read and Write
    obj.addProperty('App::PropertyString', 'tolerance', 'ct3de_data', 'Extenal thread tolerance. For example "6g" or just nothing.', 0).tolerance = ct3de_params.tolerance
    # Roughness - Read and Write
    obj.addProperty('App::PropertyString', 'roughness', 'ct3de_data', 'External thread roughness. For example "Ra 1.6" or "Rz 2" or just nothing.', 0).roughness = ct3de_params.roughness
    # Length of thread - Read and Write
    obj.addProperty('App::PropertyLength', 'length', 'ct3de_data', 'Thread length.', 0).length = ct3de_params.length
    # Is the thread throught? - Read and Write
    obj.addProperty('App::PropertyBool', 'length_through', 'ct3de_data', 'Thread is through whole body?', 0).length_through = ct3de_params.length_through
    # Length tolerance - Read and Write
    obj.addProperty('App::PropertyString', 'length_tol', 'ct3de_data', 'Length tolerance. For example "H17" or "0/+1.8" or just nothing.', 0).length_tol = ct3de_params.length_tol

    return None

