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
Menu buttons for internal and external threads are here.
The UI definition itself and supporting functions are
moved into ct3dGuiTools.py
"""

import os
import FreeCAD as App
import FreeCADGui as Gui
from AttachmentEditor import Commands
import ct3d_params
import cosmeticthread3d_part as ct3d_p
import cosmeticthread3d_partdesign as ct3d_pd
import MetricCoarse1st
import ct3dGuiTools

__title__ = 'Cosmetic Thread 3D Work Bench'
__author__ = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__ = 'https://github.com/martinproks/cosmeticthread3d'

"""
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External
"""



# **************************************************************
# **************************************************************
#
# Part version, type 0 of geometry
#
# **************************************************************
# **************************************************************


# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p0_menu_command():
    """
    Command UI - cosmetic thread internal - Part version - type 0.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p0_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P0'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 0)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel' : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means,
            # script is continuing. There are functions associated
            # to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p0('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p0', ct3di_p0_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p0_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 0.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p0_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P0'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 0)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel' : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """

        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p0('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p0', ct3de_p0_menu_command())



# **************************************************************
# **************************************************************
#
# Part version, type 1 of geometry
#
# **************************************************************
# **************************************************************

# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p1_menu_command():
    """Command UI - cosmetic thread internal - Part version - type 1.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p1_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P1'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 1)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel' : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p1('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p1', ct3di_p1_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p1_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 1.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p1_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P1'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 1)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You need
        # to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p1('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p1', ct3de_p1_menu_command())




# **************************************************************
# **************************************************************
#
# Part version, type 2 of geometry
#
# **************************************************************
# **************************************************************

# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p2_menu_command():
    """
    Command UI - cosmetic thread internal - Part version - type 2.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p2_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P2'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 2)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p2('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p2', ct3di_p2_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p2_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 2.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p2_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P2'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 2)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p2('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p2', ct3de_p2_menu_command())




# **************************************************************
# **************************************************************
#
# Part version, type 3 of geometry
#
# **************************************************************
# **************************************************************

# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p3_menu_command():
    """
    Command UI - cosmetic thread internal - Part version - type 3.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p3_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P3'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 3)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p3('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p3', ct3di_p3_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p3_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 3.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p3_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P3'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 3)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL= delete temporary object, remove the conus and ends.
            #   APPLY = just update the conus position and dimensions.
            #   OK    = go far to the cosmetic thread creation - working code
            #           is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p3('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p3', ct3de_p3_menu_command())



# **************************************************************
# **************************************************************
#
# Part version, type 4 of geometry
#
# **************************************************************
# **************************************************************

# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p4_menu_command():
    """
    Command UI - cosmetic thread internal - Part version - type 4.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p4_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P4'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 4)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p4('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p4', ct3di_p4_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p4_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 4.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p4_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P4'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 4)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p4('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p4', ct3de_p4_menu_command())



# **************************************************************
# **************************************************************
#
# Part version, type 5 of geometry
#
# **************************************************************
# **************************************************************

# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_p5_menu_command():
    """
    Command UI - cosmetic thread internal - Part version - type 5.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_p5_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread P5'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 5)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.internal_p5('CosmeticThread3DInternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_p5', ct3di_p5_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_p5_menu_command():
    """
    Command UI - cosmetic thread external - Part version - type 5.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.aPart = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_p5_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread P5'
        Tool_tip = 'Create cosmetic thread geometry and parameters (Part version - type 5)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            self.aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowP_direction.create(self.doc,
                                                                self.aPart)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_p.external_p5('CosmeticThread3DExternal',
                                 ct3d_prms,
                                 self.doc,
                                 self.aPart)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        elif form.useGroup is True:
            ct3dGuiTools.useGroupThreads(obj, self.aPart)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_p5', ct3de_p5_menu_command())



# **************************************************************
# **************************************************************
#
# PartDesign version, type 0 of geometry
#
# **************************************************************
# **************************************************************


# +--------------------------------------------------------------+
# |                                                              |
# | Command for UI creating internal thread - PartDesign version |
# |                                                              |
# +--------------------------------------------------------------+
class ct3di_pd0_menu_command():
    """
    Command UI - cosmetic thread internal - PartDesign version - type 0.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.body = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_pd0_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread PD0'
        Tool_tip = 'Create cosmetic thread geometry and parameters (PartDesign version - type 0)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel' : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        self.body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        elif not self.body:
            App.Console.PrintError("No active body.\n")
        elif self.body.Tip is None:
            App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowPD_direction.create(self.doc,
                                                                 self.body)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means,
            # script is continuing. There are functions associated
            # to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_pd.internal_pd0('CosmeticThread3DInternal',
                                   ct3d_prms,
                                   self.doc,
                                   self.body)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowPD_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_pd0', ct3di_pd0_menu_command())



# +--------------------------------------------------------------+
# |                                                              |
# | Command for UI creating external thread - PartDesign version |
# |                                                              |
# +--------------------------------------------------------------+
class ct3de_pd0_menu_command():
    """
    Command UI - cosmetic thread external - PartDesign version - type 0.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.body = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_pd0_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread PD0'
        Tool_tip = 'Create cosmetic thread geometry and parameters (PartDesign version - type 0)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        self.body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        elif not self.body:
            App.Console.PrintError("No active body.\n")
        elif self.body.Tip is None:
            App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowPD_direction.create(self.doc,
                                                                 self.body)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_pd.external_pd0('CosmeticThread3DExternal',
                                   ct3d_prms,
                                   self.doc,
                                   self.body)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_pd0', ct3de_pd0_menu_command())



