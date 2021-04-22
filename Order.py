from Item import Item
class Order:

    def __init__(self, name, items, time, status):
        self.name = name
        self.items = items.copy()
        self.time = time
        self.status = status
    
    def print_receipt(self):
        receipt = ""
        for name in self.items:
            receipt += "{} - {}\n".format(name, self.items[name])
        
        receipt += "Total Price: " + str(self.total_price())
        print(receipt)
    
    def total_price(self):
        price = 0.00
        for i in self.items:
            price = price + float(self.items[i])
        return price
    
    
    def set_status(self, new):
        self.status = new
    
    def __repr__(self):
        return str(self)


class PickUp(Order):

    def __init__(self, name, items, time, contact_info, status="In Progress"):
        self.name = name
        self.items = items.copy()
        self.time = time
        self.contact_info = contact_info
        self.status = status

    def __dictToString(self, dict):
        str1 = ", ".join(list(self.items.keys()))
        return str1

    def __str__(self):
        return self.name + "'s PickUp Order of:\n" + self.__dictToString(self.items) + "\nTime: " + self.time + "\nCustomer Contact: " + self.contact_info + "\nStatus: " + self.status

class DineIn(Order):

    def __init__(self, name, items, time, table, waiter, size, status="In Progress"):
        self.name = name
        self.items = items.copy()
        self.time = time
        self.table = table
        self.waiter = waiter
        self.size = size
        self.status = status

    def __dictToString(self, dict):
        str1 = ", ".join(list(self.items.keys()))
        return str1
    

    
    def __str__(self):
        return self.name + "'s DineIn Order of: " + self.__dictToString(self.items) + "\nTime: " + self.time + "\nTable Number: " + self.table + "\nWaiter: " + self.waiter + "\nSize: " + self.size + "\nStatus: " + self.status

class Delivery(Order):
    def __init__(self, name, items, time, merchant, address, status="In Progress"):
        self.name = name
        self.items = items.copy()
        self.time = time
        self.merchant = merchant
        self.address = address
        self.status = status

    def __dictToString(self, dict): #Convert Items in Order to String format for Easier Printing
        str1 = ", ".join(list(self.items.keys()))
        return str1

    def __str__(self):
        return self.name + "'s Delivery Order of:\n" + self.__dictToString(self.items) + "\nTime: " + self.time + "\nMerchant: " + self.merchant + "\nAddress: " + self.address + "\nStatus: " + self.status


