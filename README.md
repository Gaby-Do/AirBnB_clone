# Stacks, Queues - LIFO, FIFO

![image](https://github.com/BergeDios/AirBnB_clone/blob/gaby/boceto_casa.jpg)

We are Software Engineer students at  [Holberton School](https://www.holbertonschool.com/) and as part of our trip we have to create an AirB&B clone. At this step we´ll be working on the console step.


![GitHub last commit](https://img.shields.io/github/last-commit/BergeDios/AirBnB_clone)
![GitHub code size in byteg](https://img.shields.io/github/languages/code-size/BergeDios/AirBnB_clone)
![Lines of code](https://img.shields.io/tokei/lines/github/BergeDios/AirBnB_clone)


## Project scope
- Implement the push and pall opcodes: The opcode push pushes an element to the stack and the opcode pall prints all the values on the stack, starting from the top of the stack.
- Implement the pint opcode: The opcode pint prints the value at the top of the stack, followed by a new line.
- Implement the pop opcode: The opcode pop removes the top element of the stack.
- Implement the swap opcode: The opcode swap swaps the top two elements of the stack.
- Implement the add opcode: The opcode add adds the top two elements of the stack.
- Implement the nop opcode: The opcode nop doesn’t do anything.
- Implement the sub opcode: The opcode sub subtracts the top element of the stack from the second.
- Implement the div opcode: The opcode div divides the second top element of the stack by the top element.
- Implement the mul opcode: The opcode mul multiplies the second top element of the stack with the top element.
- Implement the mod opcode: The opcode mod computes the rest of the division of the second top element by the top element. 

## General Requirements
- Allowed editors: vi, vim, emacs
- All files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=c90
- All  files should end with a new line
- A README.md file, at the root of the folder of the project is mandatory
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You allowed to use a maximum of one global variable
- No more than 5 functions per file
- You are allowed to use the C standard library
- The prototypes of all your functions should be included in your header file called monty.h
- All your header files should be include guarded

## Given data structure
![image](https://github.com/Gaby-Do/monty/blob/master/images/estructura.png)

## Projects files structure

### Header 
In the header (monty.h) you can find, on one hand all the libraries used, as well as the prototype of all the functions developed for the purpose of this project. And on the other hand you can find the declaration of the used environment variables and the data structures 

### Main
here (monty.c)is the core code of the project.

### Opcode implementations 
In these files you can find the functions developed for the opcode implementation.

### Auxiliary functions
All other functions we needed for running the project.

## Compilation
This project  was compiled this way:

```
$ gcc -g -Wall -Werror -Wextra -pedantic -std=c90 *.c -o monty
```
#### Authors: 
@ [Gabriela Dominguez](https://github.com/Gaby-Do) &  [Marcela Carrasco](https://github.com/mcarrascopiaggio)





