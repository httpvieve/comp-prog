import math
def kenro(lst):
  key = []
  
  for i in range (len(lst)):
    r_2 = lst[i][2]
    r_1 = lst[i][1]
    n = lst[i][0]
    
    if r_1 < r_2:
      key.append("No")
    else: 
      if r_1 > 0 and r_2 > 0:
        
        ratio = r_2/(r_1 - r_2)
        d_a = (abs(math.asin(ratio)*180)/3.14)
        if r_1 < 2*r_2:
          max_circles = 1
        else:
          max_circles =(360/(2*math.floor(d_a)))
        
        if n <= max_circles:
          key.append("Yes")
      else:
        key.append("Invalid")
  return key
      