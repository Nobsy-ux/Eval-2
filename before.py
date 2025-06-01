def add_to_cart(cart, item):
    cart.append(item)

def remove_from_cart(cart, item):
    if item in cart:
        cart.remove(item)

def calculate_total(cart, prices):
    total = 0
    for item in cart:
        total += prices.get(item, 0)
    return total

def checkout(cart, prices):
    total = calculate_total(cart, prices)
    print(f"Total is ${total}")
    return total
