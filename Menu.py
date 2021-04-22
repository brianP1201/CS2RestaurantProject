class Menu:

    def __init__(self):
        self.menu = {}


    def read_menu(self): #Method converting text file of menu items and prices to a dictionnary as a key-value pair.
        full_menu = {}
        menu = open('Menu.txt').readlines()
        for line in menu:
            name, price = line.split(', ')
            full_menu[name] = price
        self.menu = full_menu.copy()
        
        