# **************************************************************
# **************************************************************
#
# PartDesign version, type 1 of geometry
#
# **************************************************************
# **************************************************************


# +--------------------------------------------------------------+
# |                                                              |
# | Command for UI creating internal thread - PartDesign version |
# |                                                              |
# +--------------------------------------------------------------+
class ct3di_pd1_menu_command():
    """
    Command UI - cosmetic thread internal - PartDesign version - type 1.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.body = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3di_pd1_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text = 'internal cosmetic thread PD1'
        Tool_tip = 'Create cosmetic thread geometry and parameters (PartDesign version - type 1)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel' : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        self.body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        elif not self.body:
            App.Console.PrintError("No active body.\n")
        elif self.body.Tip is None:
            App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowPD_direction.create(self.doc,
                                                                 self.body)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means,
            # script is continuing. There are functions associated
            # to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code
            #            is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with
        UI Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3di_params_class()
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsI(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_pd.internal_pd1('CosmeticThread3DInternal',
                                   ct3d_prms,
                                   self.doc,
                                   self.body)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_hole)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_hole, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_hole = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowPD_direction.scale(self.obj_tmp, D_hole)

Gui.addCommand('internal_cosmetic_thread_pd1', ct3di_pd1_menu_command())



# +--------------------------------------------------------------+
# |                                                              |
# | Command for UI creating external thread - PartDesign version |
# |                                                              |
# +--------------------------------------------------------------+
class ct3de_pd1_menu_command():
    """
    Command UI - cosmetic thread external - PartDesign version - type 1.
    This command is called from workbench menu or tool banner.
    """

    def __init__(self):
        self.doc = None
        self.obj_tmp = None
        self.body = None

    def GetResources(self):
        """
        Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip.
        """
        #
        # The name of a svg file available in the resources
        ct3d_path = ct3dGuiTools.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_pd1_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text = 'external cosmetic thread PD1'
        Tool_tip = 'Create cosmetic thread geometry and parameters (PartDesign version - type 1)'
        return {'Pixmap' : Pixmap_icon,
                # 'Accel'   : 'Shift+S', # a default shortcut (optional)
                'MenuText' : Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """
        Button pressed - do the working action here - call UI components...
        """
        #
        # self.doc must be here. __init__ is called when WB is loaded and
        # this was who knows when. The button is pressed NOW and now You
        # need to know active document...
        self.doc = App.ActiveDocument
        self.body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        elif not self.body:
            App.Console.PrintError("No active body.\n")
        elif self.body.Tip is None:
            App.Console.PrintError("Cosmetic thread can not be a first feature in a body.\n")
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = ct3dGuiTools.arrowPD_direction.create(self.doc,
                                                                 self.body)
            # Clear selected objects, if threre are any
            Gui.Selection.clearSelection(True)
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp,
                                    True,
                                    True,
                                    self.eA_ok,
                                    self.eA_cancel,
                                    self.eA_apply)
            # The command editAttachment is not modal. It means, script is
            # continuing. There are functions associated to OK/CANCEL/APPLY
            # buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working
            #            code is continuing there

    def IsActive(self):
        """
        Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional.
        """
        return True

    def eA_ok(self):
        """
        Reaction to editAttachment - OK has been pressed, go on with UI
        Thread Creation.
        """
        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_prms = ct3d_params.ct3de_params_class()
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.fillParamsE(ct3d_prms,
                                 lst_threads.getName(0),
                                 lst_threads)
        # Cosmetic thread creation
        obj = ct3d_pd.external_pd1('CosmeticThread3DExternal',
                                   ct3d_prms,
                                   self.doc,
                                   self.body)
        # Attachement apply from temporary object to cosmetic thread
        ct3dGuiTools.copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3dGuiTools.ct3d_threadUI(obj, D_shaft)
        form.exec_()
        if form.result == ct3dGuiTools.userCancelled:
            self.doc.removeObject(obj.Name)
        #
        # clean up...
        del lst_threads, ct3d_prms, D_shaft, obj

    def eA_cancel(self):
        """
        Reaction to editAttachment - CANCEL has been pressed.
        """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)

    def eA_apply(self):
        """
        Reaction to editAttachment - APPLY has been pressed.
        """
        D_shaft = ct3dGuiTools.diameter_from_attachment(self.obj_tmp)
        ct3dGuiTools.arrowP_direction.scale(self.obj_tmp, D_shaft)

Gui.addCommand('external_cosmetic_thread_pd1', ct3de_pd1_menu_command())
