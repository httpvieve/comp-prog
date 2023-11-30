import string
word = input()
nShift = input()
shiftedstr = ""
chr_up = []
chr_lw = list(map(chr, range(97, 123)))
for letter in chr_lw:
  chr_up += letter.upper()
for i in range (len(word)):
  if word[i] in chr_up:
    shiftedchr = chr_up[(chr_up.index(word[i]) + nShift)%len(chr_up)]
    #shiftedchr = ord(word[i]) + nShift
  elif word[i] in chr_lw:
    shiftedchr = chr_lw[(chr_lw.index(word[i]) + nShift)%len(chr_lw)]
  else:
    shiftedchr = word[i]
  shiftedstr += shiftedchr

print(shiftedstr)


