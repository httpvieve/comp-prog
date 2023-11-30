N = int(input())
mult_a = []

rel_prime = []

  
for i in range (1, N + 1):
        counter = 0
        mult_b = []
        if N%i == 0:
                mult_a.append(i) 
        for j in range (1, i+1):
                if i%j == 0:
                        mult_b.append(j)
        for num in mult_b:
                if num in mult_a:
                        counter += 1
        if counter == 1:
                rel_prime.append(i)
                
print(len(rel_prime))
print(mult_a)