#wap in python to show the methods of the math module 

import math as m 

#constant 
print(m.pi) #pi value 
print(m.e) #expo e=2.7...
print(m.inf) #infinity 
print(m.nan) #not a number 

#rounding functions 
x=3.765
print(round(x)) #nearest number round of 
print(m.floor(x)) #3
print(m.ceil(x)) #4

#truncating the data :-
print(m.trunc(x)) # 3.765 -> 3
print(int(x)) # decimal part will be truncated.

#trignometry :(angle : degree and radian)
# value will be in radians

# sin,sin^-1 => sin(arc) sin(x) asin(x)
# angle = math.pi/4 => 45 degree

# 2pi = 360 degree
# 2pi/8 = 360/8 degree
# pi/4 = 45 degree 

x = m.pi/4
print(m.sin(x))
print(m.cos(x))
print(round(m.tan(x))) # 0.99 -> round(x) -> 1
print(m.sin(x)/m.cos(x)) #1 => tanx = sinx/cosx


#inverse Trignometry 
print(m.asin(x))
print(m.acos(x))
print(round(m.atan(x))) #by default donot require math module.

#permutation and combination n! and ncr!
print(m.factorial(5)) #120 
print(m.perm(5,3)) #npr : n=5 and r = 3 => n!/(n-r)!
print(m.comb(5,2)) #ncr : n!/r!(n-r)! => 10 



























       
















