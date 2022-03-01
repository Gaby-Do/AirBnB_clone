#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    
    def check_args(self, line):
        args = line.split()
        class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if len(args) == 0:
            print('** class name missing **')
            return
        if args[0] not in class_list:
            print("** class doesn't exist **")
            return
        return args

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """
        Creates new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = self.check_args(line)
        if args:
            my_obj = eval(args[0])()
            my_obj.save()
            print(my_obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = self.check_args(line)
        if args:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                obj_id = args[0]+'.'+args[1]
                all_obj = storage.all()
                if obj_id in all_obj.keys():
                    obj = all_obj[obj_id]
                    print(obj)
                else:
                    print('** no instance found **')
                    return
           
    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save change into JSON file)
        """
        args = self.check_args(line)
        if args:
            if not args[1]:
                print('** instance id missing **')
            else:
                obj_id = args[0]+'.'+args[1]
                all_obj = storage.all()
                if obj_id in all_obj.keys():
                    all_obj.pop(obj_id)
                else:
                    print('** no instance found **')
                    return

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name.
        """
        print_list = []
        args = line.split()
        class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
        if args:
            if args[0] in class_list:
                all_obj = storage.all()
                for key, obj in all_obj.items():
                    if args[0] in key:
                        print_list.append(obj.__str__())
                print(print_list)
            else:
                print("** class doesn't exist **")
            
        else:    
            all_obj = storage.all()
            for key, obj in all_obj.items():
                print_list.append(obj.__str__())
            print(print_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id\nby adding or updating attribute (save the change into the JSON file)
        """
        args = self.check_args(line)
        if args:
            if len(args) < 2:
                print('** instance id missing **')
                return
            elif len(args) < 3:
                print('** attribute name missing **')
                return
            elif len(args) < 4:
                print('** value missing **')
                return
            else:
                obj_id = args[0]+'.'+args[1]
                all_obj = storage.all()
                if obj_id in all_obj.keys():
                    obj = all_obj[obj_id]
                    setattr(obj, args[2], args[3].strip('"'))
                    obj.save()

                else:
                    print('** no instance found **')

        #check_att_name(args[2])
        #check_att_value(args[3])



   





if __name__ == '__main__':
    HBNBCommand().cmdloop()
