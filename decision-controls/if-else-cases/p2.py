#wap in python to show nested if-else case 2

condition1 = eval(input('Enter the Boolean value condition -1:'))
condition2 = eval(input('Enter the Boolean value condition - 2:'))


if condition1:
    print('Outer if executed')
else:
    print('Outer Else is executed')
    if condition2:
        print('inner if executed')
    else:
        print('inner else executed')
    