phrase = input()
shift = int(input())
new_phrase = ""
total = 26
for letter in phrase:
  key = ord(letter) 
  init = [ord('a'), ord('A')]
  last = [ord('z'), ord('Z')]
  
  if shift > 0:
    
    delim = [last[0] - shift, last[1] - shift]
    
    if (key >= init[0] and key <= delim[0]) or (key >= init[1] and key <= delim[1]):
      new_phrase += chr(key + shift)
    elif (key > delim[0] and key <= last[0]) or (key > delim[1] and key <= last[1]):
      new_phrase += chr(key + shift - total)
    else:
      new_phrase += chr(key)
      
  if shift <= 0:

    delim = [init[0] - shift, init[1] - shift]
    
    if (key <= last[0] and key > delim[0]) or (key <= last[1] and key > delim[1]):
      new_phrase += chr(key + shift)
    elif (key >= init[0] and key < delim[0]) or (key >= init[1] and key < delim[1]):
      new_phrase += chr(key + shift + total)
    else:
      new_phrase += chr(key)

print (new_phrase)
