a =23
a = 20 + 3
print(a, type(a))
print(isinstance(a,int))

# 2진수, 10진수, 8진수, 16진수
b = 0b1101
c = 0o23
d = 0x23
print(b)
print(c)
print(d)

#python 3.x에서는 int, long 합쳐졌따. 따라서 표현 범위가 무한대이다 .
e = 2**1024
print(e, type(e))
print(e.bit_length())

#변환함수
print(bin(38)) #2진수
print(oct(38)) #8진수
print(hex(38)) #16진수

