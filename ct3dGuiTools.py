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

import os
from PySide import QtCore, QtGui
from PySide.QtGui import QFrame
import FreeCAD as App
import FreeCADGui as Gui
import Part

import MetricCoarse1st
import MetricCoarse2nd
import MetricCoarse3th
import MetricFine1st
import MetricFine2nd
import MetricFine3th
import MetricEle
import Gthread
import UNC
import UNF
import UNEF
import BSW
import BSF

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



# +-----------------------------------------------------+
# |                                                     |
# |      UI constants - results of modal dialogs        |
# |                                                     |
# +-----------------------------------------------------+
userCancelled = 'Cancel button pressed'
userOk = 'OK button pressed'



# +--------------------------------------------------------+
# |                                                        |
# | get_module_path() - internal function                  |
# |                                                        |
# +--------------------------------------------------------+
def get_module_path():
    """
    Returns the current module path.
    """
    return os.path.dirname(__file__)



# +-------------------------------------------------------+
# |                                                       |
# | UI for thread dimensions and parameters selection     |
# |                                                       |
# +-------------------------------------------------------+
class ct3d_threadUI(QtGui.QDialog):
    """
    UI for thread parameters definition - common for all threads.
    """
    # https://wiki.freecad.org/PySide_Intermediate_Examples
    # https://doc.qt.io/qt-5/qtwidgets-module.html
    # https://doc.qt.io/qt-5/qcheckbox.html
    # https://doc.qt.io/qt-5/qcombobox.html
    # https://doc.qt.io/qt-5/qlineedit.html
    def __init__(self, obj, Dobj):
        """
        __init__(obj, Dobj)

        Create UI for thread dimensions and parameters definition
        and copy the values to the obj properties.

        obj  - [text link]  Object with thread parameters...
        Dobj - [mm]         Hole or shaft diameter for preliminary
                            thread estimation.
        """
        # the obj and lst_threads pointers are copied to internal variables
        # accessible from other methods
        self.__obj = obj
        self.__Dobj = Dobj
        # Thread type initialization
        self.__tOT = [] # typesOfThreads
        self.__tOT.append('Metric Coarse thread')
        # MetricCoarse1st.MetricCoarse1st()
        self.__tOT.append('Metric Coarse thread 2nd choice')
        # MetricCoarse2nd.MetricCoarse2nd()
        self.__tOT.append('Metric Coarse thread 3th choice')
        # MetricCoarse3th.MetricCoarse3th()
        self.__tOT.append('Metric Fine thread')
        # MetricFine.MetricFine()
        self.__tOT.append('Metric Fine thread 2nd choice')
        # MetricFine2nd.MetricFine2nd()
        self.__tOT.append('Metric Fine thread 3th choice')
        # MetricFine3th.MetricFine3th()
        self.__tOT.append('Metric Electrical thread')
        # MetricEle.MetricEle() # according to EN 60423 selection
        self.__tOT.append('G - Pipe Parallel Thread (BSPP)')
        # Gthread.Gthread()
        self.__tOT.append('UNC - Unified Thread Standard Coarse')
        # UNC.UNC()
        self.__tOT.append('UNF - Unified Thread Standard Fine')
        # UNF.UNF()
        self.__tOT.append('UNEF - Unified Thread Standard Extra fine')
        # UNEF.UNEF()
        self.__tOT.append('BSW - British Standard Whitworth')
        # BSW.BSW()
        self.__tOT.append('BSF - British Standard Fine')
        # BSF.BSF()
        self.__tOT_index = 0
        self.__lthr = MetricCoarse1st.MetricCoarse1st()
        self.__lthr_index = 0
        # Use group Threads? This value is not internal.
        self.useGroup = True

        # Estimate/guess thread according the best matching Dobj
        self.__lthr_index = threadIFromDobj(self.__Dobj, \
                                            self.__obj, \
                                            self.__lthr)
        # UI itself...
        super(ct3d_threadUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.result = userCancelled
        name = self.__lthr.getName(self.__lthr_index)
        # create our window
        # define window  xLoc,yLoc,xDim,yDim
        self.setGeometry(250, 250, 400, 540)
        self.setWindowTitle('Cosmetic Thread 3D')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        # Type of thread selection
        y = 10
        self.w_tOT = QtGui.QComboBox(self)
        # self.w_tOT.setSizeAdjustPolicy(???)
        self.w_tOT.addItems(self.__tOT)
        self.w_tOT.setCurrentIndex(self.__tOT_index)
        self.w_tOT.activated[str].connect(self.onPopupTypeOfThread)
        self.w_tOT.move(10, y)

        # Widget name (it means Thread selection)
        y += 30
        self.label0a = QtGui.QLabel('Thread selected', self)
        self.label0a.setFont('Courier')
        self.label0a.move(10, y)
        self.w_lthr = QtGui.QComboBox(self)
        # self.w_lthr.setSizeAdjustPolicy(???)
        self.w_lthr.addItems(self.__lthr.getLstNames())
        self.w_lthr.setCurrentIndex(self.__lthr_index)
        self.w_lthr.activated[str].connect(self.onPopupThreadSel)
        self.w_lthr.move(180, y)

        # Widget D_nominal
        y += 30
        self.label1a = QtGui.QLabel('D nominal', self)
        self.label1a.setFont('Courier')
        self.label1a.move(30, y)
        self.w_D_nom = QtGui.QLineEdit(self)
        self.w_D_nom.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D_nom.setText(str(self.__lthr.getD_nominal(name)))
        self.w_D_nom.setFixedWidth(65)
        self.w_D_nom.setReadOnly(True)
        self.w_D_nom.move(210, y)
        self.label1b = QtGui.QLabel('mm', self)
        self.label1b.setFont('Courier')
        self.label1b.move(290, y)

        # Widget pitch
        y += 30
        self.label2a = QtGui.QLabel('Pitch', self)
        self.label2a.setFont('Courier')
        self.label2a.move(30, y)
        self.w_pitch = QtGui.QLineEdit(self)
        self.w_pitch.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_pitch.setText(str(self.__lthr.getpitch(name)))
        self.w_pitch.setFixedWidth(65)
        self.w_pitch.setReadOnly(True)
        self.w_pitch.move(210, y)
        self.label2b = QtGui.QLabel('mm', self)
        self.label2b.setFont('Courier')
        self.label2b.move(290, y)

        # Widget TPI
        y += 30
        self.label2aa = QtGui.QLabel('TPI', self)
        self.label2aa.setFont('Courier')
        self.label2aa.move(30, y)
        self.w_TPI = QtGui.QLineEdit(self)
        self.w_TPI.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_TPI.setText(str(self.__lthr.getTPI(name)))
        self.w_TPI.setFixedWidth(65)
        self.w_TPI.setReadOnly(True)
        self.w_TPI.move(210, y)
        self.label2ba = QtGui.QLabel('Thread Per Inch', self)
        self.label2ba.setFont('Courier')
        self.label2ba.move(290, y)

        # Widget D
        y += 30
        self.label3a = QtGui.QLabel('D', self)
        self.label3a.setFont('Courier')
        self.label3a.move(30, y)
        self.w_D = QtGui.QLineEdit(self)
        self.w_D.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D.setText(str(self.__lthr.getD(name)))
        self.w_D.setFixedWidth(65)
        self.w_D.setReadOnly(True)
        self.w_D.move(210, y)
        self.label3b = QtGui.QLabel('mm', self)
        self.label3b.setFont('Courier')
        self.label3b.move(290, y)

        # Widget D1
        y += 30
        self.label4a = QtGui.QLabel('D1', self)
        self.label4a.setFont('Courier')
        self.label4a.move(30, y)
        self.w_D1 = QtGui.QLineEdit(self)
        self.w_D1.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D1.setText(str(self.__lthr.getD1(name)))
        self.w_D1.setFixedWidth(65)
        self.w_D1.setReadOnly(True)
        self.w_D1.move(210, y)
        self.label4b = QtGui.QLabel('mm', self)
        self.label4b.setFont('Courier')
        self.label4b.move(290, y)

        # Widget d3
        y += 30
        self.label5a = QtGui.QLabel('d3', self)
        self.label5a.setFont('Courier')
        self.label5a.move(30, y)
        self.w_d3 = QtGui.QLineEdit(self)
        self.w_d3.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_d3.setText(str(self.__lthr.getd3(name)))
        self.w_d3.setFixedWidth(65)
        self.w_d3.setReadOnly(True)
        self.w_d3.move(210, y)
        self.label5b = QtGui.QLabel('mm', self)
        self.label5b.setFont('Courier')
        self.label5b.move(290, y)

        # Widget D_drill
        y += 30
        self.label6a = QtGui.QLabel('D drill recommended', self)
        self.label6a.setFont('Courier')
        self.label6a.move(30, y)
        self.w_D_drill = QtGui.QLineEdit(self)
        self.w_D_drill.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_D_drill.setText(str(self.__lthr.getD_drill(name)))
        self.w_D_drill.setFixedWidth(65)
        self.w_D_drill.setReadOnly(True)
        self.w_D_drill.move(210, y)
        self.label6b = QtGui.QLabel('mm', self)
        self.label6b.setFont('Courier')
        self.label6b.move(290, y)

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

        # Widget thr_through
        y += 30
        self.label9a = QtGui.QLabel('Thread through hole/bolt', self)
        self.label9a.setFont('Courier')
        self.label9a.move(10, y)
        self.w_thr_through = QtGui.QCheckBox('(full length)', self)
        self.w_thr_through.setFont('Courier')
        # self.w_thr_through.clicked.connect(self.onCheckbox1) # I do not
        # want connect anything. I read isChecked on apply...
        self.w_thr_through.setChecked(False)
        self.w_thr_through.move(250, y)

        # Widget len
        y += 30
        self.label10a = QtGui.QLabel('Thread length', self)
        self.label10a.setFont('Courier')
        self.label10a.move(10, y)
        self.w_len = QtGui.QLineEdit(self)
        self.w_len.setValidator(QtGui.QDoubleValidator(0.999, 999.999, 3))
        self.w_len.setText(str(self.__lthr.getD_drill(name) * 1.5))
        # something for start, why not Dx1.5
        self.w_len.setFixedWidth(65)
        self.w_len.setReadOnly(False)
        self.w_len.move(180, y)
        self.label10b = QtGui.QLabel('mm', self)
        self.label10b.setFont('Courier')
        self.label10b.move(270, y)

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

        y += 50
        self.label13a = QtGui.QLabel('Use Threads group', self)
        self.label13a.setFont('Courier')
        self.label13a.move(10, y)
        self.w_useGroup = QtGui.QCheckBox('', self)
        self.w_useGroup.setFont('Courier')
        # self.w_useGroup.clicked.connect(self.onCheckbox1) # I do not
        # want connect anything. I read isChecked on apply...
        self.w_useGroup.setChecked(self.useGroup)
        self.w_useGroup.move(180, y)

        # apply button
        y += 50
        applyButton = QtGui.QPushButton('Apply', self)
        applyButton.clicked.connect(self.onApply)
        applyButton.setAutoDefault(True)
        applyButton.move(40, y)

        # cancel button
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.onCancel)
        cancelButton.setAutoDefault(True)
        cancelButton.move(150, y)

        # OK button
        okButton = QtGui.QPushButton('OK', self)
        okButton.clicked.connect(self.onOk)
        okButton.move(260, y)
        self.show()
        self.onApply()

    def onPopupTypeOfThread(self, selectedText):
        self.__tOT_index = self.w_tOT.currentIndex()
        tOT_name = self.__tOT[self.__tOT_index]

        if tOT_name == 'Metric Coarse thread':
            self.__lthr = MetricCoarse1st.MetricCoarse1st()
        elif tOT_name == 'Metric Coarse thread 2nd choice':
            self.__lthr = MetricCoarse2nd.MetricCoarse2nd()
        elif tOT_name == 'Metric Coarse thread 3th choice':
            self.__lthr = MetricCoarse3th.MetricCoarse3th()
        elif tOT_name == 'Metric Fine thread':
            self.__lthr = MetricFine1st.MetricFine1st()
        elif tOT_name == 'Metric Fine thread 2nd choice':
            self.__lthr = MetricFine2nd.MetricFine2nd()
        elif tOT_name == 'Metric Fine thread 3th choice':
            self.__lthr = MetricFine3th.MetricFine3th()
        elif tOT_name == 'Metric Electrical thread':
            self.__lthr = MetricEle.MetricEle()
        elif tOT_name == 'G - Pipe Parallel Thread (BSPP)':
            self.__lthr = Gthread.Gthread()
        elif tOT_name == 'UNC - Unified Thread Standard Coarse':
            self.__lthr = UNC.UNC()
        elif tOT_name == 'UNF - Unified Thread Standard Fine':
            self.__lthr = UNF.UNF()
        elif tOT_name == 'UNEF - Unified Thread Standard Extra fine':
            self.__lthr = UNEF.UNEF()
        elif tOT_name == 'BSW - British Standard Whitworth':
            self.__lthr = BSW.BSW()
        elif tOT_name == 'BSF - British Standard Fine':
            self.__lthr = BSF.BSF()
        else:
            App.Console.PrintMessage('*** FIXME *** ct3dGouiTools.ct3d_threadUI.onPopupTypeOfThread() - selected thread type is not implemented\n')
            self.__tOT_index = 0
            self.w_tOT.setCurrentIndex(self.__tOT_index)
            self.__lthr = MetricCoarse1st.MetricCoarse1st()
        self.w_lthr.clear()
        self.w_lthr.addItems(self.__lthr.getLstNames())
        i = threadIFromDobj(self.__Dobj, self.__obj, self.__lthr)
        self.w_lthr.setCurrentIndex(i)
        self.onPopupThreadSel(self.__lthr.getName(i))
        self.onApply()
        del i, tOT_name

    def onPopupThreadSel(self, selectedText):
        # user selected some thread type, fill widgets by self.__lthr values
        self.__lthr_index = self.w_lthr.currentIndex()
        name = self.__lthr.getName(self.__lthr_index)
        self.w_D_nom.setText(str(self.__lthr.getD_nominal(name)))
        self.w_pitch.setText(str(self.__lthr.getpitch(name)))
        self.w_TPI.setText(str(self.__lthr.getTPI(name)))
        self.w_D.setText(str(self.__lthr.getD(name)))
        self.w_D1.setText(str(self.__lthr.getD1(name)))
        self.w_d3.setText(str(self.__lthr.getd3(name)))
        self.w_D_drill.setText(str(self.__lthr.getD_drill(name)))
        # Rest of the values are independent on thread selection
        del name

    def onApply(self):
        self.__obj.Label = self.w_lthr.currentText()
        self.__obj.Description = self.w_lthr.currentText()
        self.__obj.D_nominal = float(self.w_D_nom.text())
        self.__obj.pitch = float(self.w_pitch.text())
        self.__obj.TPI = float(self.w_TPI.text())
        self.__obj.D = float(self.w_D.text())
        if hasattr(self.__obj, 'D1'): # internal thread
            self.__obj.D1 = float(self.w_D1.text())
        if hasattr(self.__obj, 'd3'): # external thread
            self.__obj.d3 = float(self.w_d3.text())
        if hasattr(self.__obj, 'D_drill'):  # internal thread
            self.__obj.D_drill = float(self.w_D_drill.text())
        self.__obj.tolerance = self.w_thr_tol.displayText() # do not remove
        # white chars - displayText
        self.__obj.roughness = self.w_thr_rgh.displayText() # do not remove
        # white chars - displayText
        self.__obj.length_through = self.w_thr_through.isChecked()
        self.__obj.length = float(self.w_len.text())
        self.__obj.length_tol = self.w_len_tol.displayText() # do not remove
        # white chars - displayText
        self.useGroup = self.w_useGroup.isChecked()
        self.__obj.recompute()

    def onCancel(self):
        self.result = userCancelled
        self.close()

    def onOk(self):
        self.onApply()
        self.result = userOk
        self.close()



