#!/usr/bin/python3
'''Command Line Interpreter'''
import cmd
from models import storage
from models import *
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes_list = ["BaseModel", "User"]

    def do_EOF(self, *args):
        '''End of file command to exit the program'''
        return True

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        quit()
    
    def do_create(self, class_name):
        '''Create a new instance called <name>'''
        if class_name:
            if class_name in self.classes_list:
                class_instance = eval(class_name)()
                class_instance.save()
                object_dict = class_instance.__dict__
                print(object_dict['id'])
            else:
                print("** class doesn't exist **")
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
                if class_name in self.classes_list:
                    # check if instance_id exists
                    key = f"{class_name}.{instance_id}"
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        # print the str representation of the instance
                        print(f"[{class_name}] ({instance_id}) {str(instance_dict)}")
                    
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
                if class_name in self.classes_list:
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
        
        if line:
                if line not in self.classes_list:
                    print("** class doesn't exist **")
                    return
                else:
                    for key in instance_obj.keys():
                         # split key into class name and instance id
                        class_name, instance_id = key.split(".")
                        if line == class_name:
                            instance_dict = instance_obj[key]
                            # # print the str representation of the instance
                            instance_list.append(str(f"[{class_name}] ({instance_id}) {str(instance_dict)}"))
                            print(instance_list)
                            
        else:
            # grab each intance and format for printing
            for key in instance_obj.keys():
                #  check if class was provided
                # if line is not "" or line is not None:

                # split key into class name and instance id
                class_name, instance_id = key.split(".")
                # print(class_name, instance_id)
                instance_dict = instance_obj[key]
                # # print the str representation of the instance
                instance_list.append(str(f"[{class_name}] ({instance_id}) {str(instance_dict)}"))
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
            if class_name not in self.classes_list:
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()