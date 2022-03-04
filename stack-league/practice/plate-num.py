import string
plate_num = input()
validchar = string.ascii_uppercase
validstr = list(validchar)
is_valid = False
if len(plate_num) == 6: 
  for i in range(3):
    if plate_num[i] in validstr and int(plate_num[i + 3]) >= 0:
      is_valid = True
  if is_valid:
    print("The plate is a valid older style plate.")
elif len(plate_num) == 7:
  for a in range(4):
    for b in range (3):
      if int(plate_num[a]) >= 0 and plate_num[b + 4] in validstr:
        is_valid = True
  if is_valid:    
    print("The plate is a valid newer style plate.")
if not(is_valid):
  print("The plate is not valid.")