# +-------------------------------------------------------+
# |                                                       |
# | Arrow / direction symbol - internal class / functions |
# | Part version of the arrow                             |
# |                                                       |
# +-------------------------------------------------------+
class arrowP_direction():
    """
    Arrow / direction symbol (Part version).
    service class for tools for create/manipulate it.
    """

    def __init__(self):
        """
        __init__() - internal initialization function.
        """

    def create():
        """
        create() -> obj

        Create directional symbol / arrow / cone and return textlink
        (obj) at it.
        """
        obj = App.ActiveDocument.addObject('Part::Cone', 'ThreadOrientation')
        obj.Label = 'ThreadOrientation'
        obj.Radius1 = '1.0 mm'
        obj.Radius2 = '0.0 mm'
        obj.Height = '2.5 mm'
        # Move it into Active Part - if ActivePart exists
        aPart = Gui.ActiveDocument.ActiveView.getActiveObject('part')
        if aPart != None:
            aPart.addObject(obj)
        obj.recompute()
        return obj

    def scale(obj, hole_diameter):
        """
        scale(obj, hole_diameter)

        Scale directional symbol / arrow / cone (textlink obj) to be visually
        adequate to hole diameter.
        """
        obj.Radius1 = 0.25 * hole_diameter
        obj.Radius2 = 0.0
        obj.Height = 2.5 * obj.Radius1
        obj.recompute()



