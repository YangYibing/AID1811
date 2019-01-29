import re 

f = open('day1.txt')
data = f.read()

pattern = r'\b[A-Z]+\w*' #单词
pattern1 = r'\b-?\d+\.?\d*%?\b' #数字

l = re.findall(pattern,data)
l1 = re.findall(pattern1,data)
print(l)
print(l1)


















