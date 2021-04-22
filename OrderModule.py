import queue
from Menu import Menu
from datetime import datetime
from Item import Item
from Order import Order, Delivery, DineIn, PickUp

orders = []
start = 0
complete = 0
full_menu = Menu()
full_menu.read_menu() 


if __name__ == "__main__":
    try:
        while True:
            while start == 0: #Designate User role at start of program
                role = input("Hi! Welcome to the Order Management System! Are you a Waiter (W) or Receptionist  (R) ? Press Ctrl-C to exit. ")
                start += 1
    
            if role.casefold() == "r": #Receptionists will handle PickUp and Delivery Orders
                if not orders: #Empty queue = no orders, default action will be to add an order.
                    action = input("What type of order do you want to add? Delivery, or PickUp? ") #
                    if action.casefold() == "delivery": #Start adding a Delivery order
                        name = input("What is the customer's name? ")
                        items = input("What items are being ordered? Enter items separated by commas. (Ex: Grilled Chicken, Steak ) ")
                        items_list = list(items.split(", "))
                        for x in items_list:
                            items_dict = dict.fromkeys(items_list, full_menu.menu.get(x)) #Create dictonary of items ordered
                        now = datetime.now()
                        time = now.strftime("%I:%M:%S %p")
                        merchant = input("Who will be delivering the order? Ex: Uber Eats, DoorDash, In-House, etc. ")
                        address = input("What address will this order be delivered to? ")
                        new_order = Delivery(name, items_dict, time, merchant, address)
                        orders.append(new_order) #Add new order to the queue
                        print("New Delivery Order Placed!")
                    elif role.casefold == "pickup":
                        name = input("What is the customer's name? ") #Start adding a Pickup order
                        items = input("What items are being ordered? ")
                        items_list = list(items.split(", "))
                        for x in items_list:
                            items_dict = dict.fromkeys(items_list, full_menu.menu.get(x)) #Create dictonary of items ordered
                        now = datetime.now()
                        time = now.strftime("%I:%M:%S %p")
                        contact_info = input("What is the customer's phone number? ")
                        new_order = PickUp(name, items_dict, time, contact_info)
                        orders.append(new_order) #Add new order to the queue
                        print("New PickUp Order Placed!")

                else: #Orders are in the queue so more options are enabled
                    print([order for order in orders])
                    action = input("Would you like to add, delete, edit, or update an order? ")
                    if action.casefold() == "add": 
                        action = input("What type of order do you want to add? Delivery or PickUp? ")
                        if action.casefold() == "delivery":
                            name = input("What is the customer's name? ")
                            items = input("What items are being ordered? ")
                            items_list = list(items.split(", ")) #Separate different items with comma
                            for x in items_list:
                                items_dict = dict.fromkeys(items_list, full_menu.menu.get(x))
                            now = datetime.now()
                            time = now.strftime("%I:%M:%S %p")
                            merchant = input("Who will be delivering the order? Ex: Uber Eats, DoorDash, In-House, etc. ")
                            address = input("What address will this order be delivered to? ")
                            new_order = Delivery(name, items_dict, time, merchant, address)
                            orders.append(new_order) #Add new order to the existing queue
                            print("New Delivery Order Placed! ")
                        elif role.casefold == "pickup": #Adding a pickup order
                            name = input("Adding new PickUp Order. What is the customer's name? ")
                            items = input("What items are being ordered? ")
                            items_list = list(items.split(", "))
                            for x in items_list:
                                items_dict = dict.fromkeys(items_list, full_menu.menu.get(x))
                            now = datetime.now()
                            time = now.strftime("%I:%M:%S %p")
                            contact_info = input("What is the customer's phone number? ")
                            new_order = PickUp(name, items_dict, time, contact_info)
                            orders.append(new_order)
                            print("New PickUp Order Placed!")

                    elif action.casefold() == "delete": #Delete an order from the queue
                        find = input("Enter the customer's name of the order you would like to delete? ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                print(order.name + "'s order has been removed from the queue.")
                                orders.remove(order)

                    elif action.casefold() == "edit": #editing an order
                        find = input("Enter the customer's name of the order you would like to edit: ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                action = input("Do you want to add or remove items to the order? ")
                                if action.casefold() == "add":
                                    new_items = input("What items do you want to add to the order? ")
                                    new_items = list(new_items.split(", "))
                                    for x in new_items:
                                        items_dict.update({x:full_menu.menu.get(x)})
                                    order.items = items_dict.copy()
                                    print("Order Updated!")
                                elif action.casefold() == "remove":
                                    del_items = input("What items do you want to remove from the order? ")
                                    del_items = list(del_items.split(", "))
                                    for x in del_items:
                                        for item in order.items:
                                            if x == item:
                                                del order.items[item]
                                    print("Order Updated!")

                    elif action.casefold() == "update": #Update the status of an order
                        find = input("Enter the customer's name of the order you would like to edit: ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                update_action = input("Current status is " + order.status + ". Enter the new status of the order: ")   
                                order.set_status(update_action)
                                print("Order status updated to: " + order.status)
                            if order.status.casefold() == "completed":
                                choice = input("Do you want to print a reciept for this order? (Yes or No)") #Print a list of items ordered and total price
                                if choice.casefold() == "yes":
                                    order.print_receipt()


    

            elif role.casefold() == "w": #If user is not a receptionist, then they are a Waiter. Waiters will handle Dine-In Orders
                if not orders: #Empty queue = no orders, default action will be to add an order.
                    name = input("Adding new DineIn Order. What is the customer's name? ")
                    items = input("What items are being ordered? ")
                    items_list = list(items.split(", "))
                    for x in items_list:
                        items_dict = dict.fromkeys(items_list, full_menu.menu.get(x))
                    now = datetime.now()
                    time = now.strftime("%I:%M:%S %p")
                    table = input("What table number does this order belong to? ")
                    waiter = input("What is the name of the waiter handling this order? ")
                    size = input("How many customers are seated at the table? ")
                    new_order = DineIn(name, items_dict, time, table, waiter, size)
                    orders.append(new_order)
                    print("New DineIn order placed!")

                else: #Orders are in the queue so more options are enabled
                    print([order for order in orders])
                    action = input("Would you like to add, delete, edit, or update an order? ")
                    if action.casefold() == "add":
                        name = input("Adding new DineIn Order. What is the customer's name? ")
                        items = input("What items are being ordered? ")
                        items_list = list(items.split(", "))
                        for x in items_list:
                            items_dict = dict.fromkeys(items_list, full_menu.menu.get(x))
                        now = datetime.now()
                        time = now.strftime("%I:%M:%S %p")
                        table = input("What table number does this order belong to? ")
                        waiter = input("What is the name of the waiter handling this order? ")
                        size = input("How many customers are seated at the table? ")
                        new_order = DineIn(name, items_dict, time, table, waiter, size)
                        orders.append(new_order)
                        print("New DineIn order placed!")

                    elif action.casefold() == "delete": #Remove an order from the queue
                        find = input("Enter the customer's name of the order you would like to delete: ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                print(order.name + "'s order has been removed from the queue.")
                                orders.remove(order)

                    elif action.casefold() == "edit": #Add or remove items from an order 
                        find = input("Enter the customer's name of the order you would like to edit: ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                action = input("Do you want to add or remove items to the order? ")
                                if action.casefold() == "add": #Add items to the order
                                    new_items = input("What items do you want to add to the order? ")
                                    new_items = list(new_items.split(", "))
                                    for x in new_items:
                                        items_dict.update({x:full_menu.menu.get(x)}) #Update current order items list with new order requested
                                    order.items = items_dict.copy()
                                    print("Order Updated!")
                                elif action.casefold() == "remove":
                                    del_items = input("What items do you want to remove from the order? ")
                                    del_items = list(del_items.split(", ")) #Remove requested items from the order
                                    for x in del_items:
                                        for item in list(order.items):
                                            if x == item:
                                                del order.items[item]
                                    print("Order Updated!")
                        
                    elif action.casefold() == "update": #Update the status of an order
                        find = input("Enter the customer's name of the order you would like to edit: ")
                        for order in orders:
                            if find.casefold() == order.name.casefold():
                                update_action = input("Current status is " + order.status + ". Enter the new status of the order: ")   
                                order.set_status(update_action)
                                print("Order Status updated to: " + order.status)
                            if order.status.casefold() == "completed":
                                choice = input("Do you want to print a reciept for this order? (Yes or No)")
                                if choice.casefold() == "yes": #Print a list of items ordered and total price
                                    order.print_receipt()


    except KeyboardInterrupt:
        print("Program terminated.")
        pass


