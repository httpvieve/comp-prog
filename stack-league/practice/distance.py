import math
u = []
for i in range(4):
  u.append(input())
print(str("{:.2f}".format(math.sqrt((u[2] - u[0])**2 + (u[3] - u[1])**2))))