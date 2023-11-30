
# def sort (length, array):
#         min = array[0]
#         count = 0
#         for i in range(1, length):
#                 if array[i] < min:
#                         min = array[i]
#                         array[i] = array[0]
#                         array[0] = min
#                         # count = count + 1
#                         for j in range (1, i):
#                                 temp = array[j] # 3
#                                 if temp > array[i] : # 3 > 2
#                                         array[j] = array[i]
#                                         array[i] = temp
#                                         # count = count + 1
                                        
#         return int(count)
                                                                        


max_val = 0
count = 0
n = int(input())
arr = list(map(int, input().split()))
for i in range (len (arr)):
        max_val = max(arr[i], max_val)
        count = count + (max_val - arr[i])
print (count)