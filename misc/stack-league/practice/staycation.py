month = input()
nights = int(input())


period = [["May", "October", 85], ["July", "September", 90.58], ["June", "August", 100.50]]

premium_cost = 0.0
for i in range (3):
  if month in period[i]:

    if nights > 7 and nights < 15:
      if i == 0:
        deluxe_cost = 100.0*nights - (100*nights*0.05)
      elif nights > 14:
        premium_cost = float(period[i][2])*nights - float(period[i][2])*nights*0.1
        if i == 1: 
          deluxe_cost = 112.5*nights - (112.5*nights*0.3)
        if i == 2:
          deluxe_cost = 125.66*nights - (125.66*nights*0.2)
