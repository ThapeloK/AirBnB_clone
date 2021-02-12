# 0x00. AirBnB clone - The console

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/ThapeloK/AirBnB_clone)

## Description
The goal of the project is to deploy on the server a simple copy of the AirBnB website.The web application is composed of the following:

- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) that show the final product to everyone: static and dynamic
- A database or files that store data
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete and update them)

******************************************************************************

Table of contents
=================

<!--ts-->
   * [Description](#description)
   * [Table of contents](#table-of-contents)
   * [General](#general)
   * [Classes](#classes)
   * [Steps](#steps)
   * [Execution](#execution)
   * [Final Product](#final-product)
   * [Author](#author)
<!--te-->

******************************************************************************

## General 

What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

******************************************************************************
## Classes

******************************************************************************

## Steps

* Create a data model
* Manage (create, update, destroy, etc) objects via a console/command interpreter
* Store and persist objects to files (JSON files)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between objects and How they are stored and persisted. 

![Image of hbnb](https://github.com/ThapeloK/AirBnB_clone/blob/main/assets/console.png)

### Execution
Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Final Product

![Image of hbnb](https://github.com/ThapeloK/AirBnB_clone/blob/main/assets/Finalairbnb.png)


******************************************************************************

## Authors
* **Thapelo** - [ThapeloK](https://github.com/ThapeloK/)
* **Lilian** - [Lilieyen](https://github.com/Lilieyen)
