# E-commerce Order Processing System
# We resolved some of the errors in class. Resolve the rest of the errors


def process_order(order_id, customer_name, items) -> float:
    total = 0
    for item in items:
        price = get_price(item)
        total += price
    return total


def get_price(product):
    prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75}
    return prices[product]


inventory = {"apple": 10, "banana": 5, "orange": 0}

order_items = ["apple", "banana", "orange", "grape"]
processed_items = []

for item in order_items:
    if (item in inventory) and (inventory[item] > 0):
        inventory[item] -= 1
        processed_items.append(item)
    else:
        print("Item " + item + " is out of stock.")

order_total = process_order(1001, "John Doe", processed_items)
print("Order total is: " + str(order_total))

print("Thank you for your purchase, " + customer + "!")

discount_rate = "0.1"
if discount_rate > 0:
    order_total = order_total * (1 - discount_rate)

print("Final total after discount:", order_total)

fruits = ["apple", "banana", "cherry"]
print(fruits[3])

customer_data = {"John": "Premium", "Jane": "Standard"}
print("Customer type:", customer_data["Jake"])  # KeyError: 'Jake'

count = 0


def increment():
    count += 1
    print("Count is", count)


increment()

user_input = "ten"
quantity = int(user_input)
inventory["banana"] /= quantity


def divide(a, b):
    return a / b


result = divide(10, 0)
print("Result is", result)
