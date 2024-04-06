# -*- coding: utf-8 -*-
#
# BSW.py
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



class BSW:
    """
    class BSW

    Returns object (class) with threads parameters for British Standard
    Withworth threads.
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('BSW1/16')
        self.__D_nominal.append(1.587)
        self.__TPI.append(60)
        self.__D_drill.append(1.15)

        self.__name.append('BSW3/32')
        self.__D_nominal.append(2.381)
        self.__TPI.append(48)
        self.__D_drill.append(2.041)

        self.__name.append('BSW1/8')
        self.__D_nominal.append(3.175)
        self.__TPI.append(40)
        self.__D_drill.append(2.768)

        self.__name.append('BSW5/32')
        self.__D_nominal.append(3.969)
        self.__TPI.append(32)
        self.__D_drill.append(3.459)

        self.__name.append('BSW3/16')
        self.__D_nominal.append(4.762)
        self.__TPI.append(24)
        self.__D_drill.append(4.084)

        self.__name.append('BSW7/32')
        self.__D_nominal.append(5.556)
        self.__TPI.append(24)
        self.__D_drill.append(4.878)

        self.__name.append('BSW1/4')
        self.__D_nominal.append(6.35)
        self.__TPI.append(20)
        self.__D_drill.append(5.37)

        self.__name.append('BSW5/16')
        self.__D_nominal.append(7.938)
        self.__TPI.append(18)
        self.__D_drill.append(7.034)

        self.__name.append('BSW3/8')
        self.__D_nominal.append(9.525)
        self.__TPI.append(16)
        self.__D_drill.append(8.509)

        self.__name.append('BSW7/16')
        self.__D_nominal.append(11.113)
        self.__TPI.append(14)
        self.__D_drill.append(9.951)

        self.__name.append('BSW1/2')
        self.__D_nominal.append(12.7)
        self.__TPI.append(12)
        self.__D_drill.append(11.345)

        self.__name.append('BSW9/16')
        self.__D_nominal.append(14.29)
        self.__TPI.append(12)
        self.__D_drill.append(12.93)

        self.__name.append('BSW5/8')
        self.__D_nominal.append(15.876)
        self.__TPI.append(11)
        self.__D_drill.append(14.397)

        self.__name.append('BSW3/4')
        self.__D_nominal.append(19.051)
        self.__TPI.append(10)
        self.__D_drill.append(17.424)

        self.__name.append('BSW7/8')
        self.__D_nominal.append(22.226)
        self.__TPI.append(9)
        self.__D_drill.append(20.419)

        self.__name.append('BSW1')
        self.__D_nominal.append(25.4)
        self.__TPI.append(8)
        self.__D_drill.append(23.368)

        self.__name.append('BSW1 1/8')
        self.__D_nominal.append(28.576)
        self.__TPI.append(7)
        self.__D_drill.append(26.253)

        self.__name.append('BSW1 1/4')
        self.__D_nominal.append(31.751)
        self.__TPI.append(7)
        self.__D_drill.append(29.428)

        self.__name.append('BSW1 3/8')
        self.__D_nominal.append(34.926)
        self.__TPI.append(6)
        self.__D_drill.append(32.215)

        self.__name.append('BSW1 1/2')
        self.__D_nominal.append(38.1)
        self.__TPI.append(6)
        self.__D_drill.append(35.391)

        self.__name.append('BSW1 5/8')
        self.__D_nominal.append(41.277)
        self.__TPI.append(5)
        self.__D_drill.append(38.024)

        self.__name.append('BSW1 3/4')
        self.__D_nominal.append(44.452)
        self.__TPI.append(5)
        self.__D_drill.append(41.199)

        self.__name.append('BSW1 7/8')
        self.__D_nominal.append(47.627)
        self.__TPI.append(4.5)
        self.__D_drill.append(44.012)

        self.__name.append('BSW2')
        self.__D_nominal.append(50.802)
        self.__TPI.append(4.5)
        self.__D_drill.append(47.187)

        self.__name.append('BSW2 1/4')
        self.__D_nominal.append(57.152)
        self.__TPI.append(4)
        self.__D_drill.append(53.086)

        self.__name.append('BSW2 1/2')
        self.__D_nominal.append(63.502)
        self.__TPI.append(4)
        self.__D_drill.append(59.436)

        self.__name.append('BSW2 3/4')
        self.__D_nominal.append(69.853)
        self.__TPI.append(3.5)
        self.__D_drill.append(65.205)

        self.__name.append('BSW3')
        self.__D_nominal.append(76.203)
        self.__TPI.append(3.5)
        self.__D_drill.append(71.556)

        self.__name.append('BSW3 1/4')
        self.__D_nominal.append(82.553)
        self.__TPI.append(3.25)
        self.__D_drill.append(77.548)

        self.__name.append('BSW3 1/2')
        self.__D_nominal.append(88.903)
        self.__TPI.append(3.25)
        self.__D_drill.append(83.899)

        self.__name.append('BSW3 3/4')
        self.__D_nominal.append(95.254)
        self.__TPI.append(3)
        self.__D_drill.append(89.832)

        self.__name.append('BSW4')
        self.__D_nominal.append(101.604)
        self.__TPI.append(3)
        self.__D_drill.append(96.182)

        self.__name.append('BSW4 1/4')
        self.__D_nominal.append(107.954)
        self.__TPI.append(2.875)
        self.__D_drill.append(102.297)

        self.__name.append('BSW4 1/2')
        self.__D_nominal.append(114.304)
        self.__TPI.append(2.875)
        self.__D_drill.append(108.647)

        self.__name.append('BSW4 3/4')
        self.__D_nominal.append(120.665)
        self.__TPI.append(2.75)
        self.__D_drill.append(114.74)

        self.__name.append('BSW5')
        self.__D_nominal.append(127.005)
        self.__TPI.append(2.75)
        self.__D_drill.append(121.09)

        self.__name.append('BSW5 1/4')
        self.__D_nominal.append(133.355)
        self.__TPI.append(2.625)
        self.__D_drill.append(127.159)

        self.__name.append('BSW5 1/2')
        self.__D_nominal.append(139.705)
        self.__TPI.append(2.625)
        self.__D_drill.append(133.509)

        self.__name.append('BSW5 3/4')
        self.__D_nominal.append(146.055)
        self.__TPI.append(2.5)
        self.__D_drill.append(139.549)

        self.__name.append('BSW6')
        self.__D_nominal.append(152.406)
        self.__TPI.append(2.5)
        self.__D_drill.append(145.9)

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
