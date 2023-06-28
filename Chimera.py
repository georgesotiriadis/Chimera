#!/usr/bin/python3

from Templates.Banner import print_banner
from Templates.Controller import Controller

def main():
    """Calls the controller"""
    #Print Banner
    print_banner()
    Controller()


# Initiates the tool
if __name__ == '__main__':
    main()


