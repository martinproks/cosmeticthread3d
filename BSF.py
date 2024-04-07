# -*- coding: utf-8 -*-
#
# BSF.py
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

class BSF:
    """
    class BSF

    Returns object (class) with threads parameters for British Standard
    Withworth Fine threads.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('BSF3/16')
        self.__D_nominal.append(4.83)
        self.__TPI.append(32)
        self.__D_drill.append(4)

        self.__name.append('BSF7/32')
        self.__D_nominal.append(5.59)
        self.__TPI.append(28)
        self.__D_drill.append(4.6)

        self.__name.append('BSF1/4')
        self.__D_nominal.append(6.35)
        self.__TPI.append(26)
        self.__D_drill.append(5.3)

        self.__name.append('BSF5/16')
        self.__D_nominal.append(7.87)
        self.__TPI.append(22)
        self.__D_drill.append(6.8)

        self.__name.append('BSF3/8')
        self.__D_nominal.append(9.53)
        self.__TPI.append(20)
        self.__D_drill.append(8.2)

        self.__name.append('BSF7/16')
        self.__D_nominal.append(11.18)
        self.__TPI.append(18)
        self.__D_drill.append(9.7)

        self.__name.append('BSF1/2')
        self.__D_nominal.append(12.7)
        self.__TPI.append(16)
        self.__D_drill.append(11.1)

        self.__name.append('BSF9/16')
        self.__D_nominal.append(14.22)
        self.__TPI.append(16)
        self.__D_drill.append(12.7)

        self.__name.append('BSF5/8')
        self.__D_nominal.append(16)
        self.__TPI.append(14)
        self.__D_drill.append(14)

        self.__name.append('BSF11/16')
        self.__D_nominal.append(17.53)
        self.__TPI.append(14)
        self.__D_drill.append(15.5)

        self.__name.append('BSF3/4')
        self.__D_nominal.append(19.05)
        self.__TPI.append(12)
        self.__D_drill.append(16.75)

        self.__name.append('BSF7/8')
        self.__D_nominal.append(22.35)
        self.__TPI.append(11)
        self.__D_drill.append(19.85)

        self.__name.append('BSF1')
        self.__D_nominal.append(25.4)
        self.__TPI.append(10)
        self.__D_drill.append(22.75)

        self.__name.append('BSF1 1/8')
        self.__D_nominal.append(28.575)
        self.__TPI.append(9)
        self.__D_drill.append(26.5)

        self.__name.append('BSF1 1/4')
        self.__D_nominal.append(31.75)
        self.__TPI.append(9)
        self.__D_drill.append(28.75)

        self.__name.append('BSF1 1/2')
        self.__D_nominal.append(38.1)
        self.__TPI.append(8)
        self.__D_drill.append(34.5)

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
        x = self.getTPI(ThrName)
        x = round(25.4 / x, 3) if x > 0.0 else 0.0
        return x

    def getTPI(self, ThrName):
        """
        getTPI(ThrName) -> TPI
        """
        x = 0.0
        i = 0
        while i < len(self.__name):
            if ThrName == self.__name[i]:
                x = self.__TPI[i]
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
        h = ptmp / (3.0*math.tan(27.5*math.pi/180.0))
        # This equation can not be exactly as I write it here.
        # This equation is basic thread profile, not nut with some clearence.
        x = round(Dtmp - 2*h, 3)
        return x

    def getd3(self, ThrName):
        """
        getd3(ThrName) -> d3
        """
        x = 0.0
        Dtmp = self.getD(ThrName)
        ptmp = self.getpitch(ThrName)
        h = ptmp / (3.0*math.tan(27.5*math.pi/180.0))
        # This equation can not be exactly as I write it here.
        # This equation is basic thread profile, not bolt with some clearence.
        x = round(Dtmp - 2*h, 3)
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
