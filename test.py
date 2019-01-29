import re
import sys

def get_address(port):
    #提取一段内容
    f = open('test')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        # print(data)
        #已经到文件结尾
        if not data:
            return 'Not Found'
        
        #匹配首单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception:
            print('打开失败')
            continue
        if PORT == port:
            #pattern = r'address is ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})'
            pattern = r'address is ((\d{3}\.){3}\d{1,3}/\d+|Unknow)'
            address = re.search(pattern,data).group(1)
            return address
   


if __name__ == '__main__':
    port = sys.argv[1]
    addr = get_address(port)
    print(addr)









