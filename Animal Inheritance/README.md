# Animal Inheritance

Company| iPsY
---|---
Date|11/8/2018
Platform|HackerRank

In this challange, you will be asked to build on an abstract class and initialize an instance of each class with a variable. The program will then test your implementation by retrieving the data you stored.

The locked code in the editor does the following:
1. Declares an abstract class named `Animal` with the implementations for `getIsMammal()`and `getIsCarnivorous()` methods, as well as an abstract method named `getGreeting()`.
2. Creates _Dog, Cow,_ and _Duck_ objects.
3. Calls the `getIsMammal()`, `getIsCarnivorous()`, and `getGreeting()` methods on each of these respective objects.

Consider the following UML diagram:

Complete the code in the editor below to implement the following:
1. Three classes named `Dog`, `Cow`, and `Duck` that inherit from `Animal` class.
2. No-argument constructors for each class that initialize the instance variables inherited from the superclass.
3. Each class must implement the `getGreeting()`method:
  * For a _Dog_ object, this must return the string `ruff`.
  * For a _Cow_ object, this must return the string `moo`.
  * For a _Duck_ object, this must return the string `quack`.

#### Input Format
There is no input for this challange.

#### Output Format
The `getGreeting()`method must always return a string denoting the appropriate greeting for the implementing class.