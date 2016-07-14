# coding=utf-8
# 使python可以讀取中文
import re

def main():
    # 方法二：
#     with open('dic2.txt','a') as f2:
#         with open('dic.txt','r') as f:
#             for line in f.readlines():
#                 if not re.search(';', line, flags=0):
#                     f2.write(line)
    # 方法一：
    with open('dic3.txt','a') as f2:                
        with open('dic.txt','r') as f:
            for line in f.readlines():
                if ';' not in line :
                    strDelete='（|）|\(|\)|"|,|[A-Za-z]'
                    if  re.search(strDelete, line):
                        f2.write(re.sub(strDelete,'',line))
                    elif re.search('，', line):
                        f2.write(re.sub('，','\n',line))
                    else :
                        f2.write(line)
                      
                   
    
    
    

if __name__== "__main__":
    main()
    