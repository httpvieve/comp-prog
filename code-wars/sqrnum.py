def nearest_sq(n):
    sq_arr = [];
    temp = [n, n]
    for i in range (1, n):
        sq_arr += [i * i]    
    if n < 3:
        return 1;
    elif n in sq_arr:
        return n
    else:
        while not(temp[0] in sq_arr):
                    temp[0] += 1
        while not(temp[1] in sq_arr):
            temp[1] -= 1   
        if temp[0] - n < n - temp[1]:
            return temp[0] 
        else:
            return temp[1]
try:        
        print(nearest_sq(int(input())))
except:
        print("error")