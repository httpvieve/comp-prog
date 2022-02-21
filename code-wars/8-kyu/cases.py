def same_case(a,b):
        char_def = "abcdefghijklmnopqrstuvwxyz"
        char_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if a in char_def and b in char_def or a in char_up and b in char_up:
                return 1
        elif a in char_def and b in char_up or a in char_up and b in char_def:
                return 0
        else: 
                return -1
print(same_case(input(),input()))                
