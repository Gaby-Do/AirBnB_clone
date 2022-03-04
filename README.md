# AirBnB clone - The console

![image](https://github.com/BergeDios/AirBnB_clone/blob/gaby/5153a3c8fd500f43fc16854acb8c1ed0.jpg)

We are Software Engineer students at  [Holberton School](https://www.holbertonschool.com/) and as part of our trip we have to create an AirB&B clone. At this step we'll be writing a command interpreter to manage our AirBnB objects.


![GitHub last commit](https://img.shields.io/github/last-commit/BergeDios/AirBnB_clone)


## Project scope
This is the first step towards building our first full web application: the AirBnB clone.\
As part of it we will:
- Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances.
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- Create all unittests (at least we'll try) to validate all our classes and storage engine.

#### Through the command interpreter it's possible to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

#### Commands
- Type ./console.py to launch the command interpreter.
- create - Creates a new instance of the class.
-- Usage: create <class name> Ex: (hbnb) create BaseModel
- show - Prints an instance based on the class name and id.
-- Usage: show <class name> <id> Ex: (hbnb) show BaseModel 1234 or <class name>.show(<id>) Ex: BaseModel.show("1234")
- destroy - Deletes an instance based on the class name and id.
-- Usage: destroy <class name> <id> Ex: $ destroy BaseModel 1234 or <class name>.destroy(<id>) Ex: BaseModel.destroy("1234")
- all - Prints all instances based or not on the class name.
-- Usage: all <class name> or just all Ex: $ all BaseModel or $ all, also <class name>.all() Ex: BaseModel.all()
- update: Updates an instance based on the class name and id by adding or updating attribute.
-- Usage: update <class name> <id> <attribute name> "<attribute value>" Ex: $ update BaseModel 1234 email "aibnb@mail.com" or <class name>.update(<id>, <attribute name>, <attribute value>) Ex: BaseModel.update("1234", "año de construida", 2010)
- 
## General Requirements
- Editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Our code would use the pycodestyle (version 2.7.*)
- All classes and modules and functions will be documented
- Our command interpreter should work in interactive and non-interactive mode.

#### Authors: 
@ [Santiago Goyret](https://github.com/BergeDios) & [Gabriela Dominguez](https://github.com/Gaby-Do)

