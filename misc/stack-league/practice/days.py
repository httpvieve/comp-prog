month = input()
if month == 2:
  days = "28 or 29 days"
else:
  if month < 8:
    mod = month % 2
  else:
    mod = (month + 1) % 2
    
  if mod == 1:
    days = "31 days"
  else :
    days = "30 days"
print(days)