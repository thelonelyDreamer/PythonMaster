import re

content='''
橘子,
香蕉,
苹果,
'''
p=re.compile('^(.*)(,)',re.IGNORECASE)

for item in p.findall(content):
    print(item[0])
for item in content.split('\n'):
    print(len(item))

m=p.match('12,',0,4)


pattern = re.compile('hello',re.IGNORECASE)
match = pattern.match('Hello\nHello')
print(type(match))
print(match.group(),match.lastindex)