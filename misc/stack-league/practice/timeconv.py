time_arr = [int(input()) for x in range(3)]
time = ""
total_t = sum(time_arr)
time_m = int(total_t/60)
if time_m > 0:
  time += str(time_m) + ":"
time_s = total_t%60
if time_s < 10:
  time += "0" + str(time_s)
else:
  time += str(time_s)
print(time)


