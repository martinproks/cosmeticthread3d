# -*- coding: utf-8 -*-
#
# MetricFine2nd.py
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



class MetricFine2nd:
    """
    class MetricFine2nd

    Returns object (class) with threads parameters for Metric fine thread
    2nd choice according to ISO 261.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__pitch = []
        self.__D_drill = []

        self.__name.append('M1.1x0.2')
        self.__D_nominal.append(1.1)
        self.__pitch.append(0.2)
        self.__D_drill.append(0.9)

        self.__name.append('M1.4x0.2')
        self.__D_nominal.append(1.4)
        self.__pitch.append(0.2)
        self.__D_drill.append(1.2)

        self.__name.append('M1.8x0.2')
        self.__D_nominal.append(1.8)
        self.__pitch.append(0.2)
        self.__D_drill.append(1.6)

        self.__name.append('M2.2x0.25')
        self.__D_nominal.append(2.2)
        self.__pitch.append(0.25)
        self.__D_drill.append(1.95)

        self.__name.append('M3.5x0.35')
        self.__D_nominal.append(3.5)
        self.__pitch.append(0.35)
        self.__D_drill.append(3.15)

        self.__name.append('M4.5x0.5')
        self.__D_nominal.append(4.5)
        self.__pitch.append(0.5)
        self.__D_drill.append(4)

        self.__name.append('M7x0.75')
        self.__D_nominal.append(7)
        self.__pitch.append(0.75)
        self.__D_drill.append(6.2)

        self.__name.append('M14x1')
        self.__D_nominal.append(14)
        self.__pitch.append(1)
        self.__D_drill.append(13)

        self.__name.append('M14x1.25')
        self.__D_nominal.append(14)
        self.__pitch.append(1.25)
        self.__D_drill.append(12.8)

        self.__name.append('M14x1.5')
        self.__D_nominal.append(14)
        self.__pitch.append(1.5)
        self.__D_drill.append(12.4)

        self.__name.append('M18x1')
        self.__D_nominal.append(18)
        self.__pitch.append(1)
        self.__D_drill.append(17)

        self.__name.append('M18x1.5')
        self.__D_nominal.append(18)
        self.__pitch.append(1.5)
        self.__D_drill.append(16.4)

        self.__name.append('M18x2')
        self.__D_nominal.append(18)
        self.__pitch.append(2)
        self.__D_drill.append(16)

        self.__name.append('M22x1')
        self.__D_nominal.append(22)
        self.__pitch.append(1)
        self.__D_drill.append(21)

        self.__name.append('M22x1.5')
        self.__D_nominal.append(22)
        self.__pitch.append(1.5)
        self.__D_drill.append(20.4)

        self.__name.append('M22x2')
        self.__D_nominal.append(22)
        self.__pitch.append(2)
        self.__D_drill.append(20)

        self.__name.append('M27x1')
        self.__D_nominal.append(27)
        self.__pitch.append(1)
        self.__D_drill.append(26)

        self.__name.append('M27x1.5')
        self.__D_nominal.append(27)
        self.__pitch.append(1.5)
        self.__D_drill.append(25.4)

        self.__name.append('M27x2')
        self.__D_nominal.append(27)
        self.__pitch.append(2)
        self.__D_drill.append(25)

        self.__name.append('M33x1.5')
        self.__D_nominal.append(33)
        self.__pitch.append(1.5)
        self.__D_drill.append(31.4)

        self.__name.append('M33x2')
        self.__D_nominal.append(33)
        self.__pitch.append(2)
        self.__D_drill.append(31)

        self.__name.append('M33x3')
        self.__D_nominal.append(33)
        self.__pitch.append(3)
        self.__D_drill.append(30)

        self.__name.append('M39x1.5')
        self.__D_nominal.append(39)
        self.__pitch.append(1.5)
        self.__D_drill.append(37.4)

        self.__name.append('M39x2')
        self.__D_nominal.append(39)
        self.__pitch.append(2)
        self.__D_drill.append(37)

        self.__name.append('M39x3')
        self.__D_nominal.append(39)
        self.__pitch.append(3)
        self.__D_drill.append(36)

        self.__name.append('M45x1.5')
        self.__D_nominal.append(45)
        self.__pitch.append(1.5)
        self.__D_drill.append(43.5)

        self.__name.append('M45x2')
        self.__D_nominal.append(45)
        self.__pitch.append(2)
        self.__D_drill.append(43)

        self.__name.append('M45x3')
        self.__D_nominal.append(45)
        self.__pitch.append(3)
        self.__D_drill.append(42)

        self.__name.append('M45x4')
        self.__D_nominal.append(45)
        self.__pitch.append(4)
        self.__D_drill.append(41)

        self.__name.append('M52x1.5')
        self.__D_nominal.append(52)
        self.__pitch.append(1.5)
        self.__D_drill.append(50.5)

        self.__name.append('M52x2')
        self.__D_nominal.append(52)
        self.__pitch.append(2)
        self.__D_drill.append(50)

        self.__name.append('M52x3')
        self.__D_nominal.append(52)
        self.__pitch.append(3)
        self.__D_drill.append(49)

        self.__name.append('M52x4')
        self.__D_nominal.append(52)
        self.__pitch.append(4)
        self.__D_drill.append(48)

        self.__name.append('M60x1.5')
        self.__D_nominal.append(60)
        self.__pitch.append(1.5)
        self.__D_drill.append(58.5)

        self.__name.append('M60x2')
        self.__D_nominal.append(60)
        self.__pitch.append(2)
        self.__D_drill.append(58)

        self.__name.append('M60x3')
        self.__D_nominal.append(60)
        self.__pitch.append(3)
        self.__D_drill.append(57)

        self.__name.append('M60x4')
        self.__D_nominal.append(60)
        self.__pitch.append(4)
        self.__D_drill.append(56)

        self.__name.append('M68x1.5')
        self.__D_nominal.append(68)
        self.__pitch.append(1.5)
        self.__D_drill.append(66.5)

        self.__name.append('M68x2')
        self.__D_nominal.append(68)
        self.__pitch.append(2)
        self.__D_drill.append(66)

        self.__name.append('M68x3')
        self.__D_nominal.append(68)
        self.__pitch.append(3)
        self.__D_drill.append(65)

        self.__name.append('M68x4')
        self.__D_nominal.append(68)
        self.__pitch.append(4)
        self.__D_drill.append(64)

        self.__name.append('M76x1.5')
        self.__D_nominal.append(76)
        self.__pitch.append(1.5)
        self.__D_drill.append(74.5)

        self.__name.append('M76x2')
        self.__D_nominal.append(76)
        self.__pitch.append(2)
        self.__D_drill.append(74)

        self.__name.append('M76x3')
        self.__D_nominal.append(76)
        self.__pitch.append(3)
        self.__D_drill.append(73)

        self.__name.append('M76x4')
        self.__D_nominal.append(76)
        self.__pitch.append(4)
        self.__D_drill.append(72)

        self.__name.append('M76x6')
        self.__D_nominal.append(76)
        self.__pitch.append(6)
        self.__D_drill.append(70)

        self.__name.append('M85x2')
        self.__D_nominal.append(85)
        self.__pitch.append(2)
        self.__D_drill.append(83)

        self.__name.append('M85x3')
        self.__D_nominal.append(85)
        self.__pitch.append(3)
        self.__D_drill.append(82)

        self.__name.append('M85x4')
        self.__D_nominal.append(85)
        self.__pitch.append(4)
        self.__D_drill.append(81)

        self.__name.append('M85x6')
        self.__D_nominal.append(85)
        self.__pitch.append(6)
        self.__D_drill.append(79)

        self.__name.append('M95x2')
        self.__D_nominal.append(95)
        self.__pitch.append(2)
        self.__D_drill.append(93)

        self.__name.append('M95x3')
        self.__D_nominal.append(95)
        self.__pitch.append(3)
        self.__D_drill.append(92)

        self.__name.append('M95x4')
        self.__D_nominal.append(95)
        self.__pitch.append(4)
        self.__D_drill.append(91)

        self.__name.append('M95x6')
        self.__D_nominal.append(95)
        self.__pitch.append(6)
        self.__D_drill.append(89)

        self.__name.append('M105x2')
        self.__D_nominal.append(105)
        self.__pitch.append(2)
        self.__D_drill.append(103)

        self.__name.append('M105x3')
        self.__D_nominal.append(105)
        self.__pitch.append(3)
        self.__D_drill.append(102)

        self.__name.append('M105x4')
        self.__D_nominal.append(105)
        self.__pitch.append(4)
        self.__D_drill.append(101)

        self.__name.append('M105x6')
        self.__D_nominal.append(105)
        self.__pitch.append(6)
        self.__D_drill.append(99)

        self.__name.append('M115x2')
        self.__D_nominal.append(115)
        self.__pitch.append(2)
        self.__D_drill.append(113)

        self.__name.append('M115x3')
        self.__D_nominal.append(115)
        self.__pitch.append(3)
        self.__D_drill.append(112)

        self.__name.append('M115x4')
        self.__D_nominal.append(105)
        self.__pitch.append(4)
        self.__D_drill.append(111)

        self.__name.append('M115x6')
        self.__D_nominal.append(105)
        self.__pitch.append(6)
        self.__D_drill.append(109)

        self.__name.append('M120x2')
        self.__D_nominal.append(120)
        self.__pitch.append(2)
        self.__D_drill.append(118)

        self.__name.append('M120x3')
        self.__D_nominal.append(120)
        self.__pitch.append(3)
        self.__D_drill.append(117)

        self.__name.append('M120x4')
        self.__D_nominal.append(120)
        self.__pitch.append(4)
        self.__D_drill.append(116)

        self.__name.append('M120x6')
        self.__D_nominal.append(120)
        self.__pitch.append(6)
        self.__D_drill.append(114)

        self.__name.append('M130x2')
        self.__D_nominal.append(130)
        self.__pitch.append(2)
        self.__D_drill.append(128)

        self.__name.append('M130x3')
        self.__D_nominal.append(130)
        self.__pitch.append(3)
        self.__D_drill.append(127)

        self.__name.append('M130x4')
        self.__D_nominal.append(130)
        self.__pitch.append(4)
        self.__D_drill.append(126)

        self.__name.append('M130x6')
        self.__D_nominal.append(130)
        self.__pitch.append(6)
        self.__D_drill.append(124)

        self.__name.append('M130x8')
        self.__D_nominal.append(130)
        self.__pitch.append(8)
        self.__D_drill.append(121.5)

        self.__name.append('M150x2')
        self.__D_nominal.append(150)
        self.__pitch.append(2)
        self.__D_drill.append(148)

        self.__name.append('M150x3')
        self.__D_nominal.append(150)
        self.__pitch.append(3)
        self.__D_drill.append(147)

        self.__name.append('M150x4')
        self.__D_nominal.append(150)
        self.__pitch.append(4)
        self.__D_drill.append(146)

        self.__name.append('M150x6')
        self.__D_nominal.append(150)
        self.__pitch.append(6)
        self.__D_drill.append(144)

        self.__name.append('M150x8')
        self.__D_nominal.append(150)
        self.__pitch.append(8)
        self.__D_drill.append(141.5)

        self.__name.append('M170x3')
        self.__D_nominal.append(170)
        self.__pitch.append(3)
        self.__D_drill.append(167)

        self.__name.append('M170x4')
        self.__D_nominal.append(170)
        self.__pitch.append(4)
        self.__D_drill.append(166)

        self.__name.append('M170x6')
        self.__D_nominal.append(170)
        self.__pitch.append(6)
        self.__D_drill.append(164)

        self.__name.append('M170x8')
        self.__D_nominal.append(170)
        self.__pitch.append(8)
        self.__D_drill.append(161.5)

        self.__name.append('M190x3')
        self.__D_nominal.append(190)
        self.__pitch.append(3)
        self.__D_drill.append(187)

        self.__name.append('M190x4')
        self.__D_nominal.append(190)
        self.__pitch.append(4)
        self.__D_drill.append(186)

        self.__name.append('M190x6')
        self.__D_nominal.append(190)
        self.__pitch.append(6)
        self.__D_drill.append(184)

        self.__name.append('M190x8')
        self.__D_nominal.append(190)
        self.__pitch.append(8)
        self.__D_drill.append(181.5)

        self.__name.append('M210x3')
        self.__D_nominal.append(210)
        self.__pitch.append(3)
        self.__D_drill.append(207)

        self.__name.append('M210x4')
        self.__D_nominal.append(210)
        self.__pitch.append(4)
        self.__D_drill.append(206)

        self.__name.append('M210x6')
        self.__D_nominal.append(210)
        self.__pitch.append(6)
        self.__D_drill.append(204)

        self.__name.append('M210x8')
        self.__D_nominal.append(210)
        self.__pitch.append(8)
        self.__D_drill.append(201.5)

        self.__name.append('M240x3')
        self.__D_nominal.append(240)
        self.__pitch.append(3)
        self.__D_drill.append(237)

        self.__name.append('M240x4')
        self.__D_nominal.append(240)
        self.__pitch.append(4)
        self.__D_drill.append(236)

        self.__name.append('M240x6')
        self.__D_nominal.append(240)
        self.__pitch.append(6)
        self.__D_drill.append(234)

        self.__name.append('M240x8')
        self.__D_nominal.append(240)
        self.__pitch.append(8)
        self.__D_drill.append(231.5)

        self.__name.append('M260x4')
        self.__D_nominal.append(260)
        self.__pitch.append(4)
        self.__D_drill.append(256)

        self.__name.append('M260x6')
        self.__D_nominal.append(260)
        self.__pitch.append(6)
        self.__D_drill.append(254)

        self.__name.append('M260x8')
        self.__D_nominal.append(260)
        self.__pitch.append(8)
        self.__D_drill.append(251.5)

        self.__name.append('M300x4')
        self.__D_nominal.append(300)
        self.__pitch.append(4)
        self.__D_drill.append(296)

        self.__name.append('M300x6')
        self.__D_nominal.append(300)
        self.__pitch.append(6)
        self.__D_drill.append(294)

        self.__name.append('M300x8')
        self.__D_nominal.append(300)
        self.__pitch.append(8)
        self.__D_drill.append(291.5)

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
