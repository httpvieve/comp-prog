nBooks = input("Book quantity: ")

book_price = 24.95
discount = 0.4
ship_init = 3.00
ship_addtl = 0.75

total_cost = nBooks * (book_price * (1 - discount)) + ship_init + ship_addtl * (nBooks - 1)

print(str(total_cost))