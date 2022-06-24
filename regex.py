import re
lol= re.compile(r'(ha){3,}')
mo= lol.search('hahaha')
print(mo.group())