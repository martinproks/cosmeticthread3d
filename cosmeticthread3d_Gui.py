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
__License__ = 'LGPL-2.1-or-later'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'



"""
Vocabulary:
ct3d   - Cosmetic Thread 3D
ct3di  - Cosmetic Thread 3D Internal
ct3de  - Cosmetic Thread 3D External
"""

import os
from PySide import QtCore, QtGui
import FreeCAD as App
import FreeCADGui as Gui
from AttachmentEditor import Commands
import cosmeticthread3d
import MetricCoarse1st



# UI constants - results of modal dialogs
userCancelled = 'Cancel button pressed'
userOk        = 'OK button pressed'
# userApply     = 'Apply button pressed'



# +-------------------------------------------------------+
# |                                                       |
# | UI for thread dimensions and parameters selection     |
# |                                                       |
# +-------------------------------------------------------+
class ct3d_threadUI(QtGui.QDialog):
    """UI for thread parameters definition - common for all threads."""
    # https://wiki.freecad.org/PySide_Intermediate_Examples
    # https://doc.qt.io/qt-5/qtwidgets-module.html
    # https://doc.qt.io/qt-5/qcheckbox.html
    # https://doc.qt.io/qt-5/qcombobox.html
    # https://doc.qt.io/qt-5/qlineedit.html
    def __init__(self, obj, Dobj, lst_threads):
        # the obj ans lst_threads pointers are copied to internal variables accessible from other methods
        self.s_obj = obj
        self.s_Dobj = Dobj # diameter of hole or shaft - it depends on obj if it has parameters d3 (external) or D1 (internal)
        self.s_lst_threads = lst_threads
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.ct3d_threadUI.__init__() - Dobj -> thread estimation - s_lstCurrentIndex\n")
        self.s_lstCurrentIndex = 0
        #
        super(ct3d_threadUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.result = userCancelled
        i = self.s_lstCurrentIndex # too long name for use, just call it 'i' for now
 	# create our window
	# define window  xLoc,yLoc,xDim,yDim
        self.setGeometry(250, 250, 400, 420)
        self.setWindowTitle("Cosmetic Thread 3D")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #
        # Widget name (it means Thread selection)
        y = 10
        self.label0a = QtGui.QLabel("Thread selected", self)
        self.label0a.setFont('Courier')
        self.label0a.move(10, y)
        self.w_name = QtGui.QComboBox(self)
        self.w_name.addItems(self.s_lst_threads.name)
        self.w_name.setCurrentIndex(self.s_lstCurrentIndex)
        self.w_name.activated[str].connect(self.onPopupThreadSel)
        self.w_name.move(180, y)
        #
        # Widget D_nominal
        y += 30
        self.label1a = QtGui.QLabel("D nominal", self)
        self.label1a.setFont('Courier')
        self.label1a.move(30, y)
        self.w_D_nom = QtGui.QLineEdit(self)
        self.w_D_nom.setInputMask("####.###")
        self.w_D_nom.setText(str(self.s_lst_threads.D_nominal[i]))
        self.w_D_nom.setFixedWidth(65)
        self.w_D_nom.setReadOnly(True)
        self.w_D_nom.move(210, y)
        self.label1b = QtGui.QLabel("mm", self)
        self.label1b.setFont('Courier')
        self.label1b.move(290, y)
        #
        # Widget pitch
        y += 30
        self.label2a = QtGui.QLabel("Pitch", self)
        self.label2a.setFont('Courier')
        self.label2a.move(30, y)
        self.w_pitch = QtGui.QLineEdit(self)
        self.w_pitch.setInputMask("####.###")
        self.w_pitch.setText(str(self.s_lst_threads.pitch[i]))
        self.w_pitch.setFixedWidth(65)
        self.w_pitch.setReadOnly(True)
        self.w_pitch.move(210, y)
        self.label2b = QtGui.QLabel("mm", self)
        self.label2b.setFont('Courier')
        self.label2b.move(290, y)
        #
        # Widget D
        y += 30
        self.label3a = QtGui.QLabel("D", self)
        self.label3a.setFont('Courier')
        self.label3a.move(30, y)
        self.w_D = QtGui.QLineEdit(self)
        self.w_D.setInputMask("####.###")
        self.w_D.setText(str(self.s_lst_threads.D[i]))
        self.w_D.setFixedWidth(65)
        self.w_D.setReadOnly(True)
        self.w_D.move(210, y)
        self.label3b = QtGui.QLabel("mm", self)
        self.label3b.setFont('Courier')
        self.label3b.move(290, y)
        #
        # Widget D1
        y += 30
        self.label4a = QtGui.QLabel("D1", self)
        self.label4a.setFont('Courier')
        self.label4a.move(30, y)
        self.w_D1 = QtGui.QLineEdit(self)
        self.w_D1.setInputMask("####.###")
        self.w_D1.setText(str(self.s_lst_threads.D1[i]))
        self.w_D1.setFixedWidth(65)
        self.w_D1.setReadOnly(True)
        self.w_D1.move(210, y)
        self.label4b = QtGui.QLabel("mm", self)
        self.label4b.setFont('Courier')
        self.label4b.move(290, y)
        #
        # Widget d3
        y += 30
        self.label5a = QtGui.QLabel("d3", self)
        self.label5a.setFont('Courier')
        self.label5a.move(30, y)
        self.w_d3 = QtGui.QLineEdit(self)
        self.w_d3.setInputMask("####.###")
        self.w_d3.setText(str(self.s_lst_threads.d3[i]))
        self.w_d3.setFixedWidth(65)
        self.w_d3.setReadOnly(True)
        self.w_d3.move(210, y)
        self.label5b = QtGui.QLabel("mm", self)
        self.label5b.setFont('Courier')
        self.label5b.move(290, y)
        #
        # Widget D_drill
        y += 30
        self.label6a = QtGui.QLabel("D drill recommended", self)
        self.label6a.setFont('Courier')
        self.label6a.move(30, y)
        self.w_D_drill = QtGui.QLineEdit(self)
        self.w_D_drill.setInputMask("####.###")
        self.w_D_drill.setText(str(self.s_lst_threads.D_drill[i]))
        self.w_D_drill.setFixedWidth(65)
        self.w_D_drill.setReadOnly(True)
        self.w_D_drill.move(210, y)
        self.label6b = QtGui.QLabel("mm", self)
        self.label6b.setFont('Courier')
        self.label6b.move(290, y)
        #
        # Widget thr_tol
        y += 30
        self.label7a = QtGui.QLabel("Thread tolerances", self)
        self.label7a.setFont('Courier')
        self.label7a.move(10, y)
        self.w_thr_tol = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_thr_tol.setText('')
        self.w_thr_tol.setFixedWidth(80)
        self.w_thr_tol.setReadOnly(False)
        self.w_thr_tol.move(180, y)
        self.label7b = QtGui.QLabel("e.g. 6H or 6g", self)
        self.label7b.setFont('Courier')
        self.label7b.move(270, y)
        #
        # Widget thr_rgh
        y += 30
        self.label8a = QtGui.QLabel("Thread roughness", self)
        self.label8a.setFont('Courier')
        self.label8a.move(10, y)
        self.w_thr_rgh = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_thr_rgh.setText('')
        self.w_thr_rgh.setFixedWidth(80)
        self.w_thr_rgh.setReadOnly(False)
        self.w_thr_rgh.move(180, y)
        self.label8b = QtGui.QLabel("e.g. Ra 1.6", self)
        self.label8b.setFont('Courier')
        self.label8b.move(270, y)
        #
        # Widget thr_through
        y += 30
        self.label9a = QtGui.QLabel("Thread through hole", self)
        self.label9a.setFont('Courier')
        self.label9a.move(10, y)
        self.w_thr_through = QtGui.QCheckBox("(full length)", self)
        # self.w_thr_through.clicked.connect(self.onCheckbox1) # on, I do not wan connect anything. I read isChecked at the end...
        self.w_thr_through.setChecked(False)
        self.w_thr_through.move(180,y)
        #
        # Widget len
        y += 30
        self.label10a = QtGui.QLabel("Thread length", self)
        self.label10a.setFont('Courier')
        self.label10a.move(10, y)
        self.w_len = QtGui.QLineEdit(self)
        self.w_len.setInputMask("####.###")
        self.w_len.setText(str(self.s_lst_threads.D_drill[i] * 1.5)) # something for start, why not Dx1.5
        self.w_len.setFixedWidth(65)
        self.w_len.setReadOnly(False)
        self.w_len.move(180, y)
        self.label10b = QtGui.QLabel("mm", self)
        self.label10b.setFont('Courier')
        self.label10b.move(270, y)
        #
        # Widget len_tol
        y += 30
        self.label11a = QtGui.QLabel("Length tolerances", self)
        self.label11a.setFont('Courier')
        self.label11a.move(10, y)
        self.w_len_tol = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_len_tol.setText('')
        self.w_len_tol.setFixedWidth(80)
        self.w_len_tol.setReadOnly(False)
        self.w_len_tol.move(180, y)
        self.label11b = QtGui.QLabel("e.g. 0/+2.0", self)
        self.label11b.setFont('Courier')
        self.label11b.move(270, y)
        #
        # apply button
        y += 50
        applyButton = QtGui.QPushButton('Apply', self)
        applyButton.clicked.connect(self.onApply)
        applyButton.setAutoDefault(True)
        applyButton.move(40, y)
        #
        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, y)
        #
        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, y)
        self.show()

    def onPopupThreadSel(self, selectedText):
        # user selected some thread type, fill widgets by values from self.s_lst_threads
        i = self.w_name.currentIndex()
        self.s_lstCurrentIndex = i
        self.w_D_nom.setText(str(self.s_lst_threads.D_nominal[i]))
        self.w_pitch.setText(str(self.s_lst_threads.pitch[i]))
        self.w_D.setText(str(self.s_lst_threads.D[i]))
        self.w_D1.setText(str(self.s_lst_threads.D1[i]))
        self.w_d3.setText(str(self.s_lst_threads.d3[i]))
        self.w_D_drill.setText(str(self.s_lst_threads.D_drill[i]))
        #
        # Rest of the values are independent on thread selection
        return

    def onApply(self):
        i = self.w_name.currentIndex()
        self.s_obj.Label       = self.w_name.currentText()
        self.s_obj.Description = self.w_name.currentText()
        self.s_obj.D_nominal   = float(self.w_D_nom.text())
        self.s_obj.pitch       = float(self.w_pitch.text())
        self.s_obj.D           = float(self.w_D.text())
        if hasattr(self.s_obj, 'D1'): # internal thread
            self.s_obj.D1      = float(self.w_D1.text())
        if hasattr(self.s_obj, 'd3'): # external thread
            self.s_obj.d3      = float(self.w_d3.text())
        if hasattr(self.s_obj, 'D_drill'):  # internal thread
            self.s_obj.D_drill = float(self.w_D_drill.text())
        self.s_obj.tolerance   = self.w_thr_tol.displayText() # do not remmove white chars - displayText
        self.s_obj.roughness   = self.w_thr_rgh.displayText() # do not remmove white chars - displayText
        self.s_obj.length_through =  self.w_thr_through.isChecked()
        self.s_obj.length      = float(self.w_len.text())
        self.s_obj.length_tol  = self.w_len_tol.displayText() # do not remmove white chars - displayText
        #
        self.s_obj.recompute()
        return
        
    def onCancel(self):
        self.result = userCancelled
        self.close()
        return

    def onOk(self):
        self.result = userOk
        self.onApply()
        self.close()
        return



