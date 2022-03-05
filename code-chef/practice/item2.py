testcase_no = int(input())
tri_side =[]
tri_arr = []
for case in range(testcase_no):
    for side in range(3):
            tri_side.append(input())
    tri_arr[case][side] = [tri_side[i] for i in range (3)]
res_arr = []
for tri in tri_arr:
    sd_sum = 0
    for side in range(3):
        sd_sum += int(tri[side]) 
    if sd_sum == 180:
        res_arr.append("YES")
    else:
        res_arr.append("NO")
for s in tri_arr:
        print(s)
for result in res_arr:
    print(result)

