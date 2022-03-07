def gregoryLeibnitz(n):
  sum = 0
  for x in range (1, n + 1):
    if x % 2 == 1:
      sum += float(1/(2*x - 1))
    else:
      sum -= float(1/(2*x - 1))
  return 4 * sum