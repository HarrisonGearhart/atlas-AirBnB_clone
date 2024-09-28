#!/usr/bin/python3
"""
Our cmd module
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
