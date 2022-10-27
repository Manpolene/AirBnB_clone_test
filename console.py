#!/usr/bin/python3
'''Command Line Interpreter'''
import cmd
from models import storage
from models import *

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, *args):
        '''End of file command to exit the program'''
        return True

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        quit()
    
    def do_create(self, line):
        '''Create a new instance called <name>'''
        if line != "" or line is not None:
            if line not in storage.classes():
                print("** class doesn't exist **")
            else:
                # create an instance of the given class
                obj_intance = storage.classes()[line]()
                obj_intance.save()
                print(obj_intance.id)
        else:
            print("** class name missing **")
    
    def do_show(self, line):
        # check if class name and instance id was provided
        if line == "" or line is None:
            print("** class name missing **")
        
        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        print(instance_dict)
                    
                else:
                    print("** class doesn't exist **")

    def do_delete(self, line):
        # check if class name and instance id was provided
        if line == "" or line is None:
            print("** class name missing **")
        
        else:
            # get all the arguments passed via the command line
            class_info = line.split(" ")
            if len(class_info) < 2:
                print("** instance id missing **")
            else:
                class_name = class_info[0]
                instance_id = class_info[1]
                # check if class name exists
                if class_name in storage.classes():
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        # delete this instance and save to json
                        del storage.all()[key]
                        storage.save()
                        return
                        
                    
                else:
                    print("** class doesn't exist **")

    def do_all(self, line):
        instance_obj = storage.all()
        instance_list = []
        
        if line == "" or line is None:
            for key, value in storage.all().items():
                instance_list.append(str(value))
            print(instance_list)

        else:
            if line not in storage.classes():
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    class_name, instance_id = key.split(".")
                    if line == class_name:
                        instance_list.append(str(value))
                print(instance_list)

    def do_update(self, line):
        args = line.split(" ")
        if line == "" or line is None:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) > 3:
            (class_name, instance_id, attribute, value) = line.split(" ")
            # print(class_name, instance_id, attribute, value)
            #  check if class exists
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                key = f"{class_name}.{instance_id}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    instance_dict = storage.all()[key]
                    # remove quotation marks on value
                    value = value.replace('"', '')
                    # update attributes in the instance dictionary
                    instance_dict[attribute] = type(attribute)(value)
                    print(type(attribute), type(value))
                    storage.save()

    def emptyline(self):
        pass
    
    #  for testing purposes
    def onecmd(self, line):
        if "." in line:
            class_name, command = line.split(".")
            command = command.replace("(", "").replace(")", "")
            line = f"{command} {class_name}"
        return cmd.Cmd.onecmd(self, line)
        # print(line)

    def do_count(self, line):
        # line => User
        count = 0
        for key in storage.all().keys():
            class_name, instance_id = key.split(".")
            if line == class_name:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()