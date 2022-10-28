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


    def onecmd(self, line):
        # check if this line matches the given pattern
        if re.match(r"^(\w+)\.(\w+)\(:?.*\)$", line) is not None:
            # print("There was a match")
            # let's break line into class name and command_line
            line = re.split(r"^(\w+)\.(\w+\(.*\))$", line)
            class_name, command_line = line[1], line[2]
            # print(class_name, command_line)

            #  check what type of command was passed
            if command_line[:3] == "all" or command_line[:5] == "count":
                command = command_line.replace("(", "").replace(")", "")
                line = f"{command} {class_name}"
                # print(line)
            elif command_line[:4] == "show" or command_line[:7] == "destroy":
                # replace (" and ") from the command
                command = command_line.replace('("', ' ').replace('")', '')
                #  split the above command into the command and the id
                command, instance_id = command.split(" ")
                #  generate the actual line (command class_name id)
                line = f"{command} {class_name} {instance_id}"
            elif command_line[:6] == "update":
                # which update format was used
                if re.match(r"^(\w+\(.*\{.*\}\))$", command_line):
                    #  using the dictionary format
                    print(command_line)
                    command_line = re.split(r"^(\w+)\([\"\']([a-zA-Z0-9\-]+)[\"\']\,\s(\{[\'a-zA-Z\_\s\:\"\,0-9]+\})$", command_line)
                    print(command_line)
                    # command, instance_id, update_dict = class_name[1], class_name[2], class_name[3]
                    # line = f"{command} {class_name} {instance_id} {update_dict}"
                    # print(line)

                else:
                    # using the regular update format
                    command_line = re.split(r"^(\w+)\([\"\'](.+?)[\"\']\,\s?[\"\'](.+?)[\"\']\,\s?[\"\']?(.+?)[\"\']?\)$", command_line)
                    # print(command_line)

                    command, instance_id, attribute, value = command_line[1], command_line[2], command_line[3], command_line[4]
                    line = f"{command} {class_name} {instance_id} {attribute} {value}" 
                    print(line) 
            # return cmd.Cmd.onecmd(self, line)
        else:
            # return the default onecmd implementation
            # return cmd.Cmd.onecmd(self, line)
            print("There was no match")
