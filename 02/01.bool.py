# 부울 참이나 거짓을 나타내는 값
#True , False 두 값(리터럴)만 가진다.

a = 1
print(a > 1)
print(a < 10)

b = a > 1
print(b, type(b))

#연산식에서 integer 값 (False -> 0,Ture -> 1) 값으로 평가된다 .
print(b+1) #True + 1 이 왠말 ?
print(True * False)

if a < 10:
    print(True * False)



#다른 타입의 객체도 bool 타입으로 형반환이 가능하다.
#bool() int() str()
print(bool(10), bool(0)) #0만 F이고 나머지 숫자는 T 나온다 .
print(bool(3.14), bool(0.)) #0만 F이고 나머지 숫자는 T 나온다 .
print('hello', bool('')) #0만 F이고 나머지 숫자는 T 나온다 .
print(bool([0,1]),bool([]))
print(bool((0,1)),bool(()))
print(bool({'k1':'v1','k2':'v2'}), bool({}))
print(bool({'k1':'v1','k2':'v2'}), bool({}))
print(bool(None))

a=None
