import re


pattern = r'\w+:(\d+)'
#s = '告别2018,展望2019'
s = '张:1994,李:1995'
#直接使用re调用
# l = re.findall(pattern,s)
# print(l)

#compile对象调用
#regex = re.compile(pattern)
# l = regex.findall(s,pos = 0,endpos=10)
# print(l)

# l= re.split(r'\s+','hello    world nihao Kitty')
# print(l)

s = re.sub(r'\s+','##','hello world nihao Kitty')
print(s)

s = re.subn(r'\s+','##','hello world nihao Kitty')
print(s)

try:
    #obj = re.fullmatch(r'\w+','hello#1973')
    obj = re.fullmatch(r'\w+','hello1973')
    print(obj.group())
except AttributeError as e:
    print(e)

obj = re.match(r'[A-Z]\w+','Hello world')
print(obj.group())

s = '2018年中国经济增长6.6%,与2017年基本持平,2019面对未来'
obj = re.search(r'\d+',s)
print(obj.group())


