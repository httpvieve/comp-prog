def modified_sum(a, n):
            sum_arr = 0 
    for base in a:
        pow = 1
        for exp in range(n):
            pow *= base
        sum_arr += pow
    return sum_arr - sum(int(elem) for elem in a)