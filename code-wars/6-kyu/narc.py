def narcissistic( value ):
    sum_dig = 0
    for digit in str(value):
        pow = 1
        for exp in range(1, len(str(value)) + 1):
            pow *= int(digit)
        sum_dig += pow
    return (sum_dig == value)