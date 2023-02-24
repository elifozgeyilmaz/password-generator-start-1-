#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print(len(letters))
print(len(numbers))
print(len(symbols))
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!912



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

chosen_letters = random.sample(letters, k = nr_letters)
chosen_numbers = random.sample(numbers,k = nr_numbers)
chosen_symbols = random.sample(symbols,k = nr_symbols)
password = ""

for letter in chosen_letters:
  password += letter
for number in chosen_numbers:
  password += number

for symbol in chosen_symbols:
  password += symbol
  

chosen_items = nr_letters + nr_numbers + nr_symbols

print(chosen_items)



def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
new_password = Convert(password) 
my_password = random.shuffle(new_password)
print(new_password)
latest_password = ""
for number in range(0,len(new_password)):
  latest_password += new_password[number]

print(latest_password)  



  

  


  

