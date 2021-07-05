# Bempp acoustics exercises

This repository contains tutorials and exercises designed to show you how to use Bempp to solve problems in acoustics.
These materials were designed to be part of the [EAA / UKAN Computational Acoustics Summer School](https://acoustics.ac.uk/events/4468/).
They have all been created in [Jupyter Notebooks](https://jupyter.org/), which allow you to see code, explanation and results all alongside.

The [tutorials](tutorials/) are complete notebooks that aim to demonstrate how to approach various types of problems using Bempp. The [exercises](exercises/) invite you to develop the notebooks to add new functionality, thereby developing your experitise in using Bempp.

You can view these tutorials and exercises [on nbviewer](https://nbviewer.jupyter.org/github/mscroggs/bempp-acoustic-tutorials/blob/main/README.ipynb) without needing to install Bempp. But if you wish to make any edits yourself, as is required to undertake the exercises, then you'll need to [install Bempp](tutorials/0_install.ipynb) and either clone the repository or download the code (achieved via the green <i>Code</i> button above right).

## Contents
- [Instructions for installing Bempp](tutorials/0_install.ipynb)
- Using the null field approach
  - [Tutorial 1: Scattering from a rigid sphere using a null field approach](tutorials/1_sphere_scatterer_null_field.ipynb)
  - [Exercise 1: Uniqueness](exercises/1_uniqueness.ipynb)
- Direct formulations
  - [Tutorial 2: Scattering from a rigid sphere using a direct formulation](tutorials/2_sphere_scatterer_direct.ipynb)
  - [Exercise 2: Scattering from a pressure-release sphere](exercises/2_sphere_scatterer.ipynb)
- Checking performance
  - [Tutorial 3: Convergence rates](tutorials/3_convergence.ipynb)
  - [Exercise 3: Iteration counts](exercises/3_iterations.ipynb)
- Impedence boundary conditions
  - [Tutorial 4: Scattering from a impedence sphere](tutorials/4_impedence_scattering.ipynb)
  - [Exercise 4: Different impedences](exercises/4_inverse_problem.ipynb)
- More example applications
  - [Tutorial 5: Loudspeaker](tutorials/5_loudspeaker.ipynb)
  - [Tutorial 6: FEM-BEM coupling with FEniCSx](tutorials/6_fenicsx.ipynb)
- [Further information](tutorials/7_more.ipynb)


## Please help us correct errors by reporting them:
If you spot an error in these tutorials and exercises, please report it
on the [GitHub issue tracker](https://github.com/mscroggs/bempp-acoustic-tutorials/issues).
You can also use the issue tracker to suggest any changes that you think would help
to make these tutorials and exercises clearer.

## Notation differences between these tutorials and the Bempp documentation
The bempp website includes a [handbook](https://bempp.com/handbook/index.html), which gives an introduction to how the library operates, and [automatically generated full Python documentation](https://bempp-cl.readthedocs.io/en/latest/), which is useful for looking up specific details once you already understand the main principles for using Bempp. But that documentation uses a different operator notation to what is used in these tutorials, which follow the Jonathan Hargreaves's slides from the summer school.

Here is a summary of the differences:

Operator | Notation used herein | Notation used in bempp documentation
-------- | -------------------- | ------------------------------------
Identity | I                    | Id
Single layer | S                | V
Double layer | D                | K
Adjoint double layer | A        | K'
Hypersingular | H               | W
