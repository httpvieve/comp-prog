import math
a = input()
b = input()
c = input()

d_x = b*b - 4*a*c

if d_x > 0:
  r_1 = float((-b + math.sqrt(d_x))/(2*a))
  r_2 = float((-b - math.sqrt(d_x))/(2*a))
  print("There are two solutions , namely " + str(r_1) + " and " + str(r_2))
else:
  print("There are no solutions")