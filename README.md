# Python Practice Tasks

This is a compilation of python scripts done during 2020 while learning Python with the JetBrains course. These were uploaded initially to github each one as a single repository, so I thought it would make more sense to have them grouped in a single repository

# 1. Python Coffee Machine
Python Coffee Machine project from JetBrains Academy

Description
Let's redesign our program and write a class that represents the coffee machine. The class should have a method that takes a string as input. Every time the user inputs a string to the console, the program invokes this method with one argument: the line that user input to the console. This system simulates pretty accurately how real-world electronic devices work. External components (like buttons on the coffee machine or tapping on the screen) generate events that pass into the single interface of the program.

The class should not use system input at all; it will only handle the input that comes to it via this method and its string argument.

The first problem that comes to mind: how to write that method in a way that it represents all that coffee machine can do? If the user inputs a single number, how can the method determine what that number is: a variant of coffee chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?

The right solution to this problem is to store the current state of the machine. The coffee machine has several states it can be in. For example, the state could be "choosing an action" or "choosing a type of coffee". Every time the user inputs something and a program passes that line to the method, the program determines how to interpret this line using the information about the current state. After processing this line, the state of the coffee machine can be changed or can stay the same.

Objective
Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method. Good luck!

Example
Your coffee machine should have the the same initial resources as in the example (400 ml of water, 540 ml of milk, 120 g of coffee beans, 9 disposable cups, $550 in cash.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

https://hyperskill.org/projects/68/stages/371/implement
