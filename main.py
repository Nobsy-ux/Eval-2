from module_1 import add_to_cart, remove_from_cart
from module_2 import checkout

def main():
    cart = []
    prices = {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 0.75
    }

    add_to_cart(cart, "apple")
    add_to_cart(cart, "banana")
    remove_from_cart(cart, "orange")  # not in cart, nothing happens
    add_to_cart(cart, "orange")

    checkout(cart, prices)

if __name__ == "__main__":
    main()
