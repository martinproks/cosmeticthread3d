# -*- coding: utf-8 -*-
#
# UNF.py
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

class UNF:
    """
    class UNF

    Returns object (class) with threads parameters for Unified Thread
    Standard Fine.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('#0-80 UNF')
        self.__D_nominal.append(1.524)
        self.__TPI.append(80)
        self.__D_drill.append(1.194)

        self.__name.append('#1-72 UNF')
        self.__D_nominal.append(1.8542)
        self.__TPI.append(72)
        self.__D_drill.append(1.524)

        self.__name.append('#2-64 UNF')
        self.__D_nominal.append(2.1844)
        self.__TPI.append(64)
        self.__D_drill.append(1.778)

        self.__name.append('#3-56 UNF')
        self.__D_nominal.append(2.5146)
        self.__TPI.append(56)
        self.__D_drill.append(2.083)

        self.__name.append('#4-48 UNF')
        self.__D_nominal.append(2.8448)
        self.__TPI.append(48)
        self.__D_drill.append(2.388)

        self.__name.append('#5-44 UNF')
        self.__D_nominal.append(3.175)
        self.__TPI.append(44)
        self.__D_drill.append(2.642)

        self.__name.append('#6-40 UNF')
        self.__D_nominal.append(3.5052)
        self.__TPI.append(40)
        self.__D_drill.append(2.87)

        self.__name.append('#8-36 UNF')
        self.__D_nominal.append(4.1656)
        self.__TPI.append(36)
        self.__D_drill.append(3.454)

        self.__name.append('#10-32 UNF')
        self.__D_nominal.append(4.826)
        self.__TPI.append(32)
        self.__D_drill.append(4.039)

        self.__name.append('#12-28 UNF')
        self.__D_nominal.append(5.4864)
        self.__TPI.append(28)
        self.__D_drill.append(4.623)

        self.__name.append('1/4"-28 UNF')
        self.__D_nominal.append(6.35)
        self.__TPI.append(28)
        self.__D_drill.append(5.41)

        self.__name.append('5/16"-24 UNF')
        self.__D_nominal.append(7.9375)
        self.__TPI.append(24)
        self.__D_drill.append(6.909)

        self.__name.append('3/8"-24 UNF')
        self.__D_nominal.append(9.525)
        self.__TPI.append(24)
        self.__D_drill.append(8.433)

        self.__name.append('7/16"-20 UNF')
        self.__D_nominal.append(11.1125)
        self.__TPI.append(20)
        self.__D_drill.append(9.931)

        self.__name.append('1/2"-20 UNF')
        self.__D_nominal.append(12.7)
        self.__TPI.append(20)
        self.__D_drill.append(11.506)

        self.__name.append('9/16"-18 UNF')
        self.__D_nominal.append(14.2875)
        self.__TPI.append(18)
        self.__D_drill.append(12.7)

        self.__name.append('5/8"-18 UNF')
        self.__D_nominal.append(15.875)
        self.__TPI.append(18)
        self.__D_drill.append(14.3)

        self.__name.append('3/4"-16 UNF')
        self.__D_nominal.append(19.05)
        self.__TPI.append(16)
        self.__D_drill.append(17.475)

        self.__name.append('7/8"-14 UNF')
        self.__D_nominal.append(22.225)
        self.__TPI.append(14)
        self.__D_drill.append(20.244)

        self.__name.append('1"-12 UNF')
        self.__D_nominal.append(25.4)
        self.__TPI.append(12)
        self.__D_drill.append(23.419)

        self.__name.append('1 1/8"-12 UNF')
        self.__D_nominal.append(28.575)
        self.__TPI.append(12)
        self.__D_drill.append(0.0)

        self.__name.append('1 1/4"-12 UNF')
        self.__D_nominal.append(31.75)
        self.__TPI.append(12)
        self.__D_drill.append(0.0)

        self.__name.append('1 3/8"-12 UNF')
        self.__D_nominal.append(34.925)
        self.__TPI.append(12)
        self.__D_drill.append(0.0)

        self.__name.append('1 1/2"-12 UNF')
        self.__D_nominal.append(38.1)
        self.__TPI.append(12)
        self.__D_drill.append(0.0)

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
