#!/usr/bin/python3
"""
Our cmd module
"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self) -> bool:
        pass

    def do_exit(self, arg):
        """
        Exits the program
        """
        return True

    do_EOF = do_exit

    def do_create(self, arg):
        """
        do_create- Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id. Ex: $ create BaseModel
        If the class name is missing, print-
        ** class name missing ** (ex: $ create)
        If the class name doesn’t exist, print-
        ** class doesn't exist ** (ex: $ create MyModel)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            temp = storage.classes()[arg]()
            temp.save()
            print(temp.id)

    def do_show(self,arg):
        """do_show- Prints the string representation of
        an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        If the class name is missing, print
        ** class name missing ** (ex: $ show)
        If the class name doesn’t exist, print
        ** class doesn't exist ** (ex: $ show MyModel)
        If the id is missing, print
        ** instance id missing ** (ex: $ show BaseModel)
        If the instance of the class name doesn’t exist for the id, print
        ** no instance found ** (ex: $ show BaseModel 121212)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """
        do_destroy- Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        If the class name is missing, print
        ** class name missing ** (ex: $ destroy)
        If the class name doesn’t exist, print
        ** class doesn't exist ** (ex:$ destroy MyModel)
        If the id is missing, print
        ** instance id missing ** (ex: $ destroy BaseModel)
        If the instance of the class name doesn’t exist for the id, print
        ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storge.all()[key]
                    storage.save()

    def do_all(self, arg):
        """
        do_all - Prints all string representation of
        all instances based or not on the class name. Ex: $ all BaseModel or $ all.
        The printed result must be a list of strings (like the example below)
        If the class name doesn’t exist, print
        ** class doesn't exist ** (ex: $ all MyModel)
        """
        if arg != "":
            words = arg.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist")
            else:
                for key, obj in storage.all().items():
                    new = str(obj)
                    if type(obj).__name__ == words[0]:
                        print(new)
        else:
            for key, obj in storage.all().items():
                new_list = str(obj)
                print(new_list)

    def do_update(self, arg):
        """
        do-update: Updates an instance based on the class name and id 
        by adding or updating attribute (save the change into the JSON file)
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        The attribute value must be casted to the attribute type
        If the class name is missing, print
        ** class name missing ** (ex: $ update)
        If the class name doesn’t exist, print
        ** class doesn't exist ** (ex: $ update MyModel)
        If the id is missing, print
        ** instance id missing ** (ex: $ update BaseModel)
        If the instance of the class name doesn’t exist for the id, print
        ** no instance found ** (ex: $ update BaseModel 121212)
        If the attribute name is missing, print
        ** attribute name missing ** (ex: $ update BaseModel existing-id)
        If the value for the attribute name doesn’t exist, print
        ** value missing ** (ex: $ update BaseModel existing-id first_name)
        """
        if arg != "":
            words = arg.split(' ')
            integers = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]
            floats = ["latitude", "longitude"]
            if len(words) == 0:
                print("** class name missing **")
            elif words[0] in storage.classes():
                if len(words) > 1:
                    key = "{}.{}".format(words[0], words[1])
                    if key in storage.all():
                        if len(words) > 2:
                            if len(words) > 3:
                                if words[0] == "Place":
                                    if words[2] in integers:
                                        try:
                                            words[3] = int(words[3])
                                        except:
                                            words[3] = 0
                                    elif words[2] in floats:
                                        try:
                                            args[3] = float(args[3])
                                        except:
                                            args[3] = 0.0
                                setattr(storage.all()[key], words[2], words[3])
                                storage.all()[key].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
