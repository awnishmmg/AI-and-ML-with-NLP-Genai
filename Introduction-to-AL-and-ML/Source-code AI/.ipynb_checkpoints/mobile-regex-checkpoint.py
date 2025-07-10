#wap in python check Indian Mobile No Valid or Not using regex

import re 

mobile = input('Enter the Mobile No:')
matcher = re.finditer('[6-9]{1}[0-9]{9}',mobile)

for match in matcher:
    print(match.start(),'--------',match.end(),'-----',match.group())
    
    



