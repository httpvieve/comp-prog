age = int(input())
wm_price = float(input())
toy_price = float(input())
cash = 0.0
for yr in range (1, age + 1):
  if yr % 2 == 0: # even age
    cash += yr * 5.0 - 1.0
  else: #odd age
    cash += toy_price
rem = cash - wm_price
if rem >= 0:
  print("Yes! you still have " + str(rem) + " left")
else:
  rem = -rem
  print("No! you still need " + str(rem))
    
    