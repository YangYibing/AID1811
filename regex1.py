import re

pattern = r'\d+'
s = '2018年中国经济增长6.6%,与2017年基本持平,2019面对未来'

it = re.finditer(pattern,s)
#match对象属性
print(dir(next(it)))
for i in it:
    print(i.group())




