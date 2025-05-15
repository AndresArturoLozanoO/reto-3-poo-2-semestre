class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total = 0
    def total_price(self):
        self.total += self.price
        return self.total
    
class Beverage(MenuItem):
    def __init__(self, name, price, volume_ml):
        super().__init__(name, price)
        self.volume = volume_ml/100
        self.price = price*self.volume*0.5
    
class Appetizer(MenuItem):
    def __init__(self, name, price, adicional_pieces):
        super().__init__(name, price)
        self.ad_price = adicional_pieces*2
        self.price = price+self.ad_price

class MainCourse(MenuItem):
    def __init__(self, name, price, meatsize):
        super().__init__(name, price)
        self.price = price*meatsize*1/5

class Soup(MenuItem):
    def __init__(self, name, price, volume_ml):
        super().__init__(name, price)
        self.volume = volume_ml/100
        self.price = price*self.volume

class Bill:
    def __init__(self, tip):
        self.tip = tip
        self.item_1 = Appetizer("prawns", 12, 5)
        self.item_2 = Soup("ajiaco", 14, 250)
        self.item_3 = Soup("tripe", 10, 250)
        self.item_4 = Soup("fish stew", 8, 300)
        self.item_5 = MainCourse("pork", 8, 15)
        self.item_6 = MainCourse("veal", 15, 15)
        self.item_7 = MainCourse("Vegetarian", 18, 0)
        self.item_8 = Beverage("soda", 3, 100)
        self.item_9 = Beverage("wine", 12, 500)
        self.item_10 = Beverage("water", 3, 100)
        self.list = [self.item_1, self.item_2, 
                     self.item_3, self.item_4, 
                     self.item_5, self.item_6, 
                     self.item_7, self.item_8, 
                     self.item_9, self.item_10]
    def total(self):
        total = 0
        for i in self.list:
            total += i.total_price()
        return total + self.tip
    

bill = Bill(20)
print(bill.total())
