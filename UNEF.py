# -*- coding: utf-8 -*-
#
# UNEF.py
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

class UNEF:
    """
    class UNEF

    Returns object (class) with threads parameters for Unified Thread
    Standard Extra Fine.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('#12-32 UNEF')
        self.__D_nominal.append(5.4864)
        self.__TPI.append(32)
        self.__D_drill.append(4.775)

        self.__name.append('1/4"-32 UNEF')
        self.__D_nominal.append(6.35)
        self.__TPI.append(32)
        self.__D_drill.append(5.563)

        self.__name.append('5/16"-32 UNEF')
        self.__D_nominal.append(7.9375)
        self.__TPI.append(32)
        self.__D_drill.append(7.137)

        self.__name.append('3/8"-32 UNEF')
        self.__D_nominal.append(9.525)
        self.__TPI.append(32)
        self.__D_drill.append(8.738)

        self.__name.append('7/16"-28 UNEF')
        self.__D_nominal.append(11.1125)
        self.__TPI.append(28)
        self.__D_drill.append(10.262)

        self.__name.append('1/2"-28 UNEF')
        self.__D_nominal.append(12.7)
        self.__TPI.append(28)
        self.__D_drill.append(11.913)

        self.__name.append('9/16"-24 UNEF')
        self.__D_nominal.append(14.2875)
        self.__TPI.append(24)
        self.__D_drill.append(13.106)

        self.__name.append('5/8"-24 UNEF')
        self.__D_nominal.append(15.875)
        self.__TPI.append(24)
        self.__D_drill.append(14.681)

        self.__name.append('3/4"-20 UNEF')
        self.__D_nominal.append(19.05)
        self.__TPI.append(20)
        self.__D_drill.append(17.856)

        self.__name.append('7/8"-20 UNEF')
        self.__D_nominal.append(22.225)
        self.__TPI.append(20)
        self.__D_drill.append(21.031)

        self.__name.append('1"-20 UNEF')
        self.__D_nominal.append(25.4)
        self.__TPI.append(20)
        self.__D_drill.append(24.206)

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
        H = ptmp*0.5*math.sqrt(3)
        # D min = D maj - 2 * 5/8 * H = D maj - 1.25 * H
        x = round(Dtmp - 1.25*H, 3)
        return x

    def getd3(self, ThrName):
        """
        getd3(ThrName) -> d3
        """
        x = 0.0
        Dtmp = self.getD(ThrName)
        ptmp = self.getpitch(ThrName)
        H = ptmp*0.5*math.sqrt(3)
        # D min = D maj - 2 * 5/8 * H = D maj - 1.25 * H
        x = round(Dtmp - 1.25*H, 3)
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
