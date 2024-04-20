# CosmeticThread3D

Version: 0.2

**FreeCAD** version supported: **0.21.2 or higher**

Author: Martin Prokš

e-mail: martin.proks@proks-martin.cz

2024

Forum link: [[Feature discussion] Cosmetic thread - 3D geometry - FreeCAD Forum](https://forum.freecad.org/viewtopic.php?t=85047)

Git link: [GitHub: FreeCAD tool - cosmetic thread for 3D geometry - experimental](https://github.com/martinproks/cosmeticthread3d)

FreeCAD tool - cosmetic thread for 3D geometry - experimental.

This tool should make 3D representation and important parameters of cosmetic threads (internal and external) for standard threads to the FreeCAD.

Goal of this tool is not bring final version of the cosmetic threads (not yet), but explore ways how to do it and prepare background for more stable and good final implementation. There are 5 types of Part version of geometric representation of cosmetic thread. You can test each of them and select the one You prefer. **Please let feedback what type is the best in your opinion - what type to develop more and finally implement**.

![Cosmetic Thread 3D - internal and external examples](https://github.com/martinproks/cosmeticthread3d/blob/main/doc/img/test_2024-04-20.png?raw=true)

---

# How to use it

## Workbench installation

Find path to Your FreeCAD `Mod` directory. You can find it by typing command `App.getUserAppDataDir()` in the [Python console](https://wiki.freecad.org/Python_console "Python console").

Create folder `Mod/CosmeticThread3D` and copy there all data from this git repository.

Restart FreeCAD and the workbench should be there.

This tool is under developement. It is not usable for real work yet - some important interface parameters are changing or added or removed during the developement.

But testers and feedback from them is very helpfull and important. Please test it and left a feedback. Thanks.

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

This tool supports some types of threads. Metric Coarse, Metric Fine, UNC, UNF, BSW, G - pipe threads, ... Generally it could support any paralel thread type.

Tapered threads are not supported at this moment.

## Visual representation

There are more types of Cosmetic Threads for tests and comparison what type is the best for further implementation. Generally it is important  to see in 3D:

* Length of the thread.

* Major and minor diameters of the thread.

* Optionally some helpfull geometry to better visualisation of the thread (e.g. helix with correct pitch).

## FreeCAD geometric and parameter representation

### Geometric representation

There are two major versions of cosmetic thread. Part version and PartDesign version of cosmetic thread. Part version is based on non-solid geometry. It consist of shells and curves in 3D. PartDesign version is based on solid substractive feature.

### Parameters of FreeCAD thread feature

The cosmetic thread geometry is wrapped into one FreeCAD feature (python feature) with parameters for possibility to advanced usage - for example for TechDraw.

The parameters are:

* Thread designation (for example M10).

* Nominal thread diameter (for example 10 mm).

* Pitch (for example 1.5 mm).

* TPI - threads per inch (for example 16.933).

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

- `cosmeticthread3d_partdesign.py` - all the working code for console mode for PartDesign version of threads.

- `cosmeticthread3d_Gui.py` - GUI buttons and menus called from InitGui.py.

- `ct3dGuiTools.py` - tools for cosmeticthread3d_Gui.

- `MetricCoarse1st.py` - tabularized parameters for metric coarse threads, preffered selection (1st) according to ISO 261

- `MetricCoarse2nd.py`, `MetricCoarse3th.py`, `MetricFine1st.py`, `MetricFine2nd.py`, `MetricFine3th.py`, ... - basic geometrich parameters of the threads.

## Notes to implementation

There are more functions and classes for threads.

* **P0** - **Part** version, **type 0** of geometry representation.
  The whole work is based on Part objects and it is dedicated to be used on Part geometry. Do not mix it with PartDesign, there are non-compatible problems.

* **P1** - **Part** version, **type 1** of geometry representation.
  Simmilar as P0, but without the helix.

* **P2** - **Part** version, **type 2** of geometry representation.
  Thread is simulated by tube D-D1-length / D-d3-length.

* **P3 - Part** version, **type 3** of geometry representation.
  Outer and bottom shell of the thread as P1 type. Thread shape is **replaced** by **rotated zig-zag** profile (shell).

* **P4** - **Part** version, **type 4** of geometry representation.
  Shell with texture.

* **PD0** - **PartDesign** version, **type 0** of geometry representation.
  Geometric simmilar to P1. There are not shells, but verry thin gaps representing the thread.

Workbench for just two buttons does not make sense in the end. But for the developement of the tools it is most probably the easyest way how to do it. Someday in the future it will be good idea to merge it with some existing and more general work bench - Part or PartDesign I think. Or merge it with some other thread oriented work bench?

Notes specific to Part version of cosmetic threads: Each thread is separate Part object that could be inserted in a group Threads. It is easy to identify all threads and read their parameters, switch on/off all in once by Threads group. The main solid of the base part is not affected by the cosmetic threads - important for CAM and FEM. But TechDraw can not show shells at this moment.

Notes specific to PartDesign version of cosmetic threads: The cosmetic thread geometry is thin solid. Each cosmetic thread is normal feature in the modeling tree. Pros is, this approach is shown on TechDraw, even it is not correct according standards. Cons are two. Thread are burried inside the modeling tree and it is costs more efford to find them all. Second and more important, the cosmetic threads affects the base solid of part. Cosmetic thread is gap or crac - like geometry in the main body. It could be problem for CAM and FEM.

# Known issues

1. It will work just for simple holes perpendicular to starting plane. If the starting plane will be under angle to the hole axis, it will be a little bit wrong 3d representation.

2. Not plannar starting surface is not supported (at least yet). No threads to the cylindrical shape or spherical or general surface... Yeas there will be work-aroud with additional circles or datums or lines as hole axis, but again the final representation will be not exactly correct.

3. These problems are common for thread terminantion too.

4. Hole to the thread will be not correct representation.

5. Icons are uggly. Who cares? It is just start of developement, icons are the last thing I care.

6. TechDraw problems in Part version. On the normal view, the thread major diameter is shown. It is not exactly according to ISO drawing standards, there is whole circle shown. Bigger problem is ViewSections. The ViewSections showns just bodies, faces and their edges are ignored. It means, the cosmetic thread is not shown on ViewSections at this moment.

7. There is no python report what functions are called on background.

8. There is no language localization, it works in English only.
