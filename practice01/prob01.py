num = input('수를 입력하세요')
print(num)
num.isnumeric()
if not num.isnumeric()  :
    print("정수가 아닙니다")
elif int(num) % 3 == 0:
    print("3의 배수")
else :
       print("3의 배수가 아닙니다")

print(type(num))




