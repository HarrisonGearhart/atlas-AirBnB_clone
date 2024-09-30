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

	def do_create(self, arg):
		"""
		do_create- Creates a new instance of BaseModel, saves it (to the JSON file)
		and prints the id. Ex: $ create BaseModel
		If the class name is missing, print-
		** class name missing ** (ex: $ create)
		If the class name doesn’t exist, print-
		** class doesn't exist ** (ex: $ create MyModel)
		"""

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

	def do_all(self, arg):
		"""
		do_all - Prints all string representation of
		all instances based or not on the class name. Ex: $ all BaseModel or $ all.
		The printed result must be a list of strings (like the example below)
		If the class name doesn’t exist, print
		** class doesn't exist ** (ex: $ all MyModel)
		"""

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
		
if __name__ == "__main__":
    HBNBCommand().cmdloop()
