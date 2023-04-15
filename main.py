# Constants for pizza prices
LARGE_PRICE = 6.00
EXTRA_LARGE_PRICE = 10.00
TOPPING_PRICE = {
    1: 1.00,
    2: 1.75,
    3: 2.50,
    4: 3.35
}
HST_RATE = 0.13

# Function to calculate total cost
def calculate_cost(size, toppings):
    if size == "L":
        pizza_price = LARGE_PRICE
    elif size == "XL":
        pizza_price = EXTRA_LARGE_PRICE
    else:
        print("Invalid pizza size. Please choose either 'L' or 'XL'.")
        return None

    topping_price = TOPPING_PRICE.get(toppings, 0)
    subtotal = pizza_price + topping_price
    tax = subtotal * HST_RATE
    total = subtotal + tax

    return subtotal, tax, total

# user input
size = input("Enter pizza size (L for Large, XL for Extra Large): ")
toppings = int(input("Enter number of toppings (1-4): "))

# Calculate cost
result = calculate_cost(size, toppings)

# results
if result is not None:
    subtotal, tax, total = result
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Tax (HST): ${:.2f}".format(tax))
    print("Total: ${:.2f}".format(total))