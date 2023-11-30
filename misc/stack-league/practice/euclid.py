case_no = input()
ctr = [0, 0]
for i in range (case_no):
  gender = input()
  if gender == 'm':
    ctr[0] += 1
  elif gender == 'f':
    ctr[1] += 1

print("Males: " + str(ctr[0]) + "\nFemales: " + str(ctr[1]))
temp = min(ctr[0], ctr[1])
if ctr[0] == 0:
  print("All females")
if ctr[1] == 0:
  print("All males")
else:
  temp = min(ctr[0], ctr[1])
  while not(ctr[0] % temp == 0 and ctr[1] % temp == 0 or temp == 1):
    temp -=1
  print(str(int(ctr[0]/temp)) + ":" + str(int(ctr[1]/temp)))

  
  