def sum_str(a, b):
        if len(a) == 0 and not(len(b) == 0):
                sum = b
        elif not(len(a) == 0) and len(b) == 0:
                sum = a
        elif len(a) == 0 and len(b) == 0:
                sum = 0
        else:
                sum = str(int(a) + int(b))
        return sum