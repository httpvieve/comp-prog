div = input()
#spc_arr = []
spc_arr = ""
for num in range (1111, 10000):
  factor_ctr = 0
  for digit in str(num):
    if not(int(digit) == 0):
      if div % int(digit) == 0:
        factor_ctr +=  1
  if factor_ctr == 4:
    #spc_arr.append(num)
    spc_arr += str(num) + " "
print(spc_arr)
    