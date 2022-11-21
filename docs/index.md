# Welcome to gcp-fastapi!

This documentation will try to convey the usage of gcp-fastapi.

It is written in mkdocs material, for full documentation visit [mkdocs.org](https://www.mkdocs.org).

##### Mkdocs Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

Wondering where to put which script? Use this as a rough guide. Keep the amounts of folders as low as possible and as
high as necessary!

## Project Structure

The idea is to keep the models and their training per parameter combination separate to enable parallelization of the
computations.

## Programming principles

* Keep the ==models separated==! ^^***This is non negotiable!***^^
* When adjusting the code (variable name changes, input is slightly different) we only want to ==change **ONE**== place
  in
  the code!
* Represent ==string options as Enums== to get rid of typos!
* Keep the ==model structure as uniform== as possible!
* Keep the ==inputs as few== as possible!
* Adhere to ==naming conventions==!
* Comment with ==docstrings==!
* Update the ==documentation==!
* Write ==tests==!

## Where to start?

A good place to start coding is the [personalisation script](tutorials/personalisation.md)  
A good place to start using is the [how to script](tutorials/how_to_use.md)