# +-------------------------------------------------------+
# |                                                       |
# | Arrow / direction symbol - internal class / functions |
# |                                                       |
# +-------------------------------------------------------+
class arrow_direction():
    """Arrow / direction symbol
    service class for tools for create/manipulate it"""

    def __init__(self):
        """__init__() - internal initialization function."""
        #
        # empty
        return
    
    def create():
        """create() -> obj

        Create directional symbol / arrow / cone and return textlink (obj) at it."""
        #
        obj = App.ActiveDocument.addObject("Part::Cone","ThreadOrientation")
        obj.Label = "ThreadOrientation"
        obj.Radius1 = '1.0 mm'
        obj.Radius2 = '0.0 mm'
        obj.Height  = '2.5 mm'
        obj.recompute()
        return obj
    
    def scale(obj, hole_diameter):
        """scale(obj, hole_diameter)

        Scale directional symbol / arrow / cone (textlink obj) to be visually adequate to hole diameter.
        """
        #
        obj.Radius1 = 0.25 * hole_diameter
        obj.Radius2 = 0.0
        obj.Height  = 2.5 * obj.Radius1
        obj.recompute()
        return



# +-------------------------------------------------------+
# |                                                       |
# | Copy attachent() - service functions                  |
# |                                                       |
# +-------------------------------------------------------+
def copy_attachment(obj_from, obj_to):
    """copy_attachment(obj_from, obj_to)
    
    Internal function.
    """
    #
    obj_to.AttachmentOffset = obj_from.AttachmentOffset
    obj_to.MapReversed      = obj_from.MapReversed 
    obj_to.Support          = obj_from.Support
    obj_to.MapPathParameter = obj_from.MapPathParameter
    obj_to.MapMode          = obj_from.MapMode
    #
    return



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating internal thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3di_menu_command():
    """Command UI - cosmetic thread internal.
    This command is called from workbench menu or tool banner.
    """

    def GetResources(self):
        """Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip."""
        #
        # The name of a svg file available in the resources
        ct3d_path = cosmeticthread3d.get_module_path()
        App.Console.PrintMessage("*** FIXME *** ct3di_menu_command.GetResources() - icon to svg\n")
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'internal_thread.xpm')
        Menu_text  = "internal cosmetic thread"
        Tool_tip   = "Create cosmetic thread geometry and parameters"
        return {"Pixmap"  : Pixmap_icon,
                # "Accel"   : "Shift+S", # a default shortcut (optional)
                "MenuText": Menu_text,
                "ToolTip" : Tool_tip}

    def Activated(self):
        """Button pressed - do the working action here - call UI components..."""
        #
        # self.doc must be here. __init__ is called when WB is loaded and this was who knows when.
        # The button is pressed NOW and now You need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = arrow_direction.create()
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp, True, True, self.eA_ok, self.eA_cancel, self.eA_apply)
            # The command editAttachment is not modal. It means, script is continuing.
            # There are functions associated to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code is continuing there
        # end if
        #
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional."""
        result = True
        return result

    def eA_ok(self):
        """Reaction to editAttachment - OK has been pressed, go on with UI Thread Creation"""

        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_params = cosmeticthread3d.ct3di_params_class()

        App.Console.PrintMessage("*** FIXME *** ct3di_menu_command.eA_ok() - estimate hole diameter D_hole\n")
        D_hole = 8.5
        ct3d_params.name = lst_threads.name[0]
        ct3d_params.D_nominal = lst_threads.D_nominal[0]
        ct3d_params.pitch = lst_threads.pitch[0]
        ct3d_params.D = lst_threads.D[0]
        ct3d_params.D1 = lst_threads.D1[0]
        # ct3d_params.d3 = lst_threads.d3[0] # internal thread doesn't have this parameter
        ct3d_params.D_drill = lst_threads.D_drill[0]
        ct3d_params.tolerance = '6H'
        ct3d_params.roughness = 'Ra 1.6'
        ct3d_params.length = 1.5 * ct3d_params.D_nominal
        ct3d_params.length_through = False
        ct3d_params.length_tol = "H17"

        # Cosmetic thread creation
        obj = cosmeticthread3d.internal('CosmeticThread3DInternal', ct3d_params)
        # Attachement apply from temporary object to cosmetic thread
        copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3d_threadUI(obj, D_hole, lst_threads)
        form.exec_()
        if form.result == userCancelled:
            self.doc.removeObject(obj.Name)
        # elif form.result == userOk:
        #    obj.recompute()
        #
        # clean up...
        del(lst_threads)
        del(ct3d_params)
        del(D_hole)
        del(obj)

        return

    def eA_cancel(self):
        """Reaction to editAttachment - CANCEL has been pressed """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)
        return

    def eA_apply(self):
        """Reaction to editAttachment - APPLY has been pressed """
        App.Console.PrintMessage("*** FIXME *** cosmeticthread3d_Gui.eA_apply() - estimate hole diameter and scale cone.\n")
        D_hole = 8.5 # FIXME - estimate it correctly...
        arrow_direction.scale(self.obj_tmp, D_hole)
        return

Gui.addCommand("internal_cosmetic_thread", ct3di_menu_command())



# +--------------------------------------------------------+
# |                                                        |
# | Command for UI creating external thread - Part version |
# |                                                        |
# +--------------------------------------------------------+
class ct3de_menu_command():
    """Command external cosmetic thread - UI.
    This command is called from workbench menu or tool banner.
    """
  
    def GetResources(self):
        """Mandatory method for WorkBench Menu/tools button.
        It returns icon, menu text and tool tip."""
        #
        # The name of a svg file available in the resources
        ct3d_path = cosmeticthread3d.get_module_path()
        App.Console.PrintMessage('*** FIXME *** ct3de_menu_command.GetResources() - icon to svg\n')
        Pixmap_icon = os.path.join(ct3d_path, 'icons', 'external_thread.xpm')
        Menu_text  = 'external cosmetic thread'
        Tool_tip   = 'Create cosmetic thread geometry and parameters'
        return {'Pixmap'  : Pixmap_icon,
                # "Accel"   : "Shift+S", # a default shortcut (optional)
                'MenuText': Menu_text,
                'ToolTip' : Tool_tip}

    def Activated(self):
        """Button pressed - do the working action here - call UI components..."""
        #
        # self.doc must be here. __init__ is called when WB is loaded and this was who knows when.
        # The button is pressed NOW and now You need to know active document...
        self.doc = App.ActiveDocument
        if not self.doc:
            App.Console.PrintError('No Active Document.\n')
        else:
            # Make GUI part of the creation
            # Create an temporary object - arrow/cone for example
            self.obj_tmp = arrow_direction.create()
            # Object Attachement...
            Commands.editAttachment(self.obj_tmp, True, True, self.eA_ok, self.eA_cancel, self.eA_apply)
            # The command editAttachment is not modal. It means, script is continuing.
            # There are functions associated to OK/CANCEL/APPLY buttons I can use.
            #   CANCEL = delete temporary object, remove the conus and ends.
            #   APPLY  = just update the conus position and dimensions.
            #   OK     = go far to the cosmetic thread creation - working code is continuing there
        # end if
        #
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed)
        if certain conditions are met or not. This function is optional."""
        return True

    def eA_ok(self):
        """Reaction to editAttachment - OK has been pressed, go on with UI Thread Creation"""

        lst_threads = MetricCoarse1st.MetricCoarse1st()
        ct3d_params = cosmeticthread3d.ct3de_params_class()

        App.Console.PrintMessage("*** FIXME *** ct3de_menu_command.eA_ok() - estimate shaft diameter D_shaft\n")
        D_shaft = 10
        ct3d_params.name = lst_threads.name[0]
        ct3d_params.D_nominal = lst_threads.D_nominal[0]
        ct3d_params.pitch = lst_threads.pitch[0]
        ct3d_params.D = lst_threads.D[0]
        # ct3d_params.D1 = lst_threads.D1[0] # external thread doesn't have this parameter
        ct3d_params.d3 = lst_threads.d3[0]
        # ct3d_params.D_drill = lst_threads.D_drill[0] # external thread doesn't have this parameter
        ct3d_params.tolerance = '6g'
        ct3d_params.roughness = 'Ra 1.6'
        ct3d_params.length = 1.5 * ct3d_params.D_nominal
        ct3d_params.length_through = False
        ct3d_params.length_tol = "H17"

        # Cosmetic thread creation
        obj = cosmeticthread3d.external('CosmeticThread3DExternal', ct3d_params)
        # Attachement apply from temporary object to cosmetic thread
        copy_attachment(self.obj_tmp, obj)
        obj.recompute()
        #
        # Remove temporary geometry (directional arrow / cone) from document
        self.doc.removeObject(self.obj_tmp.Name)
        #
        # UI thread parameters estimation.
        # UI IS modal. It means code is waiting to UI close.
        form = ct3d_threadUI(obj, D_shaft, lst_threads)
        form.exec_()
        if form.result == userCancelled:
            self.doc.removeObject(obj.Name)
        # elif form.result == userOk:
        #    obj.recompute()
        #
        # clean up...
        del(lst_threads)
        del(ct3d_params)
        del(D_shaft)
        del(obj)

        return

    def eA_cancel(self):
        """Reaction to editAttachment - CANCEL has been pressed """
        # Remove geometry from document
        self.doc.removeObject(self.obj_tmp.Name)
        return

    def eA_apply(self):
        """Reaction to editAttachment - APPLY has been pressed """
        App.Console.PrintMessage("*** FIXME *** ct3de_menu_command.eA_apply() - estimate D_shaft and scale cone.\n")
        D_shaft = 10 # FIXME - estimate it correctly...
        arrow_direction.scale(self.obj_tmp, D_shaft)
        return

Gui.addCommand("external_cosmetic_thread", ct3de_menu_command())
