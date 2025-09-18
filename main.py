vowels = ["a","e","i","o","u"]

myString = input("Type summat: ")
for letter in myString:
  
  if letter.lower() in vowels:
    print('\033[33m', end='') #yellow
    
  print(letter, end="")
  print('\033[0m', end='') #back to default
