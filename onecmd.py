#  for testing purposes
import re

def onecmd(self, line):
    if "." in line:
        line = re.split(r"(\w+)\.", line)
        print(line)
        return
        #  check what type of command was passed
        if command[:3] == "all" or command[:5] == "count":
            command = command.replace("(", "").replace(")", "")
            line = f"{command} {class_name}"
        elif command[:4] == "show" or command[:7] == "destroy":
            #  command = show(<id>)
            # replace (" and ") from the command
            command = command.replace('("', ' ').replace('")', '')
            #  split the above command into the command and the id
            command, instance_id = command.split(" ")
            #  generate the actual line (command class_name id)
            line = f"{command} {class_name} {instance_id}"
        elif command[:6] == "update":
            #  check which format of update was used
            if "{" in command:
                # (\w+)\.(\w+)\(\"([a-zA-Z0-9\-]+)\"\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})
                #  class_name command id dictionary
                #  <class name>.update(<id>, <dictionary representation>)
                # command = command.replace('("', ' ').replace(')', '')
                class_name = re.split(r"(\w+)\.(\w+)\(\"([a-zA-Z0-9\-]+)\"\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})", line)
                # command, instance_id = command_id.split(' ')
                class_name, command, instance_id, update_dict = class_name[1], class_name[2], class_name[3], class_name[4]

                print(class_name, command, instance_id, update_dict)

                for key, value in update_dict.items():
                    line = f"{command} {class_name} {instance_id} {key} {value}"
                    cmd.Cmd.onecmd(self, line)
                return
            # User.update("44006e6e-8cf7-4560-a22c-138125c159ca", {'id': "44006e6e-8cf7-4560-a22c-138125c159ca", "first_name": "Tony", "email": "obed@gmail.com"})

            else:
                # <class name>.update(<id>, <attribute name>, <attribute value>)
                command = command.replace('("', ' ').replace('")', '')

                command, instance_id, attr_name, value = re.split(' |", "', command)
                line = f"{command} {class_name} {instance_id} {attr_name} {value}"
    # return cmd.Cmd.onecmd(self, line)
    # print(line)
    # print(command, instance_id, attr_name, value )