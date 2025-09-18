vowels = ["a","e","i","o","u"]

myString = input("Type summat: ")
for letter in myString:
  if letter.lower() in vowels:
    print('\033[33m' + letter + '\033[0m', end='') #yellow vowel
  else:
    print(letter, end="") #regular letter

print()  # newline at the end
