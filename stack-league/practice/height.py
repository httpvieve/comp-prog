player_name = input()
height = int(input())
feet =int(height/12)
inches = float(height - feet*12)
print("Standing at " + str(float(feet)) + "\'" + str(inches) +"\'\'" + " tall, " + player_name)