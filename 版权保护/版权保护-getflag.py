#coding=utf8
import binascii

f = open('题目.txt','r',encoding='utf8')
lines = f.readline()
f.close()

#转换为二进制0和1
i = 0
content = ''
for x in lines:
    if x == '\u200d':
        content += '0'
    elif x == '\u200c':
        content += '1'
    #i=i+1
print("输出二进制:")
print(content)

#--------------------------------------------------------------------------------------

#base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f]
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]
#print(base)

#二进制 to 十进制: int(str,n=10) 
def bin2dec(string_num):
    return str(int(string_num, 2))

#十进制 to 十六进制: hex() 
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    if num == 0:
        return '0'
    while True:
        if num == 0: break
        num,rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])

#二进制 to 十六进制: hex(int(str,2)) 
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))

#--------------------------------------------------------------------------------------

#转换为十六进制
k = 0
result = ''
num = ''
while k < len(content):
    if k!=0 and (k+1) % 4 == 0:
        num += content[k]
        result += bin2hex(num)  #二进制转十六进制
        #print(num)
        #print(bin2hex(num),'\n')
        num = ''
    else:
        num += content[k]
    k += 1 
print("\n输出十六进制:")
print(result)


#提取flag
result = result + '0'
flag = binascii.unhexlify(result)
print("\n输出flag:")
print(flag)

