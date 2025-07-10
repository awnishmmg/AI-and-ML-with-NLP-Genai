#wap in python to show the demo of the package and sub package


from pqr import users as us
from pqr.xyz import math as m

print(us.getUser('name'))
print(us.getUser('class'))
print(us.getUser('age'))


print(m.add(10,20))
print(m.multi(10,20))

