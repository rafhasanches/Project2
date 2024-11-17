import beverageObject

class VendingMachine:
    def __init__(self):
        self.items = [
            beverageObject.Beverage('1. Coca Cola', '3.00'),
            beverageObject.Beverage('2. Coke Zero', '3.00'),
            beverageObject.Beverage('3. Water', '2.00'),
            beverageObject.Beverage('4. Gatorade', '3.50'),
            beverageObject.Beverage('5. Dr. Pepper', '3.00'),
            beverageObject.Beverage('6. Mountain Dew', '3.00')
        ]

    def get_items(self):
        return self.items

    def select_beverage(self, choice):
        if 1 <= choice <= len(self.items):
            return self.items[choice - 1]
        else:
            return None

    def process_payment(self, beverage, amount_inserted):
        if amount_inserted >= beverage.price:
            return amount_inserted - beverage.price  # Return change if any
        else:
            return None




