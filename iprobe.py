#!/usr/bin/env python
# -*- coding: utf-8 -*-
# title           :iprobe.py
# description     :This program is a python management layer in CLI for information gathering TOOLSS!!!!!!
# author          :John Clark & Andrew Karls
# date            :
# version         :0.1
# usage           :python3 iprobe.py
# notes           :
# python_version  :3
# =======================================================================

# Import the modules needed to run the script.
import sys, os
from os import system
#  Main definition - constants
menu_actions = {}


# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu
def main_menu():
    os.system('clear')
    os.system('tput setaf 6')
    os.system('cat ~/iprobe/logo')
    print ("\033[1;36;40m \033[1;36;40m Welcome,\n")
    print ("\033[1;36;40m \033[1;36;40m Please choose the menu you want to start:")
    print ("\033[1;36;40m \033[1;36;40m 1. nmap")
    print ("\033[1;36;40m \033[1;36;40m 2. nikto")
    print ("\033[1;36;40m \033[1;36;40m 3. sqlmap")
    print ("\033[1;36;40m \033[1;36;40m 4. wpscan")
    print ("\033[1;36;40m \033[1;36;40m 5. domain footprint")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print ("\033[1;36;40m Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
#def menu1():
#    print "Enter IP to scan!\n"
#    choice = raw_input("")
#    os.system('nmap -Pn {}'.format(choice))
#    return
def nmap():
    IP  = input('Type host IP: ')
    print (' \033[1;36;40m nmap !\n')
    print ('\033[1;36;40m 1. Intense scan w/ port')
    print ('\033[1;36;40m 2. Intense scan')
    print ('\033[1;36;40m 3. Quick scan')
    print ('\033[1;36;40m 4. Ping scan ')
    print ('\033[1;36;40m 5. Back')

    nmap_choice = input("")

    if nmap_choice == '1':
        os.system (' nmap -p 1-65535 -T4 -A -v {}'.format(IP))
    elif nmap_choice == '2':
       os.system ('nmap -T4 -A -v {}'.format(IP))
    elif nmap_choice == '3':
       os.system ('nmap -T4 -F {}'.format(IP))
    elif nmap_choice == '4':
       os.system (' nmap -sn {}'.format(IP))
    else:
        choice = input("9")

    return

# Menu 2
def nikto():
    ip_hostname = input('Enter Host to Nikto scan!\n')
    os.system('nikto -h {}'.format(ip_hostname))
    return

# Menu 3
def sqlmap():
    URL = input('Enter URL you want to scan: ')
    os.system('sqlmap -u {}'.format(URL))
    return

# Menu 4
def wpscan():

    URLwp = input('Type Wordpress URL: ')
    os.system('ruby ~/wpscan/wpscan.rb --url {}'.format(URLwp))

# Menu 5
def domain_footprint():
    dom = input('Type what you want to search for: ')
    os.system ('python ~/tools/theHarvester/theHarvester.py -d {} -l 500 -b all&'.format(dom))
#    menu_actions['main_menu']()

# back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': nmap,
    '2': nikto,
    '3': sqlmap,
    '4': wpscan,
    '5': domain_footprint,
    '9': main_menu
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    #  Launch main menu
    main_menu()
