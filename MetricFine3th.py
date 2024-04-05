# -*- coding: utf-8 -*-
#
# MetricFine3th.py
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



class MetricFine3th:
    """
    class MetricFine3th

    Returns object (class) with threads parameters for Metric fine thread
    3th choice according to ISO 261.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__pitch = []
        self.__D_drill = []

        self.__name.append('M5.5x0.5')
        self.__D_nominal.append(5.5)
        self.__pitch.append(0.5)
        self.__D_drill.append(5)

        self.__name.append('M9x0.75')
        self.__D_nominal.append(9)
        self.__pitch.append(0.75)
        self.__D_drill.append(8.2)

        self.__name.append('M9x1')
        self.__D_nominal.append(9)
        self.__pitch.append(1)
        self.__D_drill.append(7.95)

        self.__name.append('M11x0.75')
        self.__D_nominal.append(11)
        self.__pitch.append(0.75)
        self.__D_drill.append(10.2)

        self.__name.append('M11x1')
        self.__D_nominal.append(11)
        self.__pitch.append(1)
        self.__D_drill.append(9.95)

        self.__name.append('M15x1')
        self.__D_nominal.append(15)
        self.__pitch.append(1)
        self.__D_drill.append(13.95)

        self.__name.append('M15x1.5')
        self.__D_nominal.append(15)
        self.__pitch.append(1.5)
        self.__D_drill.append(13.5)

        self.__name.append('M17x1')
        self.__D_nominal.append(17)
        self.__pitch.append(1)
        self.__D_drill.append(16)

        self.__name.append('M17x1.5')
        self.__D_nominal.append(17)
        self.__pitch.append(1.5)
        self.__D_drill.append(15.5)

        self.__name.append('M25x1')
        self.__D_nominal.append(25)
        self.__pitch.append(1)
        self.__D_drill.append(24)

        self.__name.append('M25x1.5')
        self.__D_nominal.append(25)
        self.__pitch.append(1.5)
        self.__D_drill.append(23.5)

        self.__name.append('M25x2')
        self.__D_nominal.append(25)
        self.__pitch.append(2)
        self.__D_drill.append(23)

        self.__name.append('M26x1.5')
        self.__D_nominal.append(26)
        self.__pitch.append(1.5)
        self.__D_drill.append(24.5)

        self.__name.append('M28x1')
        self.__D_nominal.append(28)
        self.__pitch.append(1)
        self.__D_drill.append(27)

        self.__name.append('M28x1.5')
        self.__D_nominal.append(28)
        self.__pitch.append(1.5)
        self.__D_drill.append(26.5)

        self.__name.append('M28x2')
        self.__D_nominal.append(28)
        self.__pitch.append(2)
        self.__D_drill.append(26)

        self.__name.append('M32x1.5')
        self.__D_nominal.append(32)
        self.__pitch.append(1.5)
        self.__D_drill.append(30.5)

        self.__name.append('M32x2')
        self.__D_nominal.append(32)
        self.__pitch.append(2)
        self.__D_drill.append(30)

        self.__name.append('M35x1.5')
        self.__D_nominal.append(35)
        self.__pitch.append(1.5)
        self.__D_drill.append(33.5)

        self.__name.append('M38x1.5')
        self.__D_nominal.append(38)
        self.__pitch.append(1.5)
        self.__D_drill.append(36.5)

        self.__name.append('M40x1.5')
        self.__D_nominal.append(40)
        self.__pitch.append(1.5)
        self.__D_drill.append(38.5)

        self.__name.append('M40x2')
        self.__D_nominal.append(40)
        self.__pitch.append(2)
        self.__D_drill.append(38)

        self.__name.append('M40x3')
        self.__D_nominal.append(40)
        self.__pitch.append(3)
        self.__D_drill.append(37)

        self.__name.append('M50x1.5')
        self.__D_nominal.append(50)
        self.__pitch.append(1.5)
        self.__D_drill.append(48.5)

        self.__name.append('M50x2')
        self.__D_nominal.append(50)
        self.__pitch.append(2)
        self.__D_drill.append(48)

        self.__name.append('M50x3')
        self.__D_nominal.append(50)
        self.__pitch.append(3)
        self.__D_drill.append(47)

        self.__name.append('M55x1.5')
        self.__D_nominal.append(55)
        self.__pitch.append(1.5)
        self.__D_drill.append(53.5)

        self.__name.append('M55x2')
        self.__D_nominal.append(55)
        self.__pitch.append(2)
        self.__D_drill.append(53)

        self.__name.append('M55x3')
        self.__D_nominal.append(55)
        self.__pitch.append(3)
        self.__D_drill.append(52)

        self.__name.append('M55x4')
        self.__D_nominal.append(55)
        self.__pitch.append(4)
        self.__D_drill.append(51)

        self.__name.append('M58x1.5')
        self.__D_nominal.append(58)
        self.__pitch.append(1.5)
        self.__D_drill.append(56.5)

        self.__name.append('M58x2')
        self.__D_nominal.append(58)
        self.__pitch.append(2)
        self.__D_drill.append(56)

        self.__name.append('M58x3')
        self.__D_nominal.append(58)
        self.__pitch.append(3)
        self.__D_drill.append(55)

        self.__name.append('M58x4')
        self.__D_nominal.append(58)
        self.__pitch.append(4)
        self.__D_drill.append(54)

        self.__name.append('M62x1.5')
        self.__D_nominal.append(62)
        self.__pitch.append(1.5)
        self.__D_drill.append(60.5)

        self.__name.append('M62x2')
        self.__D_nominal.append(62)
        self.__pitch.append(2)
        self.__D_drill.append(60)

        self.__name.append('M62x3')
        self.__D_nominal.append(62)
        self.__pitch.append(3)
        self.__D_drill.append(59)

        self.__name.append('M62x4')
        self.__D_nominal.append(62)
        self.__pitch.append(4)
        self.__D_drill.append(58)

        self.__name.append('M65x1.5')
        self.__D_nominal.append(65)
        self.__pitch.append(1.5)
        self.__D_drill.append(63.5)

        self.__name.append('M65x2')
        self.__D_nominal.append(65)
        self.__pitch.append(2)
        self.__D_drill.append(63)

        self.__name.append('M65x3')
        self.__D_nominal.append(65)
        self.__pitch.append(3)
        self.__D_drill.append(62)

        self.__name.append('M65x4')
        self.__D_nominal.append(65)
        self.__pitch.append(4)
        self.__D_drill.append(61)

        self.__name.append('M70x1.5')
        self.__D_nominal.append(70)
        self.__pitch.append(1.5)
        self.__D_drill.append(68.5)

        self.__name.append('M70x2')
        self.__D_nominal.append(70)
        self.__pitch.append(2)
        self.__D_drill.append(68)

        self.__name.append('M70x3')
        self.__D_nominal.append(70)
        self.__pitch.append(3)
        self.__D_drill.append(67)

        self.__name.append('M70x4')
        self.__D_nominal.append(70)
        self.__pitch.append(4)
        self.__D_drill.append(66)

        self.__name.append('M70x6')
        self.__D_nominal.append(70)
        self.__pitch.append(6)
        self.__D_drill.append(64)

        self.__name.append('M75x1.5')
        self.__D_nominal.append(75)
        self.__pitch.append(1.5)
        self.__D_drill.append(73.5)

        self.__name.append('M75x2')
        self.__D_nominal.append(75)
        self.__pitch.append(2)
        self.__D_drill.append(73)

        self.__name.append('M75x3')
        self.__D_nominal.append(75)
        self.__pitch.append(3)
        self.__D_drill.append(72)

        self.__name.append('M75x4')
        self.__D_nominal.append(75)
        self.__pitch.append(4)
        self.__D_drill.append(71)

        self.__name.append('M78x2')
        self.__D_nominal.append(78)
        self.__pitch.append(2)
        self.__D_drill.append(76)

        self.__name.append('M82x2')
        self.__D_nominal.append(82)
        self.__pitch.append(2)
        self.__D_drill.append(80)

        self.__name.append('M135x2')
        self.__D_nominal.append(135)
        self.__pitch.append(2)
        self.__D_drill.append(133)

        self.__name.append('M135x3')
        self.__D_nominal.append(135)
        self.__pitch.append(3)
        self.__D_drill.append(132)

        self.__name.append('M135x4')
        self.__D_nominal.append(135)
        self.__pitch.append(4)
        self.__D_drill.append(131)

        self.__name.append('M135x6')
        self.__D_nominal.append(135)
        self.__pitch.append(6)
        self.__D_drill.append(129)

        self.__name.append('M145x2')
        self.__D_nominal.append(145)
        self.__pitch.append(2)
        self.__D_drill.append(143)

        self.__name.append('M145x3')
        self.__D_nominal.append(145)
        self.__pitch.append(3)
        self.__D_drill.append(142)

        self.__name.append('M145x4')
        self.__D_nominal.append(145)
        self.__pitch.append(4)
        self.__D_drill.append(141)

        self.__name.append('M145x6')
        self.__D_nominal.append(145)
        self.__pitch.append(6)
        self.__D_drill.append(139)

        self.__name.append('M155x3')
        self.__D_nominal.append(155)
        self.__pitch.append(3)
        self.__D_drill.append(152)

        self.__name.append('M155x4')
        self.__D_nominal.append(155)
        self.__pitch.append(4)
        self.__D_drill.append(151)

        self.__name.append('M155x6')
        self.__D_nominal.append(155)
        self.__pitch.append(6)
        self.__D_drill.append(149)

        self.__name.append('M165x3')
        self.__D_nominal.append(165)
        self.__pitch.append(3)
        self.__D_drill.append(162)

        self.__name.append('M165x4')
        self.__D_nominal.append(165)
        self.__pitch.append(4)
        self.__D_drill.append(161)

        self.__name.append('M165x6')
        self.__D_nominal.append(165)
        self.__pitch.append(6)
        self.__D_drill.append(159)

        self.__name.append('M175x3')
        self.__D_nominal.append(175)
        self.__pitch.append(3)
        self.__D_drill.append(172)

        self.__name.append('M175x4')
        self.__D_nominal.append(175)
        self.__pitch.append(4)
        self.__D_drill.append(171)

        self.__name.append('M175x6')
        self.__D_nominal.append(175)
        self.__pitch.append(6)
        self.__D_drill.append(169)

        self.__name.append('M185x3')
        self.__D_nominal.append(185)
        self.__pitch.append(3)
        self.__D_drill.append(182)

        self.__name.append('M185x4')
        self.__D_nominal.append(185)
        self.__pitch.append(4)
        self.__D_drill.append(181)

        self.__name.append('M185x6')
        self.__D_nominal.append(185)
        self.__pitch.append(6)
        self.__D_drill.append(179)

        self.__name.append('M195x3')
        self.__D_nominal.append(195)
        self.__pitch.append(3)
        self.__D_drill.append(192)

        self.__name.append('M195x4')
        self.__D_nominal.append(195)
        self.__pitch.append(4)
        self.__D_drill.append(191)

        self.__name.append('M195x6')
        self.__D_nominal.append(195)
        self.__pitch.append(6)
        self.__D_drill.append(189)

        self.__name.append('M205x3')
        self.__D_nominal.append(205)
        self.__pitch.append(3)
        self.__D_drill.append(202)

        self.__name.append('M205x4')
        self.__D_nominal.append(205)
        self.__pitch.append(4)
        self.__D_drill.append(201)

        self.__name.append('M205x6')
        self.__D_nominal.append(205)
        self.__pitch.append(6)
        self.__D_drill.append(199)

        self.__name.append('M215x3')
        self.__D_nominal.append(215)
        self.__pitch.append(3)
        self.__D_drill.append(212)

        self.__name.append('M215x4')
        self.__D_nominal.append(215)
        self.__pitch.append(4)
        self.__D_drill.append(211)

        self.__name.append('M215x6')
        self.__D_nominal.append(215)
        self.__pitch.append(6)
        self.__D_drill.append(209)

        self.__name.append('M225x3')
        self.__D_nominal.append(225)
        self.__pitch.append(3)
        self.__D_drill.append(222)

        self.__name.append('M225x4')
        self.__D_nominal.append(225)
        self.__pitch.append(4)
        self.__D_drill.append(221)

        self.__name.append('M225x6')
        self.__D_nominal.append(225)
        self.__pitch.append(6)
        self.__D_drill.append(219)

        self.__name.append('M230x3')
        self.__D_nominal.append(230)
        self.__pitch.append(3)
        self.__D_drill.append(228)

        self.__name.append('M230x4')
        self.__D_nominal.append(230)
        self.__pitch.append(4)
        self.__D_drill.append(226)

        self.__name.append('M230x6')
        self.__D_nominal.append(230)
        self.__pitch.append(6)
        self.__D_drill.append(224)

        self.__name.append('M230x8')
        self.__D_nominal.append(230)
        self.__pitch.append(8)
        self.__D_drill.append(222)

        self.__name.append('M235x3')
        self.__D_nominal.append(235)
        self.__pitch.append(3)
        self.__D_drill.append(232)

        self.__name.append('M235x4')
        self.__D_nominal.append(235)
        self.__pitch.append(4)
        self.__D_drill.append(231)

        self.__name.append('M235x6')
        self.__D_nominal.append(235)
        self.__pitch.append(6)
        self.__D_drill.append(229)

        self.__name.append('M245x3')
        self.__D_nominal.append(245)
        self.__pitch.append(3)
        self.__D_drill.append(242)

        self.__name.append('M245x4')
        self.__D_nominal.append(245)
        self.__pitch.append(4)
        self.__D_drill.append(241)

        self.__name.append('M245x6')
        self.__D_nominal.append(245)
        self.__pitch.append(6)
        self.__D_drill.append(239)

        self.__name.append('M255x4')
        self.__D_nominal.append(255)
        self.__pitch.append(4)
        self.__D_drill.append(251)

        self.__name.append('M255x6')
        self.__D_nominal.append(255)
        self.__pitch.append(6)
        self.__D_drill.append(249)

        self.__name.append('M265x4')
        self.__D_nominal.append(265)
        self.__pitch.append(4)
        self.__D_drill.append(261)

        self.__name.append('M265x6')
        self.__D_nominal.append(265)
        self.__pitch.append(6)
        self.__D_drill.append(259)

        self.__name.append('M270x4')
        self.__D_nominal.append(270)
        self.__pitch.append(4)
        self.__D_drill.append(266)

        self.__name.append('M270x6')
        self.__D_nominal.append(270)
        self.__pitch.append(6)
        self.__D_drill.append(264)

        self.__name.append('M270x8')
        self.__D_nominal.append(270)
        self.__pitch.append(8)
        self.__D_drill.append(262)

        self.__name.append('M275x4')
        self.__D_nominal.append(275)
        self.__pitch.append(4)
        self.__D_drill.append(271)

        self.__name.append('M275x6')
        self.__D_nominal.append(275)
        self.__pitch.append(6)
        self.__D_drill.append(269)

        self.__name.append('M285x4')
        self.__D_nominal.append(285)
        self.__pitch.append(4)
        self.__D_drill.append(281)

        self.__name.append('M285x6')
        self.__D_nominal.append(285)
        self.__pitch.append(6)
        self.__D_drill.append(279)

        self.__name.append('M290x4')
        self.__D_nominal.append(290)
        self.__pitch.append(4)
        self.__D_drill.append(286)

        self.__name.append('M290x6')
        self.__D_nominal.append(290)
        self.__pitch.append(6)
        self.__D_drill.append(284)

        self.__name.append('M290x8')
        self.__D_nominal.append(290)
        self.__pitch.append(8)
        self.__D_drill.append(282)

        self.__name.append('M295x4')
        self.__D_nominal.append(295)
        self.__pitch.append(4)
        self.__D_drill.append(291)

        self.__name.append('M295x6')
        self.__D_nominal.append(295)
        self.__pitch.append(6)
        self.__D_drill.append(289)

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
