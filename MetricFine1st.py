# -*- coding: utf-8 -*-
#
# MetricFine1st.py
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

__title__ = 'Cosmetic Thread 3D Work Bench'
__author__ = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__ = 'https://github.com/martinproks/cosmeticthread3d'



import math



class MetricFine1st:
    """
    class MetricFine1st

    Returns object (class) with threads parameters for Metric fine thread
    1st choice according to ISO 261.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__pitch = []
        self.__D_drill = []

        self.__name.append('M1x0.2')
        self.__D_nominal.append(1)
        self.__pitch.append(0.2)
        self.__D_drill.append(0.8)

        self.__name.append('M1.2x0.2')
        self.__D_nominal.append(1.2)
        self.__pitch.append(0.2)
        self.__D_drill.append(1)

        self.__name.append('M1.6x0.2')
        self.__D_nominal.append(1.6)
        self.__pitch.append(0.2)
        self.__D_drill.append(1.4)

        self.__name.append('M2x0.25')
        self.__D_nominal.append(2)
        self.__pitch.append(0.25)
        self.__D_drill.append(1.75)

        self.__name.append('M2.5x0.35')
        self.__D_nominal.append(2.5)
        self.__pitch.append(0.35)
        self.__D_drill.append(2.15)

        self.__name.append('M3x0.35')
        self.__D_nominal.append(3)
        self.__pitch.append(0.35)
        self.__D_drill.append(2.65)

        self.__name.append('M4x0.5')
        self.__D_nominal.append(4)
        self.__pitch.append(0.5)
        self.__D_drill.append(3.5)

        self.__name.append('M5x0.5')
        self.__D_nominal.append(5)
        self.__pitch.append(0.5)
        self.__D_drill.append(4.5)

        self.__name.append('M6x0.75')
        self.__D_nominal.append(6)
        self.__pitch.append(0.75)
        self.__D_drill.append(5.2)

        self.__name.append('M8x0.75')
        self.__D_nominal.append(8)
        self.__pitch.append(0.75)
        self.__D_drill.append(7.2)

        self.__name.append('M8x1')
        self.__D_nominal.append(8)
        self.__pitch.append(1)
        self.__D_drill.append(6.95)

        self.__name.append('M10x0.75')
        self.__D_nominal.append(10)
        self.__pitch.append(0.75)
        self.__D_drill.append(9.2)

        self.__name.append('M10x1')
        self.__D_nominal.append(10)
        self.__pitch.append(1)
        self.__D_drill.append(8.95)

        self.__name.append('M10x1.25')
        self.__D_nominal.append(10)
        self.__pitch.append(1.25)
        self.__D_drill.append(8.7)

        self.__name.append('M12x1')
        self.__D_nominal.append(12)
        self.__pitch.append(1)
        self.__D_drill.append(11)

        self.__name.append('M12x1.25')
        self.__D_nominal.append(12)
        self.__pitch.append(1.25)
        self.__D_drill.append(10.7)

        self.__name.append('M12x1.5')
        self.__D_nominal.append(12)
        self.__pitch.append(1.5)
        self.__D_drill.append(10.4)

        self.__name.append('M16x1')
        self.__D_nominal.append(16)
        self.__pitch.append(1)
        self.__D_drill.append(15)

        self.__name.append('M16x1.5')
        self.__D_nominal.append(16)
        self.__pitch.append(1.5)
        self.__D_drill.append(14.4)

        self.__name.append('M20x1')
        self.__D_nominal.append(20)
        self.__pitch.append(1)
        self.__D_drill.append(19)

        self.__name.append('M20x1.5')
        self.__D_nominal.append(20)
        self.__pitch.append(1.5)
        self.__D_drill.append(18.4)

        self.__name.append('M20x2')
        self.__D_nominal.append(20)
        self.__pitch.append(2)
        self.__D_drill.append(18.9)

        self.__name.append('M24x1')
        self.__D_nominal.append(24)
        self.__pitch.append(1)
        self.__D_drill.append(23)

        self.__name.append('M24x1.5')
        self.__D_nominal.append(24)
        self.__pitch.append(1.5)
        self.__D_drill.append(22.5)

        self.__name.append('M24x2')
        self.__D_nominal.append(24)
        self.__pitch.append(2)
        self.__D_drill.append(21.9)

        self.__name.append('M30x1.5')
        self.__D_nominal.append(30)
        self.__pitch.append(1.5)
        self.__D_drill.append(28.5)

        self.__name.append('M30x2')
        self.__D_nominal.append(30)
        self.__pitch.append(2)
        self.__D_drill.append(27.9)

        self.__name.append('M30x3')
        self.__D_nominal.append(30)
        self.__pitch.append(3)
        self.__D_drill.append(26.8)

        self.__name.append('M36x1.5')
        self.__D_nominal.append(36)
        self.__pitch.append(1.5)
        self.__D_drill.append(34.5)

        self.__name.append('M36x2')
        self.__D_nominal.append(36)
        self.__pitch.append(2)
        self.__D_drill.append(34)

        self.__name.append('M36x3')
        self.__D_nominal.append(36)
        self.__pitch.append(3)
        self.__D_drill.append(32.8)

        self.__name.append('M42x1.5')
        self.__D_nominal.append(42)
        self.__pitch.append(1.5)
        self.__D_drill.append(40.5)

        self.__name.append('M42x2')
        self.__D_nominal.append(42)
        self.__pitch.append(2)
        self.__D_drill.append(40)

        self.__name.append('M42x3')
        self.__D_nominal.append(42)
        self.__pitch.append(3)
        self.__D_drill.append(38.8)

        self.__name.append('M42x4')
        self.__D_nominal.append(42)
        self.__pitch.append(4)
        self.__D_drill.append(37.8)

        self.__name.append('M48x1.5')
        self.__D_nominal.append(48)
        self.__pitch.append(1.5)
        self.__D_drill.append(46.5)

        self.__name.append('M48x2')
        self.__D_nominal.append(48)
        self.__pitch.append(2)
        self.__D_drill.append(45.9)

        self.__name.append('M48x3')
        self.__D_nominal.append(48)
        self.__pitch.append(3)
        self.__D_drill.append(44.8)

        self.__name.append('M48x4')
        self.__D_nominal.append(48)
        self.__pitch.append(4)
        self.__D_drill.append(43.8)

        self.__name.append('M56x1.5')
        self.__D_nominal.append(56)
        self.__pitch.append(1.5)
        self.__D_drill.append(54.5)

        self.__name.append('M56x2')
        self.__D_nominal.append(56)
        self.__pitch.append(2)
        self.__D_drill.append(54)

        self.__name.append('M56x3')
        self.__D_nominal.append(56)
        self.__pitch.append(3)
        self.__D_drill.append(52.8)

        self.__name.append('M56x4')
        self.__D_nominal.append(56)
        self.__pitch.append(4)
        self.__D_drill.append(51.8)

        self.__name.append('M64x1.5')
        self.__D_nominal.append(64)
        self.__pitch.append(1.5)
        self.__D_drill.append(62.4)

        self.__name.append('M64x2')
        self.__D_nominal.append(64)
        self.__pitch.append(2)
        self.__D_drill.append(62)

        self.__name.append('M64x3')
        self.__D_nominal.append(64)
        self.__pitch.append(3)
        self.__D_drill.append(60.8)

        self.__name.append('M64x4')
        self.__D_nominal.append(64)
        self.__pitch.append(4)
        self.__D_drill.append(59.8)

        self.__name.append('M72x1.5')
        self.__D_nominal.append(72)
        self.__pitch.append(1.5)
        self.__D_drill.append(70.5)

        self.__name.append('M72x2')
        self.__D_nominal.append(72)
        self.__pitch.append(2)
        self.__D_drill.append(70)

        self.__name.append('M72x3')
        self.__D_nominal.append(72)
        self.__pitch.append(3)
        self.__D_drill.append(68.8)

        self.__name.append('M72x4')
        self.__D_nominal.append(72)
        self.__pitch.append(4)
        self.__D_drill.append(67.8)

        self.__name.append('M72x6')
        self.__D_nominal.append(72)
        self.__pitch.append(6)
        self.__D_drill.append(65.6)

        self.__name.append('M80x1.5')
        self.__D_nominal.append(80)
        self.__pitch.append(1.5)
        self.__D_drill.append(78.4)

        self.__name.append('M80x2')
        self.__D_nominal.append(80)
        self.__pitch.append(2)
        self.__D_drill.append(77.9)

        self.__name.append('M80x3')
        self.__D_nominal.append(80)
        self.__pitch.append(3)
        self.__D_drill.append(76.8)

        self.__name.append('M80x4')
        self.__D_nominal.append(80)
        self.__pitch.append(4)
        self.__D_drill.append(75.8)

        self.__name.append('M80x6')
        self.__D_nominal.append(80)
        self.__pitch.append(6)
        self.__D_drill.append(73.6)

        self.__name.append('M90x2')
        self.__D_nominal.append(90)
        self.__pitch.append(2)
        self.__D_drill.append(87.9)

        self.__name.append('M90x3')
        self.__D_nominal.append(90)
        self.__pitch.append(3)
        self.__D_drill.append(86.8)

        self.__name.append('M90x4')
        self.__D_nominal.append(90)
        self.__pitch.append(4)
        self.__D_drill.append(85.8)

        self.__name.append('M90x6')
        self.__D_nominal.append(90)
        self.__pitch.append(6)
        self.__D_drill.append(83.6)

        self.__name.append('M100x2')
        self.__D_nominal.append(100)
        self.__pitch.append(2)
        self.__D_drill.append(97.9)

        self.__name.append('M100x3')
        self.__D_nominal.append(100)
        self.__pitch.append(3)
        self.__D_drill.append(96.8)

        self.__name.append('M100x4')
        self.__D_nominal.append(100)
        self.__pitch.append(4)
        self.__D_drill.append(95.8)

        self.__name.append('M100x6')
        self.__D_nominal.append(100)
        self.__pitch.append(6)
        self.__D_drill.append(93.6)

        self.__name.append('M110x2')
        self.__D_nominal.append(110)
        self.__pitch.append(2)
        self.__D_drill.append(107.9)

        self.__name.append('M110x3')
        self.__D_nominal.append(110)
        self.__pitch.append(3)
        self.__D_drill.append(106.8)

        self.__name.append('M110x4')
        self.__D_nominal.append(110)
        self.__pitch.append(4)
        self.__D_drill.append(105.8)

        self.__name.append('M110x6')
        self.__D_nominal.append(110)
        self.__pitch.append(6)
        self.__D_drill.append(103.6)

        self.__name.append('M125x2')
        self.__D_nominal.append(125)
        self.__pitch.append(2)
        self.__D_drill.append(122.9)

        self.__name.append('M125x3')
        self.__D_nominal.append(125)
        self.__pitch.append(3)
        self.__D_drill.append(121.8)

        self.__name.append('M125x4')
        self.__D_nominal.append(125)
        self.__pitch.append(4)
        self.__D_drill.append(120.8)

        self.__name.append('M125x6')
        self.__D_nominal.append(125)
        self.__pitch.append(6)
        self.__D_drill.append(118.6)

        self.__name.append('M125x8')
        self.__D_nominal.append(125)
        self.__pitch.append(8)
        self.__D_drill.append(116.5)

        self.__name.append('M140x2')
        self.__D_nominal.append(140)
        self.__pitch.append(2)
        self.__D_drill.append(137.9)

        self.__name.append('M140x3')
        self.__D_nominal.append(140)
        self.__pitch.append(3)
        self.__D_drill.append(136.8)

        self.__name.append('M140x4')
        self.__D_nominal.append(140)
        self.__pitch.append(4)
        self.__D_drill.append(135.8)

        self.__name.append('M140x6')
        self.__D_nominal.append(140)
        self.__pitch.append(6)
        self.__D_drill.append(133.6)

        self.__name.append('M140x8')
        self.__D_nominal.append(140)
        self.__pitch.append(8)
        self.__D_drill.append(131.5)

        self.__name.append('M160x3')
        self.__D_nominal.append(160)
        self.__pitch.append(3)
        self.__D_drill.append(156.8)

        self.__name.append('M160x4')
        self.__D_nominal.append(160)
        self.__pitch.append(4)
        self.__D_drill.append(155.8)

        self.__name.append('M160x6')
        self.__D_nominal.append(160)
        self.__pitch.append(6)
        self.__D_drill.append(153.6)

        self.__name.append('M160x8')
        self.__D_nominal.append(160)
        self.__pitch.append(8)
        self.__D_drill.append(151.5)

        self.__name.append('M180x3')
        self.__D_nominal.append(180)
        self.__pitch.append(3)
        self.__D_drill.append(176.8)

        self.__name.append('M180x4')
        self.__D_nominal.append(180)
        self.__pitch.append(4)
        self.__D_drill.append(175.7)

        self.__name.append('M180x6')
        self.__D_nominal.append(180)
        self.__pitch.append(6)
        self.__D_drill.append(173.6)

        self.__name.append('M180x8')
        self.__D_nominal.append(180)
        self.__pitch.append(8)
        self.__D_drill.append(171.5)

        self.__name.append('M200x3')
        self.__D_nominal.append(200)
        self.__pitch.append(3)
        self.__D_drill.append(196.8)

        self.__name.append('M200x4')
        self.__D_nominal.append(200)
        self.__pitch.append(4)
        self.__D_drill.append(195.8)

        self.__name.append('M200x6')
        self.__D_nominal.append(200)
        self.__pitch.append(6)
        self.__D_drill.append(193.6)

        self.__name.append('M200x8')
        self.__D_nominal.append(200)
        self.__pitch.append(8)
        self.__D_drill.append(191.5)

        self.__name.append('M220x3')
        self.__D_nominal.append(220)
        self.__pitch.append(3)
        self.__D_drill.append(216.8)

        self.__name.append('M220x4')
        self.__D_nominal.append(220)
        self.__pitch.append(4)
        self.__D_drill.append(215.8)

        self.__name.append('M220x6')
        self.__D_nominal.append(220)
        self.__pitch.append(6)
        self.__D_drill.append(213.6)

        self.__name.append('M220x8')
        self.__D_nominal.append(220)
        self.__pitch.append(8)
        self.__D_drill.append(211.5)

        self.__name.append('M250x3')
        self.__D_nominal.append(250)
        self.__pitch.append(3)
        self.__D_drill.append(246.8)

        self.__name.append('M250x4')
        self.__D_nominal.append(250)
        self.__pitch.append(4)
        self.__D_drill.append(245.8)

        self.__name.append('M250x6')
        self.__D_nominal.append(250)
        self.__pitch.append(6)
        self.__D_drill.append(243.6)

        self.__name.append('M250x8')
        self.__D_nominal.append(250)
        self.__pitch.append(8)
        self.__D_drill.append(241.5)

        self.__name.append('M280x4')
        self.__D_nominal.append(280)
        self.__pitch.append(4)
        self.__D_drill.append(275.8)

        self.__name.append('M280x6')
        self.__D_nominal.append(280)
        self.__pitch.append(6)
        self.__D_drill.append(273.6)

        self.__name.append('M280x8')
        self.__D_nominal.append(280)
        self.__pitch.append(8)
        self.__D_drill.append(271.5)

    def getLstNames(self):
        """
        getLstNames() -> list of threads names
        """
        return self.__name

    def getName(self, i):
        """
        getName(i) -> name

        name = string or None
        """
        x = None
        if i < len(self.__name):
            x = self.__name[i]
        return x

    def getD_nominal(self, ThrName):
        """
        getD_nominal(ThrName) -> D_nominal
        """
        x = 0.0
        i = 0
        while i < len(self.__name):
            if ThrName == self.__name[i]:
                x = self.__D_nominal[i]
                break
            i += 1
        return x

    def getpitch(self, ThrName):
        """
        getpitch(ThrName) -> pitch
        """
        x = 0.0
        i = 0
        while i < len(self.__name):
            if ThrName == self.__name[i]:
                x = self.__pitch[i]
                break
            i += 1
        return x

    def getTPI(self, ThrName):
        """
        getTPI(ThrName) -> TPI
        """
        x = self.getpitch(ThrName)
        x = round(25.4 / x, 3) if x > 0.0 else 0.0
        return x

    def getD(self, ThrName):
        """
        getD(ThrName) -> D
        """
        x = 0.0
        i = 0
        while i < len(self.__name):
            if ThrName == self.__name[i]:
                # in the case of metric thread coarse is D equal to D_nominal
                x = self.__D_nominal[i]
                break
            i += 1
        return x

    def getD1(self, ThrName):
        """
        getD1(ThrName) -> D1
        """
        x = 0.0
        Dtmp = self.getD(ThrName)
        ptmp = self.getpitch(ThrName)
        H = ptmp * 0.5 * math.sqrt(3)
        x = round(Dtmp - 2*H*(5/8), 3)
        return x

    def getd3(self, ThrName):
        """
        getd3(ThrName) -> d3
        """
        x = 0.0
        Dtmp = self.getD(ThrName)
        ptmp = self.getpitch(ThrName)
        H = ptmp * 0.5 * math.sqrt(3)
        x = round(Dtmp - 2*H*(1 - (1/6) - (1/8)), 3)
        return x
    
    def getD_drill(self, ThrName):
        """
        getD_drill(ThrName) -> D_drill
        """
        x = 0.0
        i = 0
        while i < len(self.__name):
            if ThrName == self.__name[i]:
                x = self.__D_drill[i]
                break
            i += 1
        return x
