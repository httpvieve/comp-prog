egg_quantity = input()
if egg_quantity >= 12:
  dzn = int(egg_quantity/12)
  print(dzn*70 + (egg_quantity-dzn*12)*7)
else:
  print(egg_quantity*7)
  
  
  