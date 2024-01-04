"""
VENDING MACHINE

"""
class VendingMachine:
    def __init__(self):
        self.menu = {
            'A1': {'item': 'Pepsi', 'price': 2.50},
            'A2': {'item': 'Lays', 'price': 5.50},
            'B1': {'item': 'Water', 'price': 1.00},
            'B2': {'item': 'Chocolate', 'price': 1.75},
            'C1': {'item': 'Protein Bar', 'price': 5.00},
            'C2': {'item': 'Gum', 'price': 0.75},
            # Add more items as needed
        }
        self.stock = {
            'A1': 10,
            'A2': 15,
            'B1': 20,
            'B2': 8,
            'C1': 12,
            'C2': 25,
            # Set initial stock for each item
        }

    def display_menu(self):
        print("Welcome to the Vending Machine!")
        print("Menu:")
        for code, item in self.menu.items():
            print(f"{code}: {item['item']} - ${item['price']}")

    def select_item(self):
        while True:
            code = input("Enter the code of the item you want to purchase: ").upper()
            if code in self.menu and self.stock[code] > 0:
                return code
            else:
                print("Invalid code or item out of stock. Please enter a valid code.")

    def process_payment(self, selected_item):
        item_price = self.menu[selected_item]['price']
        while True:
            try:
                money_inserted = float(input("Please insert money ($): "))
                if money_inserted >= item_price:
                    return money_inserted - item_price
                else:
                    print("Insufficient funds. Please insert more money.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def dispense_item(self, selected_item):
        print(f"Dispensing {self.menu[selected_item]['item']}...")
        self.stock[selected_item] -= 1
        print("Thank you!")

    def run(self):
        while True:
            self.display_menu()
            selected_item = self.select_item()
            change = self.process_payment(selected_item)
            self.dispense_item(selected_item)
            print(f"Change: ${change:.2f}")

# Create a VendingMachine instance and run the vending machine
vm = VendingMachine()
vm.run()

