# -*- coding: utf-8 -*-
#
# UNC.py
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

class UNC:
    """
    class UNC

    Returns object (class) with threads parameters for Unified Thread
    Standard Coarse.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('#1-64 UNC')
        self.__D_nominal.append(1.8542)
        self.__TPI.append(64)
        self.__D_drill.append(1.52)

        self.__name.append('#2-56 UNC')
        self.__D_nominal.append(2.1844)
        self.__TPI.append(56)
        self.__D_drill.append(1.78)

        self.__name.append('#3-48 UNC')
        self.__D_nominal.append(2.5146)
        self.__TPI.append(48)
        self.__D_drill.append(2)

        self.__name.append('#4-40 UNC')
        self.__D_nominal.append(2.8448)
        self.__TPI.append(40)
        self.__D_drill.append(2.26)

        self.__name.append('#5-40 UNC')
        self.__D_nominal.append(3.1750)
        self.__TPI.append(40)
        self.__D_drill.append(2.59)

        self.__name.append('#6-32 UNC')
        self.__D_nominal.append(3.5052)
        self.__TPI.append(32)
        self.__D_drill.append(2.718)

        self.__name.append('#8-32 UNC')
        self.__D_nominal.append(4.1656)
        self.__TPI.append(32)
        self.__D_drill.append(3.454)

        self.__name.append('#10-24 UNC')
        self.__D_nominal.append(4.826)
        self.__TPI.append(24)
        self.__D_drill.append(3.81)

        self.__name.append('#12-24 UNC')
        self.__D_nominal.append(5.4864)
        self.__TPI.append(24)
        self.__D_drill.append(4.496)

        self.__name.append('1/4"-20 UNC')
        self.__D_nominal.append(6.35)
        self.__TPI.append(20)
        self.__D_drill.append(5.105)

        self.__name.append('5/16"-18 UNC')
        self.__D_nominal.append(7.9375)
        self.__TPI.append(18)
        self.__D_drill.append(6.528)

        self.__name.append('3/8"-16 UNC')
        self.__D_nominal.append(9.525)
        self.__TPI.append(16)
        self.__D_drill.append(7.95)

        self.__name.append('7/16"-14 UNC')
        self.__D_nominal.append(11.1125)
        self.__TPI.append(14)
        self.__D_drill.append(9.347)

        self.__name.append('1/2"-13 UNC')
        self.__D_nominal.append(12.7)
        self.__TPI.append(13)
        self.__D_drill.append(10.719)

        self.__name.append('9/16"-12 UNC')
        self.__D_nominal.append(14.2875)
        self.__TPI.append(12)
        self.__D_drill.append(12.294)

        self.__name.append('5/8"-11 UNC')
        self.__D_nominal.append(15.875)
        self.__TPI.append(11)
        self.__D_drill.append(14.487)

        self.__name.append('3/4"-10 UNC')
        self.__D_nominal.append(19.05)
        self.__TPI.append(10)
        self.__D_drill.append(16.662)

        self.__name.append('7/8"-9 UNC')
        self.__D_nominal.append(22.225)
        self.__TPI.append(9)
        self.__D_drill.append(19.456)

        self.__name.append('1"-8 UNC')
        self.__D_nominal.append(25.4)
        self.__TPI.append(8)
        self.__D_drill.append(22.225)

        self.__name.append('1 1/8"-7 UNC')
        self.__D_nominal.append(28.575)
        self.__TPI.append(7)
        self.__D_drill.append(0.0)

        self.__name.append('1 1/4"-7 UNC')
        self.__D_nominal.append(31.75)
        self.__TPI.append(7)
        self.__D_drill.append(0.0)

        self.__name.append('1 3/8"-6 UNC')
        self.__D_nominal.append(34.925)
        self.__TPI.append(6)
        self.__D_drill.append(0.0)

        self.__name.append('1 1/2"-6 UNC')
        self.__D_nominal.append(38.1)
        self.__TPI.append(6)
        self.__D_drill.append(0.0)

        self.__name.append('1 3/4"-5 UNC')
        self.__D_nominal.append(44.45)
        self.__TPI.append(5)
        self.__D_drill.append(0.0)

        self.__name.append('2"-4 1/2 UNC')
        self.__D_nominal.append(50.8)
        self.__TPI.append(4.5)
        self.__D_drill.append(0.0)

        self.__name.append('2 1/4"-4 1/2 UNC')
        self.__D_nominal.append(57.15)
        self.__TPI.append(4.5)
        self.__D_drill.append(0.0)

        self.__name.append('2 1/2"-4 UNC')
        self.__D_nominal.append(63.5)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('2 3/4"-4 UNC')
        self.__D_nominal.append(69.85)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('3"-4 UNC')
        self.__D_nominal.append(76.2)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('3 1/4"-4 UNC')
        self.__D_nominal.append(82.55)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('3 1/2"-4 UNC')
        self.__D_nominal.append(88.9)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('3 3/4"-4 UNC')
        self.__D_nominal.append(95.25)
        self.__TPI.append(4)
        self.__D_drill.append(0.0)

        self.__name.append('4"-4 UNC')
        self.__D_nominal.append(101.6)
        self.__TPI.append(4)
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
