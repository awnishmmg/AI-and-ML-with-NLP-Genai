#wap for writing a function roll_dice/toss_coin

import random as r 
def roll_dice():
    return r.randint(1,6)


def toss_coin():
    coin = ['Head','Tail']
    return r.choice(coin)
    
choice = int(input('Enter the option:press 0|1 : '))

arr = [roll_dice(),toss_coin()]
print('The result :',arr[choice])

    
    