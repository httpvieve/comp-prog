def count_sheep(n):
        murmur = ""
        for i in range (1, n + 1):
                murmur += str(i) 
                murmur += " sheep..."
        return murmur
def reverse_seq(n):
        num_arr = [n]
        for i in range (1, n):
                num_arr += [n - i]
        return num_arr
print(reverse_seq(5))


        
        
        