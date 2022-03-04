call = int(input())
text = int(input())

fee = 25
cost = float(799.00 + fee)

print("Call minutes: " + str(call) + "\nText messages: " + str(text))
if call > 60 or text > 100: 
  call_charge = float((call - 60) * 6.50)
  text_charge = float(text - 100)
  cost = cost + call_charge + text_charge
  print("Excess minutes charges: " + str("{:.2f}".format(call_charge)) + "\nExcess SMS charges: " + str("{:.2f}".format(text_charge)))
tax = float(0.05 * cost)
total = float(cost + tax)
print("911 fee: " + str("{:.2f}".format(fee)) +"\nTax: " + str("{:.2f}".format(tax)) + "\nTotal bill: " + str("{:.2f}".format(total)))