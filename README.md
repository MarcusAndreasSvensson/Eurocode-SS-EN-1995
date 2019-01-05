# Eurocode-SS-EN-1995
The goal is to create a foundation that aids in creating software based around structural analysis of wooden structures.

Everything is written i python3 as it is the language I am most comfortable with, but other languages are welcome if, for example 
the performance is needed that isn't attainable in python. My original plan for this is to implement Cython when these kind of problems 
arises.

Programming is not my main occupation as is probably evident for the more experienced people viewing this repo. I invite every opinion
as to how this can be structured in a better way.

I think almost every comment and function name is written i Swedish and I regret doing this. From the beginning I didn't plan on
making this open-source, but realised the project have far worse chances of ever being complete if I don't ask for help. The swedish
notation is of course to the swapped for english counterparts to increase the availability for everyone who wants to participate.

As it stands today the structure is based on the structure of the Eurocode itself in the main calculation area. A large portion of the pure calculations are functional as a backend, but many functions are still 
placeholders for the future and is planned to be completed as this project progresses. 

In the future the goal is to expand this to not only calculate according to the wooden code, but to all the main building materials, steel
and concrete. Wood was chosen as it is the smallest of the codes.

In addition to just calculation according to Eurocode, the plan is to create a geometric module in which you should be able to create
simple 3D-models from which the forces and dimensions are dervied from in the calculations. 

A stretch goal is to create a FEM-module which is capable of calculating the internal and shell forces in a non-linear manner to create a
more realistic distribution of the forces involved.
