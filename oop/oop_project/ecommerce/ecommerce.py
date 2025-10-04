class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def buy(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return f'You bought {quantity} {self.name}(s). Remaining stock: {self.stock}'
        else:
            return f'Sorry, your requested quantity ({quantity}) for {self.name} is not available. Only {self.stock} left.'


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []   # cart list

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))  # টিউপল আকারে যোগ করলাম (প্রোডাক্ট, কুয়ান্টিটি)
            print(f"{self.name} added {quantity} {product.name}(s) to cart.")
        else:
            print(f"Not enough stock for {product.name}! Available: {product.stock}")

    def checkout(self):
        total = 0
        for product, quantity in self.cart:
            if product.stock >= quantity:
                product.stock -= quantity
                total += product.price * quantity
            else:
                print(f"⚠️ Sorry, not enough stock for {product.name}. Skipping this item.")
        self.cart = []   # কার্ট খালি করে দিলাম
        return f"{self.name}, your total bill is: ${total}"


# -----------------------------
# 🚀 এখন সিস্টেম টেস্ট করি
product1 = Product("iPhone", 2900, 10)
product2 = Product("Headphone", 150, 5)

customer1 = Customer("Rahim")

# Add products to cart
customer1.add_to_cart(product1, 2)
customer1.add_to_cart(product2, 3)

# Checkout
print(customer1.checkout())

# দেখানো যাক স্টক কমলো কি না
print(f"iPhone stock left: {product1.stock}")
print(f"Headphone stock left: {product2.stock}")