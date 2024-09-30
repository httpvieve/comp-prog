
key = int(input())
__LHS = key
__RHS = key
while (__LHS % 100 != 99 and __RHS % 100 != 99):
        if __LHS > 1:
                __LHS = __LHS - 1
        __RHS = __RHS + 1

if (__LHS % 100 == 99 and __RHS % 100 == 99):
        print (__RHS)
elif __LHS % 100 == 99:
        print (__LHS)
else:
        print (__RHS)