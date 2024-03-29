# -*- coding: utf-8 -*-
#
# ct3dGuiTools.py
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
Tools for GUI of Cosmetic Tread 3D.
Functions and tools in this module are common for all GUI buttons/commands.
I decided to move it to separate file for smaller an better to read
the main GUI script with buttons.
"""

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
from PySide.QtGui import QFrame
import FreeCAD as App
import FreeCADGui as Gui
import Part



# +-----------------------------------------------------+
# |                                                     |
# |      UI constants - results of modal dialogs        |
# |                                                     |
# +-----------------------------------------------------+
userCancelled = 'Cancel button pressed'
userOk        = 'OK button pressed'
# userApply     = 'Apply button pressed'



# +--------------------------------------------------------+
# |                                                        |
# | get_module_path() - internal function                  |
# |                                                        |
# +--------------------------------------------------------+
def get_module_path():
    """Returns the current module path."""
    
    return os.path.dirname(__file__)



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
        """__init__(obj, Dobj, lst_thread)
        
        Create UI for thread dimensions and parameters definition
        and copy the values to the obj properties.

        obj         - [text link]            Object with thread parameters...
        Dobj       - [mm]                    Hole or shaft diameter for preliminary thread estimation.
        lst_thread - [class list of threads] List of threads with tabularized values
        """
        
        # the obj ans lst_threads pointers are copied to internal variables accessible from other methods
        self.s_obj = obj
        self.s_lthr = lst_threads
        self.useGroup = False
        self.s_lstCurrentIndex = 0
        
        # Estimate/guess thread according the best matching Dobj
        n = len(self.s_lthr.getLstNames())
        # internal thread
        if hasattr(self.s_obj, 'D1'):
            i = 0
            Ddrill = self.s_lthr.getD_drill(self.s_lthr.getName(i))
            deviance = abs(Ddrill - Dobj) / Ddrill # relative value based on D_drill
            while i < n-1:
                Ddrill = self.s_lthr.getD_drill(self.s_lthr.getName(i+1))
                deviance_next = abs(Ddrill - Dobj) / Ddrill # relative value based on D_drill
                if deviance > deviance_next: # while the deviance is descending (deviance > deviance_next), [i+1] is matching better than [i].
                    self.s_lstCurrentIndex = i+1
                else:  # STOP, the [i] matched better than [i+1]
                    i = n-2 # this will force to stop
                i += 1 # move i for nex turn...
                deviance = deviance_next # and actualize appropriate deviance
            del(Ddrill)
        # external thread
        if hasattr(self.s_obj, 'd3'):
            i = 0
            Dtmp = self.s_lthr.getD(self.s_lthr.getName(i))
            deviance = abs(Dtmp - Dobj) / Dtmp # relative value based on D
            while i < n-1:
                Dtmp = self.s_lthr.getD(self.s_lthr.getName(i+1))
                deviance_next = abs(Dtmp - Dobj) / Dtmp # relative value based on D
                if deviance > deviance_next: # while the deviance is descending, [i+1] is matching better than [i].
                    self.s_lstCurrentIndex = i+1
                else:  # STOP, the [i] matched better than [i+1]
                    i = n-2 # this will force to stop
                i += 1 # move i for nex turn...
                deviance = deviance_next # and actualize appropriate deviance
            del(Dtmp)
        del(Dobj)
        del(deviance)
        del(deviance_next)
        del(i)
        del(n)

        # UI itself...
        super(ct3d_threadUI, self).__init__()
        self.initUI()
        return None

    def initUI(self):
        self.result = userCancelled
        i = self.s_lstCurrentIndex # too long name for use, just call it 'i' for now
        name = self.s_lthr.getName(i)
 	# create our window
	# define window  xLoc,yLoc,xDim,yDim
        self.setGeometry(250, 250, 400, 480)
        self.setWindowTitle('Cosmetic Thread 3D')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #
        # Widget name (it means Thread selection)
        y = 10
        self.label0a = QtGui.QLabel('Thread selected', self)
        self.label0a.setFont('Courier')
        self.label0a.move(10, y)
        self.w_name = QtGui.QComboBox(self)
        self.w_name.addItems(self.s_lthr.getLstNames())
        self.w_name.setCurrentIndex(self.s_lstCurrentIndex)
        self.w_name.activated[str].connect(self.onPopupThreadSel)
        self.w_name.move(180, y)
        #
        # Widget D_nominal
        y += 30
        self.label1a = QtGui.QLabel('D nominal', self)
        self.label1a.setFont('Courier')
        self.label1a.move(30, y)
        self.w_D_nom = QtGui.QLineEdit(self)
        self.w_D_nom.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D_nom.setText(str(self.s_lthr.getD_nominal(name)))
        self.w_D_nom.setFixedWidth(65)
        self.w_D_nom.setReadOnly(True)
        self.w_D_nom.move(210, y)
        self.label1b = QtGui.QLabel('mm', self)
        self.label1b.setFont('Courier')
        self.label1b.move(290, y)
        #
        # Widget pitch
        y += 30
        self.label2a = QtGui.QLabel('Pitch', self)
        self.label2a.setFont('Courier')
        self.label2a.move(30, y)
        self.w_pitch = QtGui.QLineEdit(self)
        self.w_pitch.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_pitch.setText(str(self.s_lthr.getpitch(name)))
        self.w_pitch.setFixedWidth(65)
        self.w_pitch.setReadOnly(True)
        self.w_pitch.move(210, y)
        self.label2b = QtGui.QLabel('mm', self)
        self.label2b.setFont('Courier')
        self.label2b.move(290, y)
        #
        # Widget D
        y += 30
        self.label3a = QtGui.QLabel('D', self)
        self.label3a.setFont('Courier')
        self.label3a.move(30, y)
        self.w_D = QtGui.QLineEdit(self)
        self.w_D.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D.setText(str(self.s_lthr.getD(name)))
        self.w_D.setFixedWidth(65)
        self.w_D.setReadOnly(True)
        self.w_D.move(210, y)
        self.label3b = QtGui.QLabel('mm', self)
        self.label3b.setFont('Courier')
        self.label3b.move(290, y)
        #
        # Widget D1
        y += 30
        self.label4a = QtGui.QLabel('D1', self)
        self.label4a.setFont('Courier')
        self.label4a.move(30, y)
        self.w_D1 = QtGui.QLineEdit(self)
        self.w_D1.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D1.setText(str(self.s_lthr.getD1(name)))
        self.w_D1.setFixedWidth(65)
        self.w_D1.setReadOnly(True)
        self.w_D1.move(210, y)
        self.label4b = QtGui.QLabel('mm', self)
        self.label4b.setFont('Courier')
        self.label4b.move(290, y)
        #
        # Widget d3
        y += 30
        self.label5a = QtGui.QLabel('d3', self)
        self.label5a.setFont('Courier')
        self.label5a.move(30, y)
        self.w_d3 = QtGui.QLineEdit(self)
        self.w_d3.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_d3.setText(str(self.s_lthr.getd3(name)))
        self.w_d3.setFixedWidth(65)
        self.w_d3.setReadOnly(True)
        self.w_d3.move(210, y)
        self.label5b = QtGui.QLabel('mm', self)
        self.label5b.setFont('Courier')
        self.label5b.move(290, y)
        #
        # Widget D_drill
        y += 30
        self.label6a = QtGui.QLabel('D drill recommended', self)
        self.label6a.setFont('Courier')
        self.label6a.move(30, y)
        self.w_D_drill = QtGui.QLineEdit(self)
        self.w_D_drill.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D_drill.setText(str(self.s_lthr.getD_drill(name)))
        self.w_D_drill.setFixedWidth(65)
        self.w_D_drill.setReadOnly(True)
        self.w_D_drill.move(210, y)
        self.label6b = QtGui.QLabel('mm', self)
        self.label6b.setFont('Courier')
        self.label6b.move(290, y)
        #
        # Widget thr_tol
        y += 30
        self.label7a = QtGui.QLabel('Thread tolerances', self)
        self.label7a.setFont('Courier')
        self.label7a.move(10, y)
        self.w_thr_tol = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_thr_tol.setText('')
        self.w_thr_tol.setFixedWidth(80)
        self.w_thr_tol.setReadOnly(False)
        self.w_thr_tol.move(180, y)
        self.label7b = QtGui.QLabel('e.g. 6H or 6g', self)
        self.label7b.setFont('Courier')
        self.label7b.move(270, y)
        #
        # Widget thr_rgh
        y += 30
        self.label8a = QtGui.QLabel('Thread roughness', self)
        self.label8a.setFont('Courier')
        self.label8a.move(10, y)
        self.w_thr_rgh = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_thr_rgh.setText('')
        self.w_thr_rgh.setFixedWidth(80)
        self.w_thr_rgh.setReadOnly(False)
        self.w_thr_rgh.move(180, y)
        self.label8b = QtGui.QLabel('e.g. Ra 1.6', self)
        self.label8b.setFont('Courier')
        self.label8b.move(270, y)
        #
        # Widget thr_through
        y += 30
        self.label9a = QtGui.QLabel('Thread through hole/bolt', self)
        self.label9a.setFont('Courier')
        self.label9a.move(10, y)
        self.w_thr_through = QtGui.QCheckBox('(full length)', self)
        self.w_thr_through.setFont('Courier')
        # self.w_thr_through.clicked.connect(self.onCheckbox1) # on, I do not wan connect anything. I read isChecked at the end...
        self.w_thr_through.setChecked(False)
        self.w_thr_through.move(250,y)
        #
        # Widget len
        y += 30
        self.label10a = QtGui.QLabel('Thread length', self)
        self.label10a.setFont('Courier')
        self.label10a.move(10, y)
        self.w_len = QtGui.QLineEdit(self)
        self.w_len.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_len.setText(str(self.s_lthr.getD_drill(name) * 1.5)) # something for start, why not Dx1.5
        self.w_len.setFixedWidth(65)
        self.w_len.setReadOnly(False)
        self.w_len.move(180, y)
        self.label10b = QtGui.QLabel('mm', self)
        self.label10b.setFont('Courier')
        self.label10b.move(270, y)
        #
        # Widget len_tol
        y += 30
        self.label11a = QtGui.QLabel('Length tolerances', self)
        self.label11a.setFont('Courier')
        self.label11a.move(10, y)
        self.w_len_tol = QtGui.QLineEdit(self)
        # no limitation for this input widget
        self.w_len_tol.setText('')
        self.w_len_tol.setFixedWidth(80)
        self.w_len_tol.setReadOnly(False)
        self.w_len_tol.move(180, y)
        self.label11b = QtGui.QLabel('e.g. 0/+2.0', self)
        self.label11b.setFont('Courier')
        self.label11b.move(270, y)
        #
        # y += 30
        # Horizontal line...
        # self.label12a = QtGui.QLabel(self)
        # self.label12a.setFrameShape(QFrame.HLine)
        # self.label12a.setFrameShadow(QFrame.Raised)
        # self.label12a.setMinimumWidth(1)
        # self.label12a.setFixedHeight(3)
        # self.label12a.move(10, y)
        #
        y += 50
        self.label13a = QtGui.QLabel('Use Threads group', self)
        self.label13a.setFont('Courier')
        self.label13a.move(10, y)
        self.w_useGroup = QtGui.QCheckBox('', self)
        self.w_useGroup.setFont('Courier')
        # self.w_useGroup.clicked.connect(self.onCheckbox1) # no, I do not wan connect anything. I read isChecked at the end...
        self.w_useGroup.setChecked(False)
        self.w_useGroup.move(180,y)
        #
        # y += 30
        # Horizontal line...

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
        self.onApply()
        #
        # return None

    def onPopupThreadSel(self, selectedText):
        # user selected some thread type, fill widgets by values from self.s_lthr
        self.s_lstCurrentIndex = self.w_name.currentIndex()
        name = self.s_lthr.getName(self.s_lstCurrentIndex)
        #
        self.w_D_nom.setText(str(self.s_lthr.getD_nominal(name)))
        self.w_pitch.setText(str(self.s_lthr.getpitch(name)))
        self.w_D.setText(str(self.s_lthr.getD(name)))
        self.w_D1.setText(str(self.s_lthr.getD1(name)))
        self.w_d3.setText(str(self.s_lthr.getd3(name)))
        self.w_D_drill.setText(str(self.s_lthr.getD_drill(name)))
        #
        # Rest of the values are independent on thread selection
        #
        del(name)
        # return None

    def onApply(self):
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
        self.useGroup          =  self.w_useGroup.isChecked()
        #
        self.s_obj.recompute()
        #
        # return None

    def onCancel(self):
        self.result = userCancelled
        self.close()
        # return None

    def onOk(self):
        self.result = userOk
        self.onApply()
        self.close()
        # return None



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
        # empty
        return None

    def create():
        """create() -> obj

        Create directional symbol / arrow / cone and return textlink (obj) at it."""
        #
        obj = App.ActiveDocument.addObject('Part::Cone','ThreadOrientation')
        obj.Label = 'ThreadOrientation'
        obj.Radius1 = '1.0 mm'
        obj.Radius2 = '0.0 mm'
        obj.Height  = '2.5 mm'
        #
        # Move it into Active Part - if ActivePart exists
        aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
        if aPart != None:
            aPart.addObject(obj)
        #
        obj.recompute()
        #
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
        return None



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
    # Work-around https://forum.freecad.org/viewtopic.php?t=86029
    # Reset obj_to.AttachmentOfset = point[0,0,0], rotation[0,0,0]
    # Calculate global position of obj_to.Support
    # Calculate global position of obj_to
    # Compare them and if they do not match:
    #     Calculate delta between them - obj_to.Support -> obj_to
    #     Apply the delta to obj_to.AttachmentOffset
    
    
    return None



# +---------------------------------------------------------------+
# |                                                               |
# | Estimate diameter from attachment objects - service functions |
# |                                                               |
# +---------------------------------------------------------------+
def diameter_from_attachment(obj):
    """diameter_from_attachment(obj) -> D

    Try to estimate diameter from obj.Support.
    
    Return Diameter or 0 if is it unsucesfull."""

    D = 0.0
    # https://forum.freecad.org/viewtopic.php?p=743699#p743699
    #     [[Part.getShape(feature, sub, needSubElement = True) for sub in subs] for feature, subs in obj.Support]
    #     edge.Curve.Radius
    for feature, subs in obj.Support:
        for sub in subs:
            # Look just for first circular element and estimate diameter from it. Circle or cylinder.
            if D == 0:
                shp = Part.getShape(feature, sub, needSubElement = True)
                if hasattr(shp, 'Curve'):
                    try:
                        D = 2.0 * shp.Curve.Radius
                    except:
                        pass
                elif hasattr(shp, 'Surface'):
                    try:
                        D = 2.0 * shp.Surface.Radius
                    except:
                        pass
    return D



# /***********************************************************************/
# /                                                                       /
# / useGroupThreads() - Move object obj into Threads group/folder in      /
# /     active part aPart (if active part exists)                         /
# /                                                                       /
# /***********************************************************************/
def useGroupThreads(obj, aPart):
    """
    useGroupThreads() -> None
    
    Move object obj into Threads group/folder in active part aPart (if active part exists)
    """

    groupThreadsName = 'Threads'

    doc = App.ActiveDocument
    groupObj = None
    if aPart == None:
        # There is no active Part, look for group 'Threads' inside active document top level
        for tmpObj in doc.Objects:
            if tmpObj.TypeId == 'App::DocumentObjectGroup':
                if tmpObj.Label == groupThreadsName:
                    # Ok, I have SOME group 'Threads'. But I need top level one, no parents...
                    if len(tmpObj.Parents) == 0:
                        groupObj = tmpObj
                        break
        # If the group 'Threads' does not exists, create a new one
        if groupObj == None:
            groupObj = doc.addObject('App::DocumentObjectGroup','GroupThreads')
            groupObj.Label = groupThreadsName
    else:
        # look for group 'Threads' inside active Part
        for tmpObj in aPart.Group:
            if tmpObj.TypeId == 'App::DocumentObjectGroup':
                if tmpObj.Label == groupThreadsName:
                    groupObj = tmpObj
                    break
        # If the group 'Threads' does not exists, create a new one
        if groupObj == None:
            groupObj = doc.addObject('App::DocumentObjectGroup','GroupThreads')
            groupObj.Label = groupThreadsName
            aPart.addObject(groupObj)
        # Remove object obj from active part
        aPart.removeObject(obj)

    groupObj.addObject(obj)  # Move object obj into the group 'Threads'

    return None

