import math
v_0 = float(input())
deg = float(input())
t_s = float(input())
g = 9.81
n = 180/deg
x = round(v_0*t_s*math.cos(math.pi/n))
y = round(v_0*math.sin(math.pi/n)*t_s - (t_s*t_s*g*0.5))

print(str(x) + ", "+ str(y))