#Task 1: Customer Order Processing
#using the list of orders given, unpack each tuple and print the order details
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Joe", "Smartphone", 1)
]

#Write a function to iterate over the list of orders
#Unpack each tuple in the list and format the details for display
def Display_Order():
    for i in range(len(orders)):
        name, item, quantity = orders[i]
        print(f"{name} purchased {quantity} {item}(s)")

Display_Order()