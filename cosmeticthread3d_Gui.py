# -*- coding: utf-8 -*-
#
# cosmeticthread3d_Gui.py
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

__title__   = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL 2.1'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'



"""
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External
"""

import os
import FreeCAD as App
import FreeCADGui as Gui
import cosmeticthread3d
import MetricCoarse1st



class ct3di_menu_command():
    """internal cosmetic thread - GUI command"""

    def GetResources(self):
        # The name of a svg file available in the resources
        ct3d_path = cosmeticthread3d.get_module_path()
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.ct3di_menu_command() - icon to svg\n")
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text  = "internal cosmetic thread"
        Tool_tip   = "Create cosmetic thread geometry and parameters"
        return {"Pixmap"  : Pixmap_icon,
                # "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": Menu_text,
                "ToolTip" : Tool_tip}

    def Activated(self):
        """Button pressed - do something here"""
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            #
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = self.doc.addObject("Part::Cone","ThreadOrientation")
            self.obj_tmp.Label = "ThreadOrientation"
            self.doc.recompute()
            self.obj_tmp.Radius1 = '1.0 mm'
            self.obj_tmp.Radius2 = '0.0 mm'
            self.obj_tmp.Height  = '5.0 mm'
            #
            # Object Attachement...
            # Probem - The cone dimensions are fixed. But the hole dimensions could
            #          be from approx. 1 mm to infinity. It could be good, if the
            #          obj_tmp can react (scale) to the selected geometry in the
            #          Object Attachment. But I do not know how to do it - how
            #          to detect selected geometry and estimate the scale
            #
            from AttachmentEditor import Commands
            Commands.editAttachment(self.obj_tmp, True, True, self.eA_ok, self.eA_cancel, self.eA_apply)
            # The command editAttachment is not modal. It means, script is continuing.
            # There are functions associated to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position.
            #   OK     = go far to the cosmetic thread creation
        # end if
        #
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional."""
        return True

    def eA_ok(self):
        """Reaction to editAttachment - OK has been pressed"""
        #
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        #
        ct3di_params = cosmeticthread3d.ct3di_params_class()
        ct3di_params.name = lst_threads.name[0]
        ct3di_params.D_nominal = lst_threads.D_nominal[0]
        ct3di_params.pitch = lst_threads.pitch[0]
        ct3di_params.D = lst_threads.D[0]
        ct3di_params.D1 = lst_threads.D1[0]
        ct3di_params.d3 = lst_threads.d3[0]
        ct3di_params.D_drill = lst_threads.D_drill[0]
        ct3di_params.tolerance = '6H'
        ct3di_params.roughness = 'Ra 1.6'
        ct3di_params.length = 1.5
        ct3di_params.length_trought = False
        ct3di_params.length_tol = "H17"

        # Thread parameters definition
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.eA_ok() - thread parameters definition...\n")
        #
        # Cosmetic thread creation
        obj = cosmeticthread3d.internal('', ct3di_params)
        #
        # Attachement apply from temporary object to cosmetic thread
        obj.AttachmentOffset = self.obj_tmp.AttachmentOffset
        obj.MapReversed      = self.obj_tmp.MapReversed 
        obj.Support          = self.obj_tmp.Support
        obj.MapPathParameter = self.obj_tmp.MapPathParameter
        obj.MapMode          = self.obj_tmp.MapMode
        obj.recompute()
        #
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        return

    def eA_cancel(self):
        """Reaction to editAttachment - CANCEL has been pressed """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)
        return

    def eA_apply(self):
        """Reaction to editAttachment - APPLY has been pressed """
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.eA_apply() - estimate hole diameter and scale cone.\n")
        return

Gui.addCommand("internal_cosmetic_thread", ct3di_menu_command())



class ct3de_menu_command():
    """Command external cosmetic thread - menu and tool bar"""

    def GetResources(self):
        ct3d_path = cosmeticthread3d.get_module_path()
        App.Console.PrintMessage('*** FIXME *** cosmeticthread3d_Gui.ct3de_menu_command() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')

        Menu_text  = 'external cosmetic thread'
        Tool_tip   = 'Create cosmetic thread geometry and parameters'
        return {'Pixmap'  : Pixmap_icon,
                # "Accel"   : "Shift+S", # a default shortcut (optional)
                'MenuText': Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """Button pressed - do something here"""
        # Make GUI part of the creation
        # xxxxxxxxxxx
        # Call the geometry creation function and give there all necessary parameters
        cosmeticthread3d.external()
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional."""
        return True

Gui.addCommand("external_cosmetic_thread", ct3de_menu_command())
