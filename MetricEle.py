# -*- coding: utf-8 -*-
#
# MetricEle.py
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

class MetricEle:
    """
    class MetricEle

    Returns object (class) with threads parameters for Metric Electrical thread
    choice - threads and pitchs according to EN 60423. Many electric
    devices and companies are using this selection set.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__pitch = []
        self.__D_drill = []

        self.__name.append('M6x0.75')
        self.__D_nominal.append(6)
        self.__pitch.append(0.75)
        self.__D_drill.append(5.2)

        self.__name.append('M8x1')
        self.__D_nominal.append(8)
        self.__pitch.append(1)
        self.__D_drill.append(7)

        self.__name.append('M10x1')
        self.__D_nominal.append(10)
        self.__pitch.append(1)
        self.__D_drill.append(9)

        self.__name.append('M12x1.5')
        self.__D_nominal.append(12)
        self.__pitch.append(1.5)
        self.__D_drill.append(10.5)

        self.__name.append('M16x1.5')
        self.__D_nominal.append(16)
        self.__pitch.append(1.5)
        self.__D_drill.append(14.5)

        self.__name.append('M20x1.5')
        self.__D_nominal.append(20)
        self.__pitch.append(1.5)
        self.__D_drill.append(18.5)

        self.__name.append('M25x1.5')
        self.__D_nominal.append(25)
        self.__pitch.append(1.5)
        self.__D_drill.append(23.5)

        self.__name.append('M32x1.5')
        self.__D_nominal.append(32)
        self.__pitch.append(1.5)
        self.__D_drill.append(30.5)

        self.__name.append('M40x1.5')
        self.__D_nominal.append(40)
        self.__pitch.append(1.5)
        self.__D_drill.append(38.5)

        self.__name.append('M50x1.5')
        self.__D_nominal.append(50)
        self.__pitch.append(1.5)
        self.__D_drill.append(48.5)

        self.__name.append('M63x1.5')
        self.__D_nominal.append(63)
        self.__pitch.append(1.5)
        self.__D_drill.append(61.5)

        self.__name.append('M75x1.5')
        self.__D_nominal.append(75)
        self.__pitch.append(1.5)
        self.__D_drill.append(73.5)

        self.__name.append('M90x2')
        self.__D_nominal.append(90)
        self.__pitch.append(2)
        self.__D_drill.append(88)

        self.__name.append('M110x2')
        self.__D_nominal.append(110)
        self.__pitch.append(2)
        self.__D_drill.append(108)

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
