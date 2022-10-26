#!/usr/bin/python3
'''Command Line Interpreter'''
import cmd
from models import storage
from models import base_model, FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes_list = ["BaseModel"]

    def do_EOF(self, *args):
        '''End of file command to exit the program'''
        return True

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        return True
    
    def do_create(self, class_name):
        '''Create a new instance called <name>'''
        if class_name:
            if class_name == "BaseModel":
                class_name = base_model.BaseModel()
                class_name.save()
                object_dict = class_name.__dict__
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
                    # object_received = storage.all()

                    # for obj_id in object_received.keys():
                    #     if obj_id == key:
                    #         obj = object_received[obj_id]
                    #         print(obj)
                    #         return
                    # print("** no instance found **")
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        instance_dict = storage.all()[key]
                        # print the str representation of the instance
                        print(f"[{class_name}] ({instance_id}) {str(instance_dict)}")
                    
                else:
                    print("** class doesn't exist **")


    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()