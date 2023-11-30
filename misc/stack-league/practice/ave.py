init = input()
if init == 0:
  print("No entries")
else:
  counter = + 2
  nVal = input()
  nSum = init + nVal
  while not(nVal == 0):
    nVal = input()
    nSum += nVal
    counter += 1
  print(int(nSum/counter))