# +-------------------------------------------------------+
# |                                                       |
# | Arrow / direction symbol - internal class / functions |
# | PartDesign version of the arrow                       |
# |                                                       |
# +-------------------------------------------------------+
class arrowPD_direction():
    """
    Arrow / direction symbol (PartDesign version).
    service class for tools for create/manipulate it.
    """

    def __init__(self):
        """
        __init__() - internal initialization function.
        """

    def create():
        """
        create() -> obj

        Create directional symbol / arrow / cone and return textlink
        (obj) at it.
        """
        body = Gui.ActiveDocument.ActiveView.getActiveObject("pdbody")
        obj = body.newObject('PartDesign::CoordinateSystem','Local_CS')
        obj.Label = 'ThreadOrientation'
        obj.recompute()
        return obj

    def scale(obj, hole_diameter):
        """
        scale(obj, hole_diameter)

        Scale directional symbol / arrow / cone (textlink obj) to be visually
        adequate to hole diameter.
        """
        # emnpty, LCS does not need scale...


# +-------------------------------------------------------+
# |                                                       |
# | Copy attachent() - service functions                  |
# |                                                       |
# +-------------------------------------------------------+
def copy_attachment(obj_from, obj_to):
    """
    copy_attachment(obj_from, obj_to)

    Internal function.
    """
    #
    obj_to.AttachmentOffset = obj_from.AttachmentOffset
    obj_to.MapReversed = obj_from.MapReversed
    # They changed Support to AttachmentSupport in 0.22.devel:
    if int(App.Version()[1]) >= 22:
        obj_to.AttachmentSupport = obj_from.AttachmentSupport
    else:
        obj_to.Support = obj_from.Support
    obj_to.MapPathParameter = obj_from.MapPathParameter
    obj_to.MapMode = obj_from.MapMode
    #
    # Work-around https://forum.freecad.org/viewtopic.php?t=86029
    # Reset obj_to.AttachmentOfset = point[0,0,0], rotation[0,0,0]
    # Calculate global position of obj_to.Support
    # Calculate global position of obj_to
    # Compare them and if they do not match:
    #     Calculate delta between them - obj_to.Support -> obj_to
    #     Apply the delta to obj_to.AttachmentOffset



