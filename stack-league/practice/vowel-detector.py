str_phrase = input("input phrase/word..")
vowels = ["a", "e", "i","o", "u"]
vowel_counter = [0,0,0,0,0]
total = 0
for letter in str_phrase:
  if letter in vowels:
    vowel_counter[vowels.index(letter)] += 1

for counter in vowel_counter:
        if counter >= 1:
                total += 1
if total == 1:
        print("There is only one different vowel in the string.")
else:
        print("There are " + str(total) + " different vowels in the string.")
    
  