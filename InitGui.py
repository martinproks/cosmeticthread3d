# -*- coding: utf-8 -*-
#
# InitGui.py
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
In the InitGui.py file you usually define a workbench, which contains a name,
an icon, and a series of FreeCAD commands (see below). That python file also
defines functions that are executed when FreeCAD loads. You try to do as little
as possible there, so you don't slow down the startup. Another that gets
executed when the workbench is activated, that's where you'll do most
of the work. The third one when the workbench is deactivated, so you can
remove things if needed.
"""

import os

__title__ = 'Cosmetic Thread 3D Work Bench'
__author__ = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__ = 'https://github.com/martinproks/cosmeticthread3d'

class CosmeticThread3D(Workbench):
    """
    CosmeticThread3D Workbench definition class
    """

    def __init__(self):
        #
        import ct3d_params
        #
        self.list = []
        self.__class__.MenuText = 'Cosmetic Thread 3D'
        self.__class__.ToolTip = 'Create cosmetic thread at model space - holes and rods'
        self.__class__.Icon = os.path.join(ct3d_params.get_module_path(), \
                                           'icons', \
                                           'CosmeticThread3D_WB.png')

    def Initialize(self):
        """
        This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated
        function.
        """
        #
        import cosmeticthread3d_Gui
        #
        # a list of command names created in the line above
        self.list = ['internal_cosmetic_thread_p0',
                     'external_cosmetic_thread_p0',
                     'internal_cosmetic_thread_p1',
                     'external_cosmetic_thread_p1',
                     'internal_cosmetic_thread_p2',
                     'external_cosmetic_thread_p2',
                     'internal_cosmetic_thread_p3',
                     'external_cosmetic_thread_p3',
                     'internal_cosmetic_thread_p4',
                     'external_cosmetic_thread_p4',
                     'internal_cosmetic_thread_pd0',
                     'external_cosmetic_thread_pd0',
                     'internal_cosmetic_thread_pd1',
                     'external_cosmetic_thread_pd1']
        #
        # # creates a new toolbar with your commands
        # # toolbar not necessary, this workbench is for developement and testing of tools
        # self.appendToolbar("Cosmetic_Thread_3D", self.list)
        #
        # creates a new menu
        self.appendMenu('Cosmetic Thread 3D', self.list)
        #
        # # appends a submenu to an existing menu
        # self.appendMenu(["An existing Menu", "My submenu"], self.list)

    def Activated(self):
        """
        This function is executed whenever the workbench is activated
        """

    def Deactivated(self):
        """
        This function is executed whenever the workbench is deactivated
        """

    def ContextMenu(self, recipient):
        """
        This function is executed whenever the user right-clicks on screen
        """
        # "recipient" will be either "view" or "tree"
        # add commands to the context menu
        # self.appendContextMenu("My commands", self.list)

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly
        #      "Gui::PythonWorkbench"
        return 'Gui::PythonWorkbench'

Gui.addWorkbench(CosmeticThread3D())
