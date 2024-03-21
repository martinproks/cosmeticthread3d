# CosmeticThread3D

Version: 0.1

Author: Martin Prokš

e-mail: martin.proks@proks-martin.cz

2024

Forum link: [[Feature discussion] Cosmetic thread - 3D geometry - FreeCAD Forum](https://forum.freecad.org/viewtopic.php?t=85047)

Git link: [GitHub: FreeCAD tool - cosmetic thread for 3D geometry - experimental](https://github.com/martinproks/cosmeticthread3d)

FreeCAD tool - cosmetic thread for 3D geometry - experimental.

This tool should make 3D representation and important parameters of cosmetic threads (internal and external) for basic metric standard threads to the FreeCAD.

Goal of this tool is not bring final version of the cosmetic threads (not yet), but explore ways how to do it and prepare background for more stable and good final implementation.

![Cosmetic Thread 3D - internal and external examples](https://github.com/martinproks/cosmeticthread3d/blob/main/doc/img/test_2024-03-01.png?raw=true)

---

# How to use it

## Workbench installation

Find path to Your FreeCAD `Mod` directory. You can find it by typing command `App.getUserAppDataDir()` in the [Python console](https://wiki.freecad.org/Python_console "Python console").

Create folder `Mod/CosmeticThread3D` and copy there all data from this git repository.

Restart FreeCAD and the workbench should be there.

This tool is early stage of developement. It is not usable for real work yet.

## Usage

1. Open some document (`tests_and_examples/testing_model.FCStd` for example)

2. Press Internal cosmetic thread button (from menu or from tool buttons). It should create cone and attachment editor. It represent thread orientation.

3. Select hole edge (circle) as first attachment and select "Concentric".

4. If You need, flip side orientation.

5. Set thread parameters.

6. Press OK.

![Cosmetic Thread 3D internal  how to use it](https://github.com/martinproks/cosmeticthread3d/blob/main/doc/img/ct3d__first_test.gif?raw=true)

Feedback is welcome.

---

# Main idea

Some users (and 3D geometry) does not need true shape of threads in the model. We need just clear visual information like: this hole is not simple hole, this is threaded hole with thread nominal dimension MX and length Y mm. Or this cylindrical end of shaft/bolt/pin/whatever is threaded MX length Y mm. This level of information is enought for drawing making and later machining. (Plus informations about required tolerances and roughness.) And it is enought to visual check if the nominal diameters and lenghts of threads are OK in the mating parts like bolt+nut in an assembly.

True shape of the thread is not necessary to see and the true shape is potential source of problems on a larger models or assemblies. True shape is consuming a lot of computation resources and it is CPU killer in a case of bigger assembly with a lot of screws, nuts and threaded components.

## Supported threads

This tool should support at least standard metric threads with coarse pitch. It means threads M1 to M280 at least. I hope it will be not big problem to support more thread types and pitch in a future. But at this moment, there is just Metric coarse thread (1st selection) supported.

## Visual representation

There are more types of Cosmetic Threads for tests and comparison what type is the best for further implementation. Generally it is important  to see in 3D:

* Length of the thread.

* Major and minor diameters of the thread.

* Optionally some helpfull geometry to better visualisation of the thread (e.g. helix with correct pitch).

## FreeCAD geometric and parameter representation

### Type 0 geometric representation

Shell of end of thread and shell of major/minor diameter.

Helix (right handed) on the drilled hole diameter with thread pitch.

### Type 1 geometric representation

Shell of end of thread and shell of major/minor diameter.

### Type 2 geometric representation

Separate body (tube) representing major/minor diameter and length of the thread.

### Type 3 geometric representation

Circular shallow groves with distance = pitch between groves.

### Type 4 geometric representation

Shell of major/minor diameter with simple texture.

### Parameters of FreeCAD thread feature

The cosmetic thread geometry is wrapped into one FreeCAD feature (python feature) with parameters for possibility to advanced usage - for example for TechDraw.

The parameters are:

* Thread designation (for example M10).

* Nominal thread diameter (for example 10 mm).

* Pitch (for example 1.5 mm).

* Major diameter and minor diameter for zero tolerances (for example external thread 10 mm / 8.160 mm; internal thread 10 mm / 8.376 mm).

* Thread length (for example 15 mm).

* Pre-drilled hole diameter in the case of internal thread (for example 8.5 mm).

* Tolerances of the thread (for example -6H or -6g).

* Required roughness of the thread (for example Ra 1.6).

* Tolerance of lenght of the thread (for example -0/+1 mm).

---

# Implementation

## File structure - what is what

- `doc/` - documentation...

- `icons/` - icon folder...

- `tests_and_examples/` - just some junk-yard...

- `Init.py` - this file is loaded when FreeCAD starts. It is import of the `cosmeticthread3d` class there.

- `InitGui.py` - the workbench GUI, menus and toolbar buttons.

- `__init__.py` - rest of macro version of the scripts I started. Not relevant for workbench.

- `ct3d_params.py` - common parameters definition for all thread versions and types.

- `cosmeticthread3d_part.py` - all the working code for console mode for Part version of threads.

- `cosmeticthread3d_Gui.py` - GUI buttons and menus called from InitGui.py.

- `ct3dGuiTools.py` - tools for cosmeticthread3d_Gui.

- `MetricCoarse1st.py` - tabularized parameters for metric coarse threads, preffered selection (1st) according to ISO 261

## Notes to implementation

There are more functions and classes for threads (at least it is planned).

* **P0** - **Part** version, **type 0** of geometry representation.
  The whole work is based on Part objects and it is dedicated to be used on Part geometry. Do not mix it with PartDesign, there are non-compatible problems.

* **P1** - **Part** version, **type 1** of geometry representation.
  Simmilar as P0, but without the helix.

* **P2** - **Part** version, **type 2** of geometry representation.
  Thread is simulated by tube D-D1-length / D-d3-length.

* **P4** - **Part** version, **type 4** of geometry representation.
  Shell with texture.

* **PD0** - **PartDesign** version, **type 0** of geometry representation.
  (not implemented yet)
  Geometric identical or verry simmilar to P0.

* **PD1** - **PartDesign** version, **type 1** of geometry representation.
  (*not implemented yet*)
  Simmilar as PD0, but without the helix.

* **PD2** - **PartDesign** version, **type 2** of geometry representation.
  (*not implemented yet*)
  Multi-body geometry...

* **PD3** - **PartDesign** version, **type 3** of geometry representation.
  (*not implemented yet*)
  Small circular grooves as visual thread indication.

* **PD4** - **PartDesign** version, **type 4** of geometry representation.
  (*not implemented yet*)
  Shell with texture.

Workbench for just two buttons does not make sense in the end. But for the developement of the tools it is most probably the easyest way how to do it. Someday in the future it will be good idea to merge it with some existing and more general work bench - Part or PartDesign I think. Or merge it with some other thread oriented work bench?

# Known issues

1. It is based on a Part objects now and it works well with geometry based on Part Work Bench.For using with PartDesign objects it is necessary to use ShapeBinder or SubShapeBinder.

2. It will work just for simple holes perpendicular to starting plane. If the starting plane will be under angle to the hole axis, it will be a little bit wrong 3d representation.

3. Not plannar starting surface is not supported (at least yet). No threads to the cylindrical shape or spherical or general surface... Yeas there will be work-aroud with additional circles or datums or lines as hole axis, but again the final representation will be not exactly correct.

4. These problems are common for thread terminantion too.

5. Hole to the thread will be not correct representation.

6. Icons are uggly. Who cares? It is just start of developement, icons are the last thing I care.

7. TechDraw problems. On the normal view, the thread major diameter is shown. It is not exactly according to ISO drawing standards, there is whole circle shown. Bigger problem is ViewSections. The ViewSections showns just bodies, faces and their edges are ignored. It means, the cosmetic thread is not shown on ViewSections at this moment.

8. There is no python report what functions are called on background.

9. There is no language localization, it works in English only.

10. 
