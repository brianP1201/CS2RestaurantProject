class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, new):
        self.price = new

    def set_name(self, new):
        self.name = new

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


   