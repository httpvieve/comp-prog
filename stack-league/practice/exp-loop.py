base_0 = input()
base_n = input()
exp = input()

for num_base in range(base_0, base_n + 1):
  result = num_base
  exp_res = ""
  for num_exp in range (2, exp + 1):
    result *= num_base
    exp_res += str(result)
    if num_exp < exp:
      exp_res += ", "
  print(exp_res)

    
    
