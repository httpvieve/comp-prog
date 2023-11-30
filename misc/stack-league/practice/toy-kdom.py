target_donation = float(input())
prod_quantity = [float(input()) for x in range(5)]
prod_price = [14, 3, 20.2, 8.2, 10.65]
total_price = sum(float(prod_quantity[i] * prod_price[i]) for i in range(5))
if sum(prod_quantity) >= 50:
        total_price = total_price * 0.75

res = total_price*0.9 - target_donation 
if res > 0:
        print("Yes! " + str("{:.2f}".format(res)) + " dollars left.")
else:
        res = -res
        print("Not enough money! "+ str("{:.2f}".format(res)) + " dollars needed.")
        