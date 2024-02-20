# CosmeticThread3D

Version: 0.0 - just first preview

Author: Martin Prokš

e-mail: martin.proks@proks-martin.cz

2024

Forum link: [[Feature discussion] Cosmetic thread - 3D geometry - FreeCAD Forum](https://forum.freecad.org/viewtopic.php?t=85047)

Git link: [GitHub: FreeCAD tool - cosmetic thread for 3D geometry - experimental](https://github.com/martinproks/cosmeticthread3d)

FreeCAD tool - cosmetic thread for 3D geometry - experimental.

This tool should make 3D representation and important parameters of cosmetic threads (internal and external) for basic metric standard threads to the FreeCAD.

Goal of this macro is not bring final version of the cosmetic threads, but explore ways how to do it and prepare background for more stable and better codded solution. This macro is just first approach.

I'm not a programmer, I'm a learning python/FreeCAD techniques and I'm fighting with GIT - a lot. Be patient with this code and with me please.

---

# Main ideas

Some users (and 3D geometry) does not need true shape of threads in the model. We need just clear visual information like: this hole is not simple hole, this is threaded hole with thread nominal dimension MX and length Y mm. Or this cylindrical end of shaft/bolt/pin/whatever is threaded MX length Y mm. This level of information is enought for drawing making and later machining. (Plus informations about required tolerances and roughness.) And it is enought to visual check if the nominal diameters and lenghts of threads are OK in the mating parts like bolt+nut in an assembly.

True shape of the thread is not necessary to see and the true shape is potential source of problems on a larger models or assemblies. True shape is consuming a lot of computation resources and it is CPU killer in a case of bigger assembly with a lot of screws, nuts and threaded components.

## Supported threads

This tool should support at least standard metric threads with coarse pitch. It means threads M1.6 to M64 at least. I hope it will be not big problem to support more thread types and pitch.

## Visual representation

For 3D representation it is good to see for threaded parts:

- Length of the thread

- Small and big diameter of the thread

- Helix with appropriate pitch

## FreeCAD geometric and parameter representation

Geometric representation should be for internal thread:

* Shell of end of thread and shell of nominal diameter

* Helix (right handed) on the drilled hole diameter with thread pitch.

Geometric representation should be for external thread:

- Shell of end of thread and shell of small diameter.

- Helix (right handed) on nominal diameter with thread pitch.

The cosmetic thread geometry should be wrapped into one FreeCAD feature or object with parameters for possibility to advanced usage - for example for TechDraw.

The parameters should be:

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

- `icons/` - icon folder...

- `tests_and_examples/` - just some junk-yard...

- `Init.pi` - this file is loaded when FreeCAD starts. It is import of the `cosmeticthread3d` class there.

- `InitGui.py` - the workbench GUI, menus and toolbar buttons.

- `__init__.py` - rest of macro version of the scripts I started. Not relevant for workbench.

- `cosmeticthread3d.py` - all the working code for console mode.

- `cosmeticthread3d_Gui.py` - GUI part of the macro called from work bench buttons and menus.

## Notes to implementation

The whole work is based on Part objects.

Workbench for just two buttons does not make sense in the end. But for the developement of the tools it is most probably the easyest way how to do it. Someday in the future it will be good idea to merge it with some existing and more general work bench - Part or PartDesign I think. Or merge it with some other thread oriented work bench?

---

# How to use it

## Workbench installation

Find path to Your FreeCAD `Mod` directory. You can find it by typing command `App.getUserAppDataDir()` in the [Python console](https://wiki.freecad.org/Python_console "Python console").

Create folder `Mod/CosmeticThread3D` and copy there all data from this git repository.

Restart FreeCAD and the workbench should be there.

This tools are at early stage of developement. It is just presentation of the current stage and the direction it is heading. It is not usable for real work yet.

## Current usage

1. Open some document (`tests_and_examples/testing_model.FCStd` ideally)

2. Press Internal cosmetic thread button (from menu or from tool buttons). It should create cone and attachment editor. It represent thread orientation.

3. Select hole edge (circle) as first attachment and select "Concentric".

4. If You need, flip side orientation.

5. There is no GUI yet for selecting of the thread type and dimensions. It will create M10 thread for now.

6. You can check parameters of the feature.

Feedback is welcome. 

---

# Known troubles

1. There is just `internal cosmetic thread` function under developement yet. The `external cosmetic thread` will be equivalent, I just start with the internal for now.

2. It is based on a Part objects now. It means, there will be problems with PartDesign patterns - not usable. But the threaded holes are wery offen arranged into patterns (linear, rectangular or polar). It means there will be good idea to rework it to the PartDesign approach. But there will be PartDesign specific problems too.

3. There is no GUI and no thread type and dimension selection menu. Yes, it's under developement, I'm learning how to do it right now.

4. It will work just for simple holes perpendicular to starting plane. If the starting plane will be under angle to the hole axis, it will be a little bit wrong 3d representation.

5. Not plannar starting surface is not supported (at least yet). No threads to the cylindrical shape or spherical or general surface... Yeas there will be work-aroud with additional circles or datums or lines as hole axis, but again the final representation will be not exactly correct.

6. These problems are common for thread end too.

7. Hole to the thread will be not correct representation.

8. Icons are uggly. Who cares? It is just start of developement, icons are the last thing I care.

9. TechDraw problems. On the normal view, the thread major diameter is shown. It is not exactly according to ISO drawing standards, there is whole circle shown. Bigger problem is ViewSections. The ViewSections showns just bodies, faces and their edges are ignored. It means, the cosmetic thread is not shown on ViewSections at this moment.