# +---------------------------------------------------------------+
# |                                                               |
# | Estimate diameter from attachment objects - service functions |
# |                                                               |
# +---------------------------------------------------------------+
def diameter_from_attachment(obj):
    """
    diameter_from_attachment(obj) -> D

    Try to estimate diameter from obj.Support.

    Return Diameter or 0 if is it unsucesfull.
    """

    D = 0.0
    # https://forum.freecad.org/viewtopic.php?p=743699#p743699
    #     [[Part.getShape(feature, sub, needSubElement = True) \
    #          for sub in subs] for feature, subs in obj.Support]
    #     edge.Curve.Radius
    # They changed Support to AttachmentSupport in 0.22.devel:
    if int(App.Version()[1]) >= 22:
        obj_AS = obj.AttachmentSupport
    else:
        obj_AS = obj.Support
    for feature, subs in obj_AS:
        for sub in subs:
            # Look just for first circular element and estimate diameter
            # from it. Circle or cylinder.
            if D == 0:
                shp = Part.getShape(feature, sub, needSubElement=True)
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
# / threadIFromDobj() - Estimate best fitting thread name/counter 'i'     /
# /     from Dobj and list of threads                                     /
# /                                                                       /
# /***********************************************************************/
def threadIFromDobj(Dobj, obj, lthr):
    """
    threadIFromDobj(Dobj, obj, list_of_thread_class) -> int

    Estimate the best fitting thread index from Dobj and list_of_thread_class.
    Returns int >= 0
    """
    CurrentIndex = 0
    n = len(lthr.getLstNames())
    if hasattr(obj, 'D1'):  # internal thread
        i = 0
        Ddrill = lthr.getD_drill(lthr.getName(i))
        # deviance is relative value based on D_drill
        deviance = abs(Ddrill - Dobj) / Ddrill
        while i < n-1:
            Ddrill = lthr.getD_drill(lthr.getName(i+1))
             # deviance_next is relative value based on D_drill
            deviance_next = abs(Ddrill - Dobj) / Ddrill
            if deviance > deviance_next:
                # while the deviance is descending (deviance > deviance_next),
                # [i+1] is matching better than [i].
                CurrentIndex = i+1
            else:  # STOP, the [i] matched better than [i+1]
                i = n-2 # this will force to stop
            i += 1 # move i for nex turn...
            deviance = deviance_next # and actualize appropriate deviance
        del Ddrill
    if hasattr(obj, 'd3'):  # external thread
        i = 0
        Dtmp = lthr.getD(lthr.getName(i))
        deviance = abs(Dtmp - Dobj) / Dtmp # relative value based on D
        while i < n-1:
            Dtmp = lthr.getD(lthr.getName(i+1))
             # deviance_next is relative value based on D
            deviance_next = abs(Dtmp - Dobj) / Dtmp
            if deviance > deviance_next:
                # while the deviance is descending, [i+1] is matching
                # better than [i].
                CurrentIndex = i+1
            else:  # STOP, the [i] matched better than [i+1]
                i = n-2 # this will force to stop
            i += 1 # move i for nex turn...
            deviance = deviance_next # and actualize appropriate deviance
        del Dtmp
    del n, i, deviance, deviance_next
    return CurrentIndex



