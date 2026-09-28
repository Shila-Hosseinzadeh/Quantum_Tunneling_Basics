
# QuantumATK for Quantum Transport

## Lesson 1 — Introduction to QuantumATK and Magnetic Tunnel Junctions

### English Audio Lecture Script

Hello everyone, and welcome to the first lesson of our course on QuantumATK for quantum transport and magnetic tunnel junction simulations.

In this course, our main goal is to learn how to use QuantumATK to study quantum transport in magnetic materials.

More specifically, we will eventually work with one of the most important magnetic tunnel junction systems:

**Fe, magnesium oxide, Fe — or Fe/MgO/Fe.**

We will start completely from the beginning.

So, if you have never used QuantumATK before, that is absolutely fine.

In this first lesson, we are not going to perform a complicated calculation.

Instead, we are going to build the conceptual foundation that we will need for the rest of the course.

---

## Part 1 — What is QuantumATK?

So, what exactly is QuantumATK?

QuantumATK is a computational platform that can be used to model atomic structures, electronic properties, and quantum transport in materials and nanoscale devices.

For our research, three concepts will be especially important.

The first one is **Density Functional Theory**, or DFT.

The second one is **spin-polarized electronic structure calculations**.

And the third one is the **Non-Equilibrium Green's Function formalism**, usually called NEGF.

These three ideas will appear repeatedly throughout this course.

But don't worry if NEGF or spin-polarized DFT sound complicated right now.

We will introduce them step by step.

Our final goal is not simply to learn how to click buttons in QuantumATK.

We want to understand what the software is actually calculating.

That distinction is very important for research.

---

## Part 2 — Our Research Problem

Let's look at the physical system that we eventually want to simulate.

Imagine two layers of iron separated by a very thin layer of magnesium oxide.

We can write this as:

**Fe / MgO / Fe.**

The two iron regions are magnetic.

The magnesium oxide layer acts as a tunneling barrier.

An electron coming from the left iron electrode can encounter this barrier.

Quantum mechanics tells us that the electron does not necessarily have to be reflected.

There can be a finite probability that it tunnels through the barrier.

This is the basic physical idea behind a magnetic tunnel junction.

Our computational problem is therefore:

How does an electron move through the Fe/MgO/Fe structure?

And how does this transport depend on energy, bias voltage, spin, and the magnetic configuration of the electrodes?

---

## Part 3 — The Overall Computational Workflow

To answer these questions, we will follow a sequence of calculations.

First, we need an atomic structure.

Then we calculate the electronic structure using DFT.

Because our system is magnetic, we need to take electron spin into account.

After that, when we want to study transport, we construct an open quantum device.

We then use the NEGF formalism to calculate quantum transport.

One of the most important quantities we will obtain is the transmission function.

We usually write it as:

**T of E.**

In other words, transmission as a function of energy.

From transport calculations, we can then calculate current and obtain current-voltage characteristics.

Finally, for a magnetic tunnel junction, we can compare different magnetic configurations and calculate quantities such as tunnel magnetoresistance, or TMR.

So our overall workflow is:

Atomic structure,

then DFT,

then electronic structure,

then spin,

then NEGF,

then transmission,

then current and I-V,

and finally TMR.

This workflow will become very familiar to you during the course.

---

## Part 4 — NanoLab

Now let's talk about the QuantumATK environment itself.

When you open QuantumATK, one of the main environments you will work with is called **NanoLab**.

NanoLab provides the graphical interface for working with QuantumATK.

In the beginning, this is where we will build structures, set up calculations, inspect our data, and visualize results.

A very simple way to remember our workflow is:

**Build, Calculate, Analyze.**

First, we build our model.

Second, we perform a calculation.

Third, we analyze the results.

Later, we will also learn how to perform many of these tasks using Python.

That will become particularly useful when we want to automate calculations or study several different MgO thicknesses.

---

## Part 5 — The Builder

One of the first tools you will use is called the **Builder**.

The Builder is where we construct and manipulate atomic structures.

For example, we might start by constructing bulk iron.

Then we can construct magnesium oxide.

Later, we will combine these materials to construct our Fe/MgO/Fe magnetic tunnel junction.

So, whenever you see the word "Builder", think:

**This is where I construct my atomic model.**

We will spend quite a bit of time in the Builder in the next few lessons.

---

## Part 6 — What is a BulkConfiguration?

Now we come to an important QuantumATK concept.

A crystal is periodic.

For example, an ideal iron crystal contains a huge number of iron atoms arranged in a repeating pattern.

We obviously cannot simulate an infinite crystal atom by atom.

Instead, we define a small repeating unit called a **unit cell**.

Then we tell the computer that this unit cell repeats periodically in space.

In QuantumATK, a periodic atomic structure is represented by a **BulkConfiguration**.

