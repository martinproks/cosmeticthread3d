# -*- coding: utf-8 -*-
#
# MetricCoarse1st.py
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



class MetricCoarse1st:
    """
    class MetricCoarse1st

    Returns object (class) with threads parameters for Metric coarse thread
    1st selection (ISO 261 preffered group of threads).
    """

    __name = []
    __D_nominal = []
    __pitch = []
    __D_drill = []

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__pitch = []
        self.__D_drill = []

        self.__name.append('M1')
        self.__D_nominal.append(1)
        self.__pitch.append(0.25)
        self.__D_drill.append(0.75)

        self.__name.append('M1.2')
        self.__D_nominal.append(1.2)
        self.__pitch.append(0.25)
        self.__D_drill.append(0.95)

        self.__name.append('M1.6')
        self.__D_nominal.append(1.6)
        self.__pitch.append(0.35)
        self.__D_drill.append(1.25)

        self.__name.append('M2')
        self.__D_nominal.append(2)
        self.__pitch.append(0.4)
        self.__D_drill.append(1.6)

        self.__name.append('M2.5')
        self.__D_nominal.append(2.5)
        self.__pitch.append(0.45)
        self.__D_drill.append(2.05)

        self.__name.append('M3')
        self.__D_nominal.append(3)
        self.__pitch.append(0.5)
        self.__D_drill.append(2.5)

        self.__name.append('M4')
        self.__D_nominal.append(4)
        self.__pitch.append(0.7)
        self.__D_drill.append(3.3)

        self.__name.append('M5')
        self.__D_nominal.append(5)
        self.__pitch.append(0.8)
        self.__D_drill.append(4.2)

        self.__name.append('M6')
        self.__D_nominal.append(6)
        self.__pitch.append(1)
        self.__D_drill.append(5)

        self.__name.append('M8')
        self.__D_nominal.append(8)
        self.__pitch.append(1.25)
        self.__D_drill.append(6.75)

        self.__name.append('M10')
        self.__D_nominal.append(10)
        self.__pitch.append(1.5)
        self.__D_drill.append(8.5)

        self.__name.append('M12')
        self.__D_nominal.append(12)
        self.__pitch.append(1.75)
        self.__D_drill.append(10.2)

        self.__name.append('M16')
        self.__D_nominal.append(16)
        self.__pitch.append(2)
        self.__D_drill.append(14)

        self.__name.append('M20')
        self.__D_nominal.append(20)
        self.__pitch.append(2.5)
        self.__D_drill.append(17.5)

        self.__name.append('M24')
        self.__D_nominal.append(24)
        self.__pitch.append(3)
        self.__D_drill.append(21)

        self.__name.append('M30')
        self.__D_nominal.append(30)
        self.__pitch.append(3.5)
        self.__D_drill.append(26.5)

        self.__name.append('M36')
        self.__D_nominal.append(36)
        self.__pitch.append(4)
        self.__D_drill.append(32)

        self.__name.append('M42')
        self.__D_nominal.append(42)
        self.__pitch.append(4.5)
        self.__D_drill.append(37.5)

        self.__name.append('M48')
        self.__D_nominal.append(48)
        self.__pitch.append(5)
        self.__D_drill.append(43)

        self.__name.append('M56')
        self.__D_nominal.append(56)
        self.__pitch.append(5.5)
        self.__D_drill.append(50.5)

        self.__name.append('M64')
        self.__D_nominal.append(64)
        self.__pitch.append(6)
        self.__D_drill.append(58)

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
