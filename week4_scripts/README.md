# Intermediate Python - Week 4

## Goals
-----
* This week, we will transition away from writing code in Jupyter Notebooks and start writing standalone programs you can run from the command line
* Introduction to isolated python environments using virtualenv
* Introduction to PyCharm and IDEs

Whilst Jupyter notebooks are great for exploring ideas and initial development, they have their limitations, and at some point, you're going to want to convert your code to a standalone `.py` file that you can run from the command line.
This week, we're going to transition away from from Jupyter notebooks and get comfortable writing programs that you can run from the command line

Some prerequisites:
* Install PyCharm community and Python 3.9 from the software store
* Follow the installation instructions documentation in this folder to get up and running

## Writing Python scripts from scratch

### Introduction:
* Setting up your folder
* Creating an isolated virtual environment
* Installing some packages: scipy, scikit-learn, matplotlib, numpy, pandas
* Creating and editing files in PyCharm
* Running your program from a terminal

### 'Hello World' as a standalone program

* Exercise 1: write a standalone python script that takes two random numbers and returns their product

### Passing arguments from the command line with `sys.argv`

* Exercise 2: Write and execute a program that takes some numbers as arguments from the command line and calculates their sum

### Argparse: A library for parsing arguments


* Exercise 3: Use the argparse library to pass two numbers to your `main` function and return their average


### Going deeper into the argparse library
  * Positional arguments, defaults, data types, actions
  
* Exercise 4: Write a script that takes the path (or url) to the metabric dataset we used earlier in the course, read it in using pandas, and print some summary statistics (the data can be found here
  https://raw.githubusercontent.com/AstraZeneca-Code-Club/intermediate_python/main/metabric_clinical_and_expression_data.csv)

* Exercise 5/Extension/Homework: Extend the function you wrote above to add a seaborn plot 

