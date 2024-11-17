
from vendingMachineObject import VendingMachine


def main():
    machine = VendingMachine()

    while True:
        print("Available Beverages:")
        items = machine.get_items()
        for i in range(len(items)):
            print(f"{i + 1}. {items[i]}")

        try:
            choice = int(input("Select a beverage by number (or enter 0 to exit): "))
            if choice == 0:
                print("Exiting the vending machine. Have a great day!")
                break

            selected_beverage = machine.select_beverage(choice)
            if not selected_beverage:
                print("Invalid selection. Please choose a valid number.")
                continue

            amount_inserted = 0.0
            while amount_inserted < selected_beverage.price:
                try:
                    money = float(input(f"Insert money (${selected_beverage.price - amount_inserted:.2f} remaining): "))
                    amount_inserted += money
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")

            change = machine.process_payment(selected_beverage, amount_inserted)
            if change is not None:
                print(f"Vending {selected_beverage.name}. Enjoy your drink!")
                if change > 0:
                    print(f"Please take your change: ${change:.2f}")
            else:
                print("Insufficient funds. Transaction canceled.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()