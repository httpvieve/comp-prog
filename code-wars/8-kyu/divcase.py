def is_divisible(n,x,y):
        isdiv_x = False
        isdiv_y = False
        res = False
        if n % x == 0 or x == 1:
                isdiv_x = True
        if n % y == 0 or y == 1:
                isdiv_y = True
        if isdiv_x and isdiv_y:
                res = True
        return res
    
    