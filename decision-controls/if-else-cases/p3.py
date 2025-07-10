#wap in python to show nested if-else case 3

condition1 = eval(input('Enter the Boolean value condition -1:'))

if condition1:
    print('Outer if executed')
    condition2 = eval(input('Enter the Boolean value condition - 2:'))
    if condition2:
        print('inner if of if executed')
    else:
        print('inner else of if executed')
else:
    print('Outer Else is executed')
    condition3 = eval(input('Enter the Boolean value condition - 3:'))
    if condition3:
        print('inner if of else executed')
    else:
        print('inner else of else executed')
    