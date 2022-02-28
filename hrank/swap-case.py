def swap_case(s):
        swap = ""
        for letter in s:
                if letter.isupper():
                        swap += letter.lower()
                elif letter.islower():
                        swap += letter.upper()
                else:
                        swap += letter
        return swap