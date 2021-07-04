# Bempp acoustics exercises

This repository contains tutorials and exercises designed to show you how to use Bempp to solve problems in acoustics.
These materials were designed to be part of the [EAA / UKAN Computational Acoustics Summer School](https://acoustics.ac.uk/events/4468/).

You can view these tutorials and exercises [on nbviewer](https://nbviewer.jupyter.org/github/mscroggs/bempp-acoustic-tutorials/blob/main/README.ipynb).

## Contents
- [Instructions for installing Bempp](tutorials/0_install.ipynb)
- Using the null field approach
  - [Tutorial 1: Scattering from a rigid sphere using a null field approach](tutorials/1_sphere_scatterer_null_field.ipynb)
  - [Exercise 1: Uniqueness](exercises/1_uniqueness.ipynb)
- Direct formulations
  - [Tutorial 2: Scattering from a rigid sphere using a direct formulation](tutorials/2_sphere_scatterer_direct.ipynb)
  - [Exercise 2: Scattering from a pressure-release sphere](exercises/2_sphere_scatterer.ipynb)
- Impedence boundary conditions
  - [Tutorial 3: Scattering from a impedence sphere](tutorials/3_impedence_scattering.ipynb)
  - [Exercise 3: Different impedences](exercises/3_impedences.ipynb)
- Checking performance
  - [Tutorial 4: Convergence rates](tutorials/4_convergence.ipynb)
  - [Exercise 4: Iteration counts](exercises/4_iterations.ipynb)
- More example applications
  - [Tutorial 5: Loudspeaker](tutorials/5_loudspeaker.ipynb)
  - [Tutorial 6: FEM-BEM coupling with FEniCSx](tutorials/6_fenicsx.ipynb)
- [Further information](tutorials/7_more.ipynb)

## Things we're still working on:
- [Tutorial 3: Scattering from a impedence sphere](tutorials/3_impedence_scattering.ipynb)
  - The text at the top needs updating (currently copied from example 1)
  - Correctness and choice of parameters need checking
- [Exercise 3: Different impedences](exercises/3_impedences.ipynb)
  - This needs writing

## Please help us correct errors by reporting them:
If you spot an error in these tutorials and exercises, please report it
on the [GitHub issue tracker](https://github.com/mscroggs/bempp-acoustic-tutorials/issues).
You can also use the issue tracker to suggest any changes that you think would help
to make these tutorials and exercises clearer.

## Notation differences between these tutorials and exercises and the bempp documentation
The bempp website includes a [handbook](https://bempp.com/handbook/index.html), which gives an introduction to how the library operates, and [automatically generated full Python documentation](https://bempp-cl.readthedocs.io/en/latest/), which is useful for looking up specific details once you already understand the main principles for using bempp. But that documentation uses a different operator notation to what is used in these tutorials, which follow the Jonathan Hargreaves's slides from the summer school.

Here is a summary of the differences:
<table>
  <tr>
    <td>Operator</td>
    <td>Notation used herein</td>
    <td>Notation used in bempp documentation</td>
  </tr>
  <tr>
    <td>Identity Operator</td>
    <td>I</td>
    <td>Id</td>
  </tr>
  <tr>
    <td>Single Layer Potential</td>
    <td>S</td>
    <td>V</td>
  </tr>
  <tr>
    <td>Double Layer Potential</td>
    <td>D</td>
    <td>K</td>
  </tr>
  <tr>
    <td>Adjoint Double Layer Potential</td>
    <td>A</td>
    <td>K'</td>
  </tr>
  <tr>
    <td>Hypersinglar Operator</td>
    <td>H</td>
    <td>W</td>
  </tr>
</table>
