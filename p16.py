#wap in python to show use of random module:-

import random as r 
print(r.random()) #random floating point numbers.
print(r.randint(1,10)) #1 and 10 included

otp = r.randint(1111,9999)
print('Your Otp:',otp)

d1 = r.randint(1,9)
d2 = r.randint(1,9)
d3 = r.randint(1,9)
d4 = r.randint(1,9)
d5 = r.randint(1,9)
d6 = r.randint(1,9)

new_otp = str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)
print('new otp:',new_otp)


otp_2 = f"{d1}{d2}{d3}{d4}{d5}{d6}"
print('Otp 2: ', otp_2)


#decimal random B/w 2 range
print('floating random:',int(r.uniform(5,15)))









