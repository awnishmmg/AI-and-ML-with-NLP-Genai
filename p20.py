#wap in python to show random: password 

import string
import random as r
asci_letter = string.ascii_letters
#print(asci_letter)
asci_digit = string.digits
#print(asci_digit)
ascii_symbols = string.punctuation
#print(ascii_symbols)
password = f'{asci_letter}{asci_digit}{ascii_symbols}'
length = int(input('Enter length of password:'))
random_password = r.choices(password,k=length)
pwd = "".join(random_password)
print(pwd)