# /***********************************************************************/
# /                                                                       /
# / useGroupThreads() - Move object obj into Threads group/folder in      /
# /     active part aPart (if active part exists)                         /
# /                                                                       /
# /***********************************************************************/
def useGroupThreads(obj, aPart):
    """
    useGroupThreads() -> None

    Move object obj into Threads group/folder in active part aPart
    (if active part exists)
    """

    groupThreadsName = 'Threads'

    doc = App.ActiveDocument
    groupObj = None
    if aPart is None:
        # There is no active Part, look for group 'Threads' inside
        # active document top level
        for tmpObj in doc.Objects:
            if tmpObj.TypeId == 'App::DocumentObjectGroup':
                if tmpObj.Label == groupThreadsName:
                    # Ok, I have SOME group 'Threads'.
                    # But I need top level one, no parents...
                    if len(tmpObj.Parents) == 0:
                        groupObj = tmpObj
                        break
        # If the group 'Threads' does not exists, create a new one
        if groupObj is None:
            groupObj = doc.addObject('App::DocumentObjectGroup', \
                                     'GroupThreads')
            groupObj.Label = groupThreadsName
    else:
        # look for group 'Threads' inside active Part
        for tmpObj in aPart.Group:
            if tmpObj.TypeId == 'App::DocumentObjectGroup':
                if tmpObj.Label == groupThreadsName:
                    groupObj = tmpObj
                    break
        # If the group 'Threads' does not exists, create a new one
        if groupObj is None:
            groupObj = doc.addObject('App::DocumentObjectGroup', \
                                     'GroupThreads')
            groupObj.Label = groupThreadsName
            aPart.addObject(groupObj)
        # Remove object obj from active part
        aPart.removeObject(obj)

    groupObj.addObject(obj) # Move object obj into the group 'Threads'
