def disemvowel(string_):
        vowels = ""
        for letter in string_:
                if not letter in "aeiouAEIOU":
                        vowels += letter
        return vowels

print(disemvowel("Huang Renjun"))