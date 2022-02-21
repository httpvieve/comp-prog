def sum_mul(n, m):
        if n > 0 and m > 0:
                result = 0
                for i in range(n, m):
                        if i % n == 0:
                                result += i
                return result
        else:
                return "INVALID"
                        
    