#global, local 심벌 테이블 확인
g_a = 1
g_s = '마이콜'

def g_f():
    l_a = 2
    l_s = '둘리'
    g_a =2
    print(g_a)
    #g_a = 2
    #print(locals())
print('========Global Symbol Table VS Local Symbol Table========')
print(globals())
g_f()

print(g_a)
# print(l_a)

print("======== Object's Symbol Table ========")

# 1.사용자 정의된 함수
# 심벌테이블 O -> 확장 O
g_f.n = 'hello'
g_f.i = 10
print(g_f.__dict__)

# 2.사용자 클래스
# 심벌테이블 O -> 확장 O
class MyClass:
    def __init__(self):
        self.i = 10
        self.j = 20
    x = 10
    y = 10

MyClass.z = 10
print(MyClass.__dict__)

# 3. 내장함수
#내장함수는 심볼테이블 없음 -> 확장 불가능
#내가 정의한 함수는 확장이 가능하지만 내장함수는 불가능하다
# print.z =10
# print(print.__dict__)

# 4. 내장 클래스
print(str.__dict__) #내장클래스는 심볼테이블 O -> 확장 가능?? -> 확장은 불가능하다 (확장 못하도록 금지되어있음)


# 5. 내장 클래스로 생성된 객체
# 심벌테이블 x -> 확장 x
g_a.z = 10
#print(g_a.__dict__)


#클래스는 왜 만들어요 ? ?객체 만들라고

# 6. 사용자 정의 클래스로 생성된 객체
# 심벌테이블 O -> 확장 O
o = MyClass()
print(o.__dict__)