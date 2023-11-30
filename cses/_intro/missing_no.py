def return_missing (n, arr):
        total = 0;
        for i in range(len(arr)):
                total = total + arr[i]
        return int(((n * (n + 1))/2) - total)

n = int(input())
arr = list(map(int, input().split()))

print (return_missing(n, arr))