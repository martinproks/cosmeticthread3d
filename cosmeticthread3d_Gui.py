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
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            #
            # Call the geometry creation function and give there all necessary parameters
            cosmeticthread3d.internal('', '')
        #
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional."""
        return True

Gui.addCommand("internal_cosmetic_thread", ct3di_menu_command())



class ct3de_menu_command():
    """Command external cosmetic thread - menu and tool bar"""

    def GetResources(self):
        ct3d_path = cosmeticthread3d.get_module_path()
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.ct3de_menu_command() - icon to svg\n")
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')

        Menu_text  = "external cosmetic thread"
        Tool_tip   = "Create cosmetic thread geometry and parameters"
        return {"Pixmap"  : Pixmap_icon,
                # "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": Menu_text,
                "ToolTip" : Tool_tip}

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