So remember this simple definition:

**BulkConfiguration means a periodic atomic structure.**

We will use BulkConfigurations to study materials such as bulk iron and bulk magnesium oxide.

---

## Part 7 — Why Do We Study Bulk Materials First?

You might ask:

Why don't we immediately build Fe/MgO/Fe?

The reason is that we need to understand the individual components first.

We will first study bulk iron.

Then we will study bulk magnesium oxide.

After that, we can investigate the interface between iron and magnesium oxide.

And finally, we will construct the complete Fe/MgO/Fe device.

So our progression is:

**Fe bulk,**

then **MgO bulk,**

then the **Fe/MgO interface,**

and finally **Fe/MgO/Fe.**

This step-by-step approach is important because it allows us to understand where the properties of the final device come from.

---

## Part 8 — Bulk Configuration versus Device Configuration

There is another important distinction that you should learn today.

A **BulkConfiguration** describes a periodic material.

A transport calculation is different.

For transport, we have an open system with a left electrode, a central region, and a right electrode.

This is represented by a **DeviceConfiguration**.

Conceptually, we can write it as:

Left Electrode,

Central Region,

and Right Electrode.

For our magnetic tunnel junction, the picture becomes:

**Fe electrode, MgO barrier, Fe electrode.**

The two Fe regions act as the electrodes, while MgO forms the tunneling barrier.

This distinction between bulk and device configurations will become extremely important when we start learning NEGF.

---

## Part 9 — Why Do We Need NEGF?

Now let's ask an important physics question.

Why can't we simply use DFT and calculate everything?

DFT is extremely useful for calculating electronic structure and many ground-state properties.

But a transport problem is different.

In a transport problem, electrons are coming from one side of the system and leaving through the other side.

So we have an open quantum system.

We can imagine it as:

An electron reservoir,

then the left Fe electrode,

then the MgO barrier,

then the right Fe electrode,

and finally another electron reservoir.

This is where the **Non-Equilibrium Green's Function**, or NEGF, formalism becomes important.

NEGF provides a framework for calculating quantum transport through open systems.

One of the most important quantities we will calculate is the transmission function:

**T of E.**

Transmission tells us how effectively electronic states can pass through the device at a given energy.

Later, we will study transmission in much more detail.

---

## Part 10 — Magnetic Tunnel Junctions

Now let's introduce the magnetic part of our problem.

Our system is:

**Fe / MgO / Fe.**

The two iron electrodes are magnetic.

Their magnetizations can be oriented in different ways.

The first important configuration is called the **parallel configuration**.

In the parallel configuration, the magnetizations point in the same direction.

We can represent this simply as:

up, up.

The second configuration is called the **antiparallel configuration**.

Here, the magnetizations point in opposite directions.

We can represent it as:

up, down.

The difference between transport in these two configurations is central to the physics of magnetic tunnel junctions.

It is also the basis for tunnel magnetoresistance, or TMR.

Later in this course, we will calculate transport for both configurations and compare them quantitatively.

---

## Part 11 — What Will We Learn in This Course?

So, where are we going from here?

We will start with the QuantumATK environment and the NanoLab interface.

Then we will learn how to construct atomic structures.

We will study crystal lattices, unit cells, and periodic boundary conditions.

After that, we will learn the basics of DFT calculations.

We will calculate electronic structures, band structures, density of states, and related quantities.

Then we will introduce spin-polarized calculations.

After that comes the most important part for quantum transport:

NEGF.

We will learn about electrodes, the central region, transmission, and transport calculations.

Then we will construct the Fe/MgO/Fe magnetic tunnel junction.

Finally, we will calculate transmission, current-voltage characteristics, parallel and antiparallel transport, and tunnel magnetoresistance.

Once we are comfortable with these topics, we can move to more advanced research topics.

These include k-resolved transmission, Δ1 symmetry, interface states, spin-dependent transport, spin-transfer torque, convergence studies, and Python automation.

---

## Part 12 — Your First Exercise

For today's exercise, I want you to do something very simple.

Open QuantumATK NanoLab.

Create a new project.

Give the project the name:

**MTJ_QuantumATK.**

Then open the Builder.

Do not perform a DFT calculation yet.

For now, simply explore the interface.

Look at the different panels and tools.

Don't worry if some of the options seem unfamiliar.

You are not expected to understand everything in the first lesson.

The purpose of today's lesson is to become familiar with the environment and, more importantly, to understand the physical and computational roadmap.

In the next lesson, we will start doing something concrete.

We will construct our first bulk iron structure.

We will learn what a unit cell is, what a lattice is, and how periodic boundary conditions are represented in QuantumATK.

And from that point onward, the course will become increasingly hands-on.

Welcome to QuantumATK.

Let's begin.
