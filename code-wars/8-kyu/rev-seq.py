def reverse_seq(n):
        num_arr = [n]
        for i in range (1, n):
                num_arr += [n - i]
        return num_arr