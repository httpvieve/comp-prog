def next_bigger(number):
  d_ones = number%10
  d_tens = int((number%100 - number%10)/10)
  switched = number - number%100 + d_ones*10 + d_tens
  if d_tens >= d_ones or number < 10:
    return -1
  else: 
    return switched

print(next_bigger(970))