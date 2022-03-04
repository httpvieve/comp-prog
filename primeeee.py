import math
def long_gray(n):
  while n % 2 == 0:
    max_prime = 2
    n /= 2
  for factor in range(3, int(math.sqrt(n)) + 1, 2):
    while n % factor == 0:
      max_prime = factor
      n = n / factor
  if n > 2:
    max_prime = n
  return int(max_prime)
print(long_gray(1000219))