k = int(input())
a = k/2
b = (k + 1)/2

print(int(a * b))
for i in range(1,int(a + 1)):
        for j in range(int(a + 1), k + 1):
                print("{} {}".format(i, j))