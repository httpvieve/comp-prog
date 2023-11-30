def capitalize (str):
  sym = ['.', '!', '?']
  newstr = ""
  for i in range (0, len(str)):
    if str[i - 2] in sym and str[i].isupper() == False and i - 2 >= 0 and str[i - 1] == ' ':
      newstr += str[i].upper()

    elif i == 0 and str[i].isupper() == False:
      newstr += str[i].upper()
    elif str[i] == 'i' and str[i - 1] == ' ' and (str[i + 1] == ' ' or str[i+1] in sym) :
      newstr += 'I'
    elif i < len(str) and str[i].isupper() == False and str[i - 1] in sym:
      newstr += " " + str[i].upper()
    else:
      newstr += str[i]
  return newstr


p ="i.heaeh.i it is i. dasd"
print(capitalize(p))
