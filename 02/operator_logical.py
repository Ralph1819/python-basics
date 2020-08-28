# 일반적으로 피연산자(operand)sms True 또는 False
a = 20

# not T = F
# not F = T
print(not a < 20)

# T and T = T
# T and F = F
# F and T = F
# F and F = F
print(a < 30 and a != 30)


# T or T = T
# T or F = T
# F or T = T
# F or F = F

print( a == 30 or a > 30)

#논리 연산자로 만들어진걸 논리식이라고 하죠 ,
#논리식의 계산순서


print(True or bool('logical'))
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([] and 'logical')
print([2,10] and 'logical')

def f():
    print('hello world')
a=5
#a > 10 and f()
#if a> 10:
#   f()

s= 'Hello World'
s and print(s) #뜻 : s가 빈문자열이 아니라면 출력해라

