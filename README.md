# cosmeticthread3d

Author: Martin Prokš

e-mail: martin.proks@proks-martin.cz

2024

 

FreeCAD tool - cosmetic thread for 3D geometry - experimental.

This tool should make 3D representation and important parameters of cosmetic threads (internal and external) for basic metric standard threads to the FreeCAD.

Goal of this macro is not bring final version of the cosmetic threads, but explore ways how to do it and prepare background for more stable and better codded solution. This macro is just first approach.

(I'm not a programmer, I'm a little bit fighting with python and GIT, be patient withg this code and with me please.)



## Main idea

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



## Plan of work

- Create PythonFeatures *CosmeticThread3DInternal* and *CosmeticThread3DExternal*. May be it could be good idea to simplify the names to *ct3di* and *ct3de*. These PythgonFeatures should hold the geometry of the cosmetic threads.

- Create small workbench *CosmeticThread3D* with GUI functions *Cosmetic Thread 3D Internal* and *Cosmetic Thread 3D External*. May be it could be good idea to simplify the names to *ct3digui* and *ct3degui*.








