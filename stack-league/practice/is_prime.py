num = int(input())
factor_ctr = 0
for i in range (1, num):
  if num % i == 0:
    factor_ctr += 1
if factor_ctr == 1:
  print("Prime")
else:
  print("Not Prime")
  