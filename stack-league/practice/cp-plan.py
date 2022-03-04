call = float(input())
text = float(input())
call_charge = 0
text_charge = 0
fee = 25
cost = float(799.00 + fee)
print("Call minutes: " + str(call) + "\nText messages: " + str(text))
if call > 60 or text > 100:
  if call > 60:
    call_charge = float((call - 60) * 6.50)
  if text > 100:
    text_charge = float(text - 100)
  cost = cost + call_charge + text_charge
print("Excess minute charges: " + str("{:.2f}".format(call_charge)) + "\nExcess SMS charges: " + str("{:.2f}".format(text_charge)))
tax = float(0.05 * cost)
total = float(cost + tax)
print("911 fee: " + str("{:.2f}".format(fee)) +"\nTax: " + str("{:.2f}".format(tax)) + "\nTotal bill: " + str("{:.2f}".format(total)))