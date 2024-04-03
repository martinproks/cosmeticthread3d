# -*- coding: utf-8 -*-
#
# MetricCoarse2nd.py
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



import math
    


class MetricCoarse2nd:
    """
    class MetricCoarse2nd

    Returns object (class) with threads parameters for Metric coarse thread
    2nd selection (ISO 261 preffered group of threads).
    """

    __name = []
    __D_nominal = []
    __pitch = []
    __D_drill = []

    def __init__(self):
        self.__name      = []
        self.__D_nominal = []
        self.__pitch     = []
        self.__D_drill   = []

        self.__name.append('M1.1')
        self.__D_nominal.append(1.1)
        self.__pitch.append(0.25)
        self.__D_drill.append(0.85)

        self.__name.append('M1.4')
        self.__D_nominal.append(1.4)
        self.__pitch.append(0.25)
        self.__D_drill.append(1.15)

        self.__name.append('M1.8')
        self.__D_nominal.append(1.8)
        self.__pitch.append(0.35)
        self.__D_drill.append(1.5)

        self.__name.append('M2.2')
        self.__D_nominal.append(2.2)
        self.__pitch.append(0.45)
        self.__D_drill.append(1.75)

        self.__name.append('M3.5')
        self.__D_nominal.append(3.5)
        self.__pitch.append(0.6)
        self.__D_drill.append(2.85)

        self.__name.append('M4.5')
        self.__D_nominal.append(4.5)
        self.__pitch.append(0.75)
        self.__D_drill.append(3.7)

        self.__name.append('M7')
        self.__D_nominal.append(7)
        self.__pitch.append(1)
        self.__D_drill.append(5.95)

        self.__name.append('M14')
        self.__D_nominal.append(14)
        self.__pitch.append(2)
        self.__D_drill.append(11.9)

        self.__name.append('M18')
        self.__D_nominal.append(18)
        self.__pitch.append(2.5)
        self.__D_drill.append(15.3)

        self.__name.append('M22')
        self.__D_nominal.append(22)
        self.__pitch.append(2.5)
        self.__D_drill.append(19.3)

        self.__name.append('M27')
        self.__D_nominal.append(27)
        self.__pitch.append(3)
        self.__D_drill.append(23.8)

        self.__name.append('M33')
        self.__D_nominal.append(33)
        self.__pitch.append(3.5)
        self.__D_drill.append(29.5)

        self.__name.append('M39')
        self.__D_nominal.append(39)
        self.__pitch.append(4)
        self.__D_drill.append(34.8)

        self.__name.append('M45')
        self.__D_nominal.append(45)
        self.__pitch.append(4.5)
        self.__D_drill.append(40.2)

        self.__name.append('M52')
        self.__D_nominal.append(52)
        self.__pitch.append(5)
        self.__D_drill.append(46.6)

        self.__name.append('M60')
        self.__D_nominal.append(60)
        self.__pitch.append(5.5)
        self.__D_drill.append(54.2)

        self.__name.append('M68')
        self.__D_nominal.append(68)
        self.__pitch.append(6)
        self.__D_drill.append(65.6)

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
