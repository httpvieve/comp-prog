def nearest_sq(n):
    sq_arr = [];
    temp_1 = n
    temp_2 = n
    for i in range (1, n):
        sq_arr += [i * i]    
    if n < 3:
        return 1;
    elif n in sq_arr:
        return n
    else:
        while not(temp_1 in sq_arr):
            temp_1 += 1
        while not(temp_2 in sq_arr):
            temp_2 -= 1   
        if temp_1 - n <= n - temp_2:
            return temp_1 
        else:
            return temp_2        
print(nearest_sq(int(input())))
