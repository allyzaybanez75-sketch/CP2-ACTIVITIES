class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)
        print(item, "added to cart.")

    def remove_item(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found in cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.cart:
                print("-", item)

    def checkout(self):
        print("Checking out...")
        self.view_cart()
        print("Thank you for shopping!")


cart = ShoppingCart()

while True:
    print("\nShopping Cart Menu")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        cart.add_item(item)

    elif choice == "2":
        item = input("Enter item to remove: ")
        cart.remove_item(item)

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()

    elif choice == "5":
        print("Program ended.")
        break

    else:

        print("Invalid choice.")
