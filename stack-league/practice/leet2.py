
def addTwoNumbers(arr_1, arr_2):
        arr_1.reverse()
        arr_2.reverse()
        sum_arr = []
        strn1 = ""
        strn2 = ""
        for a in arr_1:
            strn1 += str(a)
        for b in arr_2:
            strn2 += str(b)
        nsum = str(int(strn1) + int(strn2))
        for digit in nsum:
            sum_arr.append(int(digit))
        return sum_arr

a = [2,4,3]
b = [5,6,4]

c = [9,9,9,9,9,9,9]
d = [9,9,9,9]

print(addTwoNumbers(a,b))
print(addTwoNumbers(d, c))
    
    