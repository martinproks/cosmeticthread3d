# -*- coding: utf-8 -*-
#
# Gthread.py
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

class Gthread:
    """
    class Gthread

    Returns object (class) with threads parameters for British Standard
    Pipe Parallel threads (labeled as G or BSPP).
    """

    def __init__(self):
        self.__name = []
        self.__D_nominal = []
        self.__TPI = []
        self.__D_drill = []

        self.__name.append('G1/16')
        self.__D_nominal.append(7.723)
        self.__TPI.append(28)
        self.__D_drill.append(6.8)

        self.__name.append('G1/8')
        self.__D_nominal.append(9.728)
        self.__TPI.append(28)
        self.__D_drill.append(8.8)

        self.__name.append('G1/4')
        self.__D_nominal.append(13.157)
        self.__TPI.append(19)
        self.__D_drill.append(11.8)

        self.__name.append('G3/8')
        self.__D_nominal.append(16.662)
        self.__TPI.append(19)
        self.__D_drill.append(15.3)

        self.__name.append('G1/2')
        self.__D_nominal.append(20.955)
        self.__TPI.append(14)
        self.__D_drill.append(19.1)

        self.__name.append('G5/8')
        self.__D_nominal.append(22.911)
        self.__TPI.append(14)
        self.__D_drill.append(21.1)

        self.__name.append('G3/4')
        self.__D_nominal.append(26.441)
        self.__TPI.append(14)
        self.__D_drill.append(24.6)

        self.__name.append('G7/8')
        self.__D_nominal.append(30.201)
        self.__TPI.append(14)
        self.__D_drill.append(28.3)

        self.__name.append('G1')
        self.__D_nominal.append(33.249)
        self.__TPI.append(11)
        self.__D_drill.append(30.9)

        self.__name.append('G1 1/8')
        self.__D_nominal.append(37.897)
        self.__TPI.append(11)
        self.__D_drill.append(35.5)

        self.__name.append('G1 1/4')
        self.__D_nominal.append(41.91)
        self.__TPI.append(11)
        self.__D_drill.append(39.5)

        self.__name.append('G1 3/8')
        self.__D_nominal.append(44.323)
        self.__TPI.append(11)
        self.__D_drill.append(42)

        self.__name.append('G1 1/2')
        self.__D_nominal.append(47.803)
        self.__TPI.append(11)
        self.__D_drill.append(45.4)

        self.__name.append('G1 5/8')
        self.__D_nominal.append(52.883)
        self.__TPI.append(11)
        self.__D_drill.append(50.5)

        self.__name.append('G1 3/4')
        self.__D_nominal.append(53.746)
        self.__TPI.append(11)
        self.__D_drill.append(51.4)

        self.__name.append('G1 7/8')
        self.__D_nominal.append(56.998)
        self.__TPI.append(11)
        self.__D_drill.append(54.6)

        self.__name.append('G2')
        self.__D_nominal.append(59.614)
        self.__TPI.append(11)
        self.__D_drill.append(57.2)

        self.__name.append('G2 1/4')
        self.__D_nominal.append(65.71)
        self.__TPI.append(11)
        self.__D_drill.append(63.3)

        self.__name.append('G2 1/2')
        self.__D_nominal.append(75.184)
        self.__TPI.append(11)
        self.__D_drill.append(72.8)

        self.__name.append('G2 3/4')
        self.__D_nominal.append(81.534)
        self.__TPI.append(11)
        self.__D_drill.append(79.2)

        self.__name.append('G3')
        self.__D_nominal.append(87.884)
        self.__TPI.append(11)
        self.__D_drill.append(85.5)

        self.__name.append('G3 1/4')
        self.__D_nominal.append(93.98)
        self.__TPI.append(11)
        self.__D_drill.append(91.6)

        self.__name.append('G3 1/2')
        self.__D_nominal.append(100.33)
        self.__TPI.append(11)
        self.__D_drill.append(98)

        self.__name.append('G3 3/4')
        self.__D_nominal.append(106.68)
        self.__TPI.append(11)
        self.__D_drill.append(104.3)

        self.__name.append('G4')
        self.__D_nominal.append(113.03)
        self.__TPI.append(11)
        self.__D_drill.append(110.7)

        self.__name.append('G4 1/2')
        self.__D_nominal.append(125.73)
        self.__TPI.append(11)
        self.__D_drill.append(123.4)

        self.__name.append('G5')
        self.__D_nominal.append(138.43)
        self.__TPI.append(11)
        self.__D_drill.append(136.1)

        self.__name.append('G5 1/2')
        self.__D_nominal.append(151.13)
        self.__TPI.append(11)
        self.__D_drill.append(148.8)

        self.__name.append('G6')
        self.__D_nominal.append(163.83)
        self.__TPI.append(11)
        self.__D_drill.append(161.5)

        self.__name.append('G7')
        self.__D_nominal.append(189.23)
        self.__TPI.append(10)
        self.__D_drill.append(186.6)

        self.__name.append('G8')
        self.__D_nominal.append(214.63)
        self.__TPI.append(10)
        self.__D_drill.append(212)

        self.__name.append('G9')
        self.__D_nominal.append(240.03)
        self.__TPI.append(10)
        self.__D_drill.append(237.4)

        self.__name.append('G10')
        self.__D_nominal.append(265.43)
        self.__TPI.append(10)
        self.__D_drill.append(262.8)

        self.__name.append('G11')
        self.__D_nominal.append(290.83)
        self.__TPI.append(8)
        self.__D_drill.append(287.6)

        self.__name.append('G12')
        self.__D_nominal.append(316.23)
        self.__TPI.append(8)
        self.__D_drill.append(313)

        self.__name.append('G13')
        self.__D_nominal.append(347.472)
        self.__TPI.append(8)
        self.__D_drill.append(344.2)

        self.__name.append('G14')
        self.__D_nominal.append(372.872)
        self.__TPI.append(8)
        self.__D_drill.append(369.6)

        self.__name.append('G15')
        self.__D_nominal.append(398.272)
        self.__TPI.append(8)
        self.__D_drill.append(395)

        self.__name.append('G16')
        self.__D_nominal.append(423.672)
        self.__TPI.append(8)
        self.__D_drill.append(420.4)

        self.__name.append('G17')
        self.__D_nominal.append(449.072)
        self.__TPI.append(8)
        self.__D_drill.append(445.8)

        self.__name.append('G18')
        self.__D_nominal.append(474.472)
        self.__TPI.append(8)
        self.__D_drill.append(471.2)

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
        h = 0.6403*ptmp
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
        h = 0.6403*ptmp
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
