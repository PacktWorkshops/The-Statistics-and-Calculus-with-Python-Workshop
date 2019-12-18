prices = {'MacBook 13': 1300, 'MacBook 15': 2100, 'ASUS ROG': 1600}  # available products and respective prices

cart = {}  # products added to cart and respective counts

# Shopping - adding items to the cart.
while True:
    _continue = input('Would you like to continue shopping? [y/n]: ')  # talk about the `continue` keyword

    if _continue == 'y':
        print(f'Available products and prices: {prices}')
        new_item = input('Which product would you like to add to your cart? ')

        # Increment the count of the new product in the cart
        if new_item in prices:
            if new_item in cart:
                cart[new_item] += 1
            else:
                cart[new_item] = 1  # if the cart doesn't have the product yet
        else:
            print('Please only choose from the available products.')

    elif _continue == 'n':
        break

    else:
        print('Please only enter "y" or "n".')

# Calculation of total bill.
running_sum = 0
for item in cart:
    running_sum += cart[item] * prices[item]  # quantity times price

print(f'Your final cart is:')
for item in cart:
    print(f'- {cart[item]} {item}(s)')
print(f'Your final bill is: {running_sum}')
