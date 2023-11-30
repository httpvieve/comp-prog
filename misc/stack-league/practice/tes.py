# number = input()
arr_digits = []
max_num = ""
#for digit in str(number):
  arr_digits.append(int(digit))

# sorted_arr = [i for n, i in enumerate(arr_digits) if i not in arr_digits[:n]] #removes dupliicates
# sorted_arr.sort() # arrange ascending
# sorted_arr.reverse() 
arr_digits.sort()
arr_digits.reverse()
for dig in arr_digits:
  max_num += str(dig)
# print(max_num)

