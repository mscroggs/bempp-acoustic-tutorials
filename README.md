# Bempp acoustics exercises

This repository contains tutorials and exercises designed to show you how to use Bempp to solve problems in acoustics.
These materials were designed to be part of the [EAA / UKAN Computational Acoustics Summer School](https://acoustics.ac.uk/events/4468/).

You can view these exercises [on nbviewer](https://nbviewer.jupyter.org/github/mscroggs/bempp-acoustic-tutorials/blob/main/README.ipynb).

## Contents
- Scattering from a rigid obstacle
  - [Tutorial 1: Rigid scattering with Neumann conditions](tutorials/1_sphere_scatterer.ipynb)
  - [Exercise 1a: Rigid scattering with Dirichlet conditions](tutorials/1_sphere_scatterer.ipynb)
  - [Exercise 1b: Uniqueness](tutorials/1_sphere_scatterer.ipynb)

## Scattering from a rigid obstacle
The [first tutorial](tutorials/1_sphere_scatterer.ipynb)
demonstrates two possible approaches for solving a rigid exterior scattering problem.

This tutorial should be used to complete the following exercises:

- [Dirichlet conditions](exercises/1a_sphere_scatterer.ipynb).
  In this exercise, you will write your own code to solve a scattering problem with different boundary conditions to the tutorial.
- [Uniqueness](exercises/1b_uniqueness.ipynb).
  In this exercise, you will investigate the effect of resonances on the solutions of boundary integral equations.
