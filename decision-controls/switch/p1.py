#wap in python to show switch statement

n = eval(input('Enter the value of n:'))

def switch(n):
    match n:
        case 1:
            return 'one'
        case 2:
            return 'two'
        case 3:
            return 'three'
        case _:
            return 'No Option'

print(switch(n))
