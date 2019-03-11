# Eurocode-SS-EN-1995
The goal is to create a foundation that aids in creating software based around structural analysis of different materials according to eurocode.

Programming is not my main occupation so I am happy to recieve every opinion as to how this can be structured in a better way.

Some functions and notations is still written in Swedish and replacing all of these is an ongoing pursuit.

As it stands today the structure is based on the structure of the Eurocode itself in the main calculation area. A large portion of the calculations needed for basic wooden structures are functional and accessible via an API. Though many functions are still 
placeholders for the future and are planned to be completed as this project progresses. 

In addition to just calculation according to Eurocode, the plan is to create a geometric module in which you should be able to create
simple 3D-models from which the forces and dimensions are dervied from in the calculations. 

A stretch goal is to create a FEM-module which is capable of calculating the internal and shell forces in a non-linear manner to create a
more realistic distribution of the forces involved.
