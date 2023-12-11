#!/usr/bin/python3
"""
Console module
"""
import sys
import cmd
import shlex
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class console for user interaction
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def emptyline(self):
        """
        Emptyline method
        """
        # print('emptyline()')
        # return cmd.Cmd.emptyline(self)
        pass

    def precmd(self, line):
        """
        Method precmd for reformation the given input
        Args: line
        """
        if "." in line:
            match_1 = re.match(r'(\w+)\.show\("([^"]+)"\)', line)
            match_2 = re.match(r'(\w+)\.destroy\("([^"]+)"\)', line)
            if match_1:
                class_name = match_1.group(1)
                instance_id = match_1.group(2)
                # print(f"Class Name: {class_name}")
                # print(f"Instance ID: {instance_id}")
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                line = line.split(" ")
                line = f"{line[1]} {line[0]}"
                # print(line)
                lines = line.split("\"")
                new = f'{lines[0]} {class_name} {instance_id}'
                # print(new)
                return cmd.Cmd.precmd(self, new)
            elif match_2:
                class_name = match_2.group(1)
                instance_id = match_2.group(2)
                # print(f"Class Name: {class_name}")
                # print(f"Instance ID: {instance_id}")
                line = line.replace(".", " ").replace("(", "").replace(")", "")
                line = line.split(" ")
                line = f"{line[1]} {line[0]}"
                # print(line)
                lines = line.split("\"")
                new = f'{lines[0]} {class_name} {instance_id}'
                # print(new)
                return cmd.Cmd.precmd(self, new)

            line = line.replace(".", " ").replace("(", "").replace(")", "")
            line = line.split(" ")
            line = f"{line[1]} {line[0]}"
            # print(line)
        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """
        Method to create a new instance
        """
        if line:
            try:
                create = eval(line)()
                create.save()
                print(create.id)
            except NameError:
                print("** class doesn't exist **")
        print("** class name missing **")

    def do_show(self, line):
        """
        Method to show attributes of an instance
        """
        arguments = shlex.split(line)

        if not arguments or len(arguments) < 1:
            print("** class name missing **")

        elif arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(arguments) == 1 and arguments[0] in HBNBCommand.classes:
            print("** instance id missing **")
        else:
            dictionary = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in dictionary:
                print("** no instance found **")
            else:
                print(dictionary[key])

    def do_destroy(self, line):
        """
        Method that delete an instance based on the id and class name
        """
        arguments = shlex.split(line)
        if not arguments or len(arguments) < 1:
            print("** class name missing **")

        elif arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(arguments) == 1 and arguments[0] in HBNBCommand.classes:
            print("** instance id missing **")
        else:
            new_dict = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in new_dict:
                print("** no instance found **")
            else:
                del new_dict[key]
                storage.save()

    def do_all(self, line):
        """
        Method that show all instance with their attributes
        """
        arguments = shlex.split(line)

        string = []
        dictionary = storage.all()
        if not line:
            for key, value in dictionary.items():
                string.append(str(value))
            print(string)

        else:
            if arguments[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for key, value in dictionary.items():
                if key.split('.')[0] == arguments[0]:
                    string.append(str(value))
            print(string)

    def do_update(self, line):
        """
        Method to update or add a new attribute
        """
        arguments = shlex.split(line)
        if not arguments or len(arguments) < 1:
            print("** class name missing **")

        elif arguments[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif arguments[0] in HBNBCommand.classes and len(arguments) == 1:
            print("** instance id missing **")
        elif arguments[0] in HBNBCommand.classes and len(arguments) == 2:
            print("** attribute name missing **")
        elif arguments[0] in HBNBCommand.classes and len(arguments) == 3:
            print("** value missing **")
        else:
            dictionary = storage.all()
            key = "{}.{}".format(arguments[0], arguments[1])
            if key not in dictionary:
                print("** no instance found **")

            # update BaseModel id attr_name value
            # setattr(obj, attribute_name, value
            # ex:    obj = BaseModel()
            #        obj.name = "Betty"
            # ===>   setattr(obj, name, value)
            instance = dictionary[key]
            attribute_name = arguments[2]
            if attribute_name not in ["id", "created_at", "updated_at"]:
                # if not arguments[3]:
                #    print("** value missing **")
                value = arguments[3]
                try:

                    value = type(getattr(instance, attribute_name))(value)
                except AttributeError:
                    pass
                setattr(instance, attribute_name, value)
                instance.save()

    def do_count(self, line):
        """
        Method that count the number of instance of a class
        """
        # count BaseModel
        arguments = shlex.split(line)
        class_name = arguments[0]
        # let's load all instances have been created
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            dictionnary = storage.all()
            count = 0
            for key in dictionnary:
                if key.split(".")[0] == class_name:
                    count += 1
            print(count)

    def do_EOF(self, line):
        """EOF  help  quit

        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program

        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
