#python Password generator:
import random
letters=['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers =['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '-', '.', '~', '|', '<', '>', '=', '-', '_', '/', ':', ';', '?', '[', ']', '{', '}', '~']
l=int(input("How many Letters would u like in your password \n"))
s=int(input("how many symbols u like to add\n"))
num = int(input("how many numbers would u like to had\n"))
psk = []
for i in range(0,l+1):
    psk +=random.choice(letters)
for j in range (0,s+1):
    psk += random.choice(symbol)
for k in range (0,num+1):
    psk +=random.choice(numbers)
pas="".join(psk)
s_s = "".join(random.sample(pas, len(pas)))
print("Generaated Paassword: ",s_s)
#the end
