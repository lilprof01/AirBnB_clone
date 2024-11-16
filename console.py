#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """console program"""
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
