# OMG SHOELACE METHOD
import math
v_x = []
v_y = []
ctr = 1
d = input()
if not(str(d) == 'stop'):
  v_x.append(str(d))
while str(d) != 'stop':
  ctr += 1
  d = str(input())
  if not(str(d) == 'stop'):
    if ctr % 2 == 0:
      v_y.append(d)
    else:
      v_x.append(d)
perimeter_total = math.sqrt(((int(v_x[len(v_x) -1]) - int(v_x[0]))**2 + (int(v_y[len(v_x) -1]) - int(v_y[0]))**2)) + sum([math.sqrt(((int(v_x[j + 1])) - int(v_x[j]))**2 + (int(v_y[j + 1]) - int(v_y[j]))**2) for j in range(0, len(v_y)-1)])
area = 0.5 * (int(v_x[len(v_x) -1]) * int(v_y[0]) - int(v_y[len(v_x) -1]) * int(v_x[0]) + sum([int(v_x[i])*int(v_y[i + 1]) - int(v_y[i])*int(v_x[i + 1]) for i in range(0, len(v_y)-1)]))
if str(d) == 'stop':
        print("Perimeter: " + str(perimeter_total) +"\nArea: " + str(area))


