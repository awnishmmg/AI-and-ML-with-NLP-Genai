#wap in python to show nested if-else case 1

condition1 = eval(input('Enter the Boolean value:'))
condition2 = eval(input('Enter the Boolean value:'))


if condition1:
    print('Outer if executed')
    if condition2:
        print('inner if executed')
    else:
        print('inner else executed')
else:
    print('Outer Else is executed')
    