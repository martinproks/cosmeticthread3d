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

__title__   = 'Cosmetic Thread 3D Work Bench'
__author__  = 'Martin Prokš'
__License__ = 'LGPL-2.1-or-later'
__url__     = 'https://github.com/martinproks/cosmeticthread3d'



class MetricCoarse1st:
    """
    class MetricCoarse1st

    Returns object (class) with list of thread parameters for Metric coarse thread
    1st selection (ISO 261 preffered group of threads).

                 - Wrapping object for lists:
    MetricCoarse1st.name[]      - List of descriptions of the threads
    MetricCoarse1st.D_nominal[] - List of nominal diameters
    MetricCoarse1st.pitch[]     - List of pitchs
    MetricCoarse1st.D[]         - List of major diameters
    MetricCoarse1st.D1[]        - List of minor diameters of internal thread
    MetricCoarse1st.d3[]        - List of minor diameters of external thread
    MetricCoarse1st.D_drill[]   - List of recommended diameters for pre-drilled holes
    """
    
    name = []
    D_nominal = []
    pitch = []
    D = []
    D1 = []
    d3 = []
    D_drill = []

    def __init__(self):
        self.name.append('M1')
        self.D_nominal.append(1)
        self.pitch.append(0.25)
        self.D.append(1)
        self.D1.append(0.729)
        self.d3.append(0.693)
        self.D_drill.append(0.75)

        self.name.append('M1.2')
        self.D_nominal.append(1.2)
        self.pitch.append(0.25)
        self.D.append(1.2)
        self.D1.append(0.929)
        self.d3.append(0.893)
        self.D_drill.append(0.95)

        self.name.append('M1.6')
        self.D_nominal.append(1.6)
        self.pitch.append(0.35)
        self.D.append(1.6)
        self.D1.append(1.221)
        self.d3.append(1.171)
        self.D_drill.append(1.25)

        self.name.append('M2')
        self.D_nominal.append(2)
        self.pitch.append(0.4)
        self.D.append(2)
        self.D1.append(1.567)
        self.d3.append(1.509)
        self.D_drill.append(1.6)

        self.name.append('M2.5')
        self.D_nominal.append(2.5)
        self.pitch.append(0.45)
        self.D.append(2.5)
        self.D1.append(2.013)
        self.d3.append(1.948)
        self.D_drill.append(2.05)

        self.name.append('M3')
        self.D_nominal.append(3)
        self.pitch.append(0.5)
        self.D.append(3)
        self.D1.append(2.459)
        self.d3.append(2.387)
        self.D_drill.append(2.5)

        self.name.append('M4')
        self.D_nominal.append(4)
        self.pitch.append(0.7)
        self.D.append(4)
        self.D1.append(3.242)
        self.d3.append(3.141)
        self.D_drill.append(3.3)

        self.name.append('M5')
        self.D_nominal.append(5)
        self.pitch.append(0.8)
        self.D.append(5)
        self.D1.append(4.134)
        self.d3.append(4.019)
        self.D_drill.append(4.2)

        self.name.append('M6')
        self.D_nominal.append(6)
        self.pitch.append(1)
        self.D.append(6)
        self.D1.append(4.917)
        self.d3.append(4.773)
        self.D_drill.append(5)

        self.name.append('M8')
        self.D_nominal.append(8)
        self.pitch.append(1.25)
        self.D.append(8)
        self.D1.append(6.647)
        self.d3.append(6.466)
        self.D_drill.append(6.75)

        self.name.append('M10')
        self.D_nominal.append(10)
        self.pitch.append(1.5)
        self.D.append(10)
        self.D1.append(8.376)
        self.d3.append(8.16)
        self.D_drill.append(8.5)

        self.name.append('M12')
        self.D_nominal.append(12)
        self.pitch.append(1.75)
        self.D.append(12)
        self.D1.append(10.106)
        self.d3.append(9.853)
        self.D_drill.append(10.2)

        self.name.append('M16')
        self.D_nominal.append(16)
        self.pitch.append(2)
        self.D.append(16)
        self.D1.append(13.835)
        self.d3.append(13.546)
        self.D_drill.append(14)

        self.name.append('M20')
        self.D_nominal.append(20)
        self.pitch.append(2.5)
        self.D.append(20)
        self.D1.append(17.294)
        self.d3.append(16.933)
        self.D_drill.append(17.5)

        self.name.append('M24')
        self.D_nominal.append(24)
        self.pitch.append(3)
        self.D.append(24)
        self.D1.append(20.752)
        self.d3.append(20.319)
        self.D_drill.append(21)

        self.name.append('M30')
        self.D_nominal.append(30)
        self.pitch.append(3.5)
        self.D.append(30)
        self.D1.append(26.211)
        self.d3.append(25.706)
        self.D_drill.append(26.5)

        self.name.append('M36')
        self.D_nominal.append(36)
        self.pitch.append(4)
        self.D.append(36)
        self.D1.append(31.67)
        self.d3.append(31.093)
        self.D_drill.append(32)

        self.name.append('M42')
        self.D_nominal.append(42)
        self.pitch.append(4.5)
        self.D.append(42)
        self.D1.append(37.129)
        self.d3.append(36.479)
        self.D_drill.append(37.5)

        self.name.append('M48')
        self.D_nominal.append(48)
        self.pitch.append(5)
        self.D.append(48)
        self.D1.append(42.587)
        self.d3.append(41.866)
        self.D_drill.append(43)

        self.name.append('M56')
        self.D_nominal.append(56)
        self.pitch.append(5.5)
        self.D.append(56)
        self.D1.append(50.046)
        self.d3.append(49.252)
        self.D_drill.append(50.5)

        self.name.append('M64')
        self.D_nominal.append(64)
        self.pitch.append(6)
        self.D.append(64)
        self.D1.append(57.505)
        self.d3.append(56.639)
        self.D_drill.append(58)

        self.name.append('M72')
        self.D_nominal.append(72)
        self.pitch.append(6)
        self.D.append(72)
        self.D1.append(65.505)
        self.d3.append(64.639)
        self.D_drill.append(66)

        self.name.append('M80')
        self.D_nominal.append(80)
        self.pitch.append(6)
        self.D.append(80)
        self.D1.append(73.505)
        self.d3.append(72.639)
        self.D_drill.append(74)

        self.name.append('M90')
        self.D_nominal.append(90)
        self.pitch.append(6)
        self.D.append(90)
        self.D1.append(83.505)
        self.d3.append(82.639)
        self.D_drill.append(84)

        self.name.append('M100')
        self.D_nominal.append(100)
        self.pitch.append(6)
        self.D.append(100)
        self.D1.append(93.505)
        self.d3.append(92.639)
        self.D_drill.append(94)

        self.name.append('M110')
        self.D_nominal.append(110)
        self.pitch.append(6)
        self.D.append(110)
        self.D1.append(103.505)
        self.d3.append(102.639)
        self.D_drill.append(104)

        self.name.append('M125')
        self.D_nominal.append(125)
        self.pitch.append(8)
        self.D.append(125)
        self.D1.append(116.34)
        self.d3.append(115.185)
        self.D_drill.append(116.5)

        self.name.append('M140')
        self.D_nominal.append(140)
        self.pitch.append(8)
        self.D.append(140)
        self.D1.append(131.34)
        self.d3.append(130.185)
        self.D_drill.append(131.5)

        self.name.append('M160')
        self.D_nominal.append(160)
        self.pitch.append(8)
        self.D.append(160)
        self.D1.append(151.34)
        self.d3.append(150.185)
        self.D_drill.append(151.5)

        self.name.append('M180')
        self.D_nominal.append(180)
        self.pitch.append(8)
        self.D.append(180)
        self.D1.append(171.34)
        self.d3.append(170.185)
        self.D_drill.append(171.5)

        self.name.append('M200')
        self.D_nominal.append(200)
        self.pitch.append(8)
        self.D.append(200)
        self.D1.append(191.34)
        self.d3.append(190.185)
        self.D_drill.append(191.5)

        self.name.append('M220')
        self.D_nominal.append(220)
        self.pitch.append(8)
        self.D.append(220)
        self.D1.append(211.34)
        self.d3.append(210.185)
        self.D_drill.append(211.5)

        self.name.append('M250')
        self.D_nominal.append(250)
        self.pitch.append(8)
        self.D.append(250)
        self.D1.append(241.34)
        self.d3.append(240.185)
        self.D_drill.append(241.5)

        self.name.append('M280')
        self.D_nominal.append(280)
        self.pitch.append(8)
        self.D.append(280)
        self.D1.append(271.34)
        self.d3.append(270.185)
        self.D_drill.append(271.5)
  
    
