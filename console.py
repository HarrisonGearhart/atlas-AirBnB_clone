#!/usr/bin/python3
"""
Our cmd module
"""
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def emptyline(self) -> bool:
        pass

    def do_exit(self, arg):
        """
        Exits the program
        """
        return True
    
    def do_create(self, arg):
        if arg == "":
            print("** class name is missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            temp = BaseModel
            with open("file.json", "w") as file:
                json.dump(temp.to_dict(), file)
            print(f"{id(temp)}")

    do_EOF = do_exit


if __name__ == "__main__":
    HBNBCommand().cmdloop()
