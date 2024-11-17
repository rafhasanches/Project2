class Beverage:
    def __init__(self, beverage, price):
        self.beverage = beverage
        self.price = price

    def __str__(self):
        return f"{self.beverage} {self.price}"