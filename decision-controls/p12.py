#wap in python to show the demo of 
#elif statement 


age=eval(input('Enter the age:'))
price = 100

if age<=5:
    price = 0 
elif age>=6 and age<=10:
    price = price/3
elif age>=11 and age<=18:
    price = price/2 
else:
     price = price/1

print(f' Net Fare :{price}.00 /- INR')
if(price == 0):
    print('Your Ticket is Free')
