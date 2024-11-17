#!/usr/bin/python3
""" Defines the console class
"""


import cmd
#from models import storage
#from models.engine.errors import *
#import shlex
#from models.base_model import BaseModel
#from models.user import User
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.place import Place
#from models.review import Review

#classes = storage.models


class HBNBCommand(cmd.Cmd):
    """ does various HBNB commands """
    prompt = "(hbnb) "

    # Commands
    def do_EOF(self, args):
        """Exits the programme in non-interactive mode"""
        return True

    def do_quit(self, args):
        """Quits commands that closes the programme"""
        return True

    def emptyline(self):
        """Overides empty line to do nothing """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
