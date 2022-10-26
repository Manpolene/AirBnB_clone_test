#!/usr/bin/python3
'''Command Line Interpreter'''
import cmd
from models import *
from models import base_model

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    
    def do_EOF():
        '''End of file command to exit the program'''
        return True

    def do_quit(self, *args):
        '''Quit command to exit the program'''
        return True
    
    def do_create(self, BaseModel):
        if BaseModel:
            BaseModel = base_model.BaseModel()
            BaseModel.save()
            object_dict = BaseModel.__dict__
            print(object_dict['id'])
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()