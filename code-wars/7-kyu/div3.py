def divisible_by_three(st): 
    digits = []
    sum_st = 0
    for dig in str(st):
        digits.append(dig)
    for num in digits:
        sum_st += int(num)
    while not(sum_st < 3):
        sum_st -= 3
    if sum_st == 0:
        return True
    else :
        return False