class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"