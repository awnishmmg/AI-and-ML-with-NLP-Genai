#wap in python to show decorator 
# note : donot consider @decorator as variable because they are only implemented in oops


class Test:
     @property
     def name(self):
        return 'Awnish'
     

test = Test()
print(test.name)
 