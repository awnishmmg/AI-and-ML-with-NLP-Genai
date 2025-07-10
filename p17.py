#wap in python show selection of choice using random

import random as r

wifes = ["katreena","kareena","aishwarya","sunny","madhuri","urfi javed"]

drinks = ["RedLabel","8PM","Bagpiper","brocode","kingfisher","oldmonk","blackdog"]

print('My wife selection:',r.choice(wifes))
print('My fav drink:',r.choice(drinks))

# if pickup some random value out of give list.

index = r.randint(0,len(drinks)-1)
print(drinks[index])

# sample selection : within the range
sample = r.sample(drinks,2)
print('Top drinks:',sample)

# sample selection : outside the range
#sample = r.sample(drinks,10) #0 to n-1
#print('Top drinks:',sample)

print('My wife selection:',r.choices(wifes,k=4))
#chance of repeatition
print('My wife selection:',r.choices(wifes,k=10))
#shuffle



















