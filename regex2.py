import re

pattern = r'(ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefghijk',pos=0,endpos=8)

#obj属性变量
print(obj.pos)   #目标字符串的开始位置
print(obj.endpos) #目标字符串的结束位置
print(obj.re) #正则表达式
print(obj.string) #目标字符串
print(obj.lastgroup) #最后一组的名称
print(obj.lastindex) #最后一组是第几组

print('***************************************')

#obj方法
print(obj.span()) #得到匹配内容的起止位置
print(obj.start()) #匹配内容的开始位置
print(obj.end()) #匹配内容的结束位置

print('+++++++++++++++++++++++++++++++++++++++')

#group()功能：获取match对象的对应内容
#参数：默认为0　表示获取正则表达式整体匹配到的内容
    #如果为序列号或者子组名称则表示获取对应子组的匹配内容
#返回值：返回相应的内容
print(obj.group()) #获取匹配到的内容
print(obj.group(1)) #获取第一组内容
print(obj.group(2)) #获取第二组内容
print(obj.group('dog')) #获取dog组内容

print(obj.groupdict()) #获取捕获组字典
print(obj.groups()) #获取所有子组









