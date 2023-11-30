def algo (n):
        print(int(n), end=" ")
        while (n != 1):
                n = n / 2 if n % 2 == 0 else (n * 3) + 1
                print(int(n), end=" ")
algo (int(input()))
        
