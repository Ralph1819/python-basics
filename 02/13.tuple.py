#생성

t = () #공튜플
t = (1,) # 튜플ㄹ이라는거 표시하기 위해 뒤에 , 표시 // #항목이 하나인 튜플을 생성할 때는 반드시 코마를 사용한다 .

t = (1,2,3)
print(t, type(t))

print("===========sequence 타입 특징 ==============")
print(t[-3],t[-2],t[-1],t[0],t[1],t[2])

# 인덱싱(sequence 타입 특징)
print(t[-3], t[-2],t[-1],t[0],t[1],t[2])

#slicing (sequence 타입 특징)
print(t[1:3])
print(t[:])

#연결 (sequence 타입 특징)
t3 = t +(4,5,6)
print(t3)

#연결 (sequence 타입 특징)
print(len(t3))

#in , not in
print( 4 in t3 )
print( 7 not in t3)

#튜플은 변경 불가
try:
    t4 = ('apple','banana',10,20)
    t4[2] = 90

except TypeError as e:
    print('튜플은 변경 불가 - immutable')

#튜플을 이용한 여러 값의 대입
x, y ,z = 10, 20, 30
print(x,y,z)
x, y =10,20
print(x,y)
x, y = y,x
print(x,y)

print("===========객체함수============")

t5 = (20,30,40,50,20)
print(t5.index(50))
print(t5.count(20))

#변환 : tuple -> set
s = set(t5)
print(t5)

#변환 : tuple -> list

l = list(t5)
l.insert(0,10)
print(l,type(l))
t5 = tuple(l)
print(t5)

tuple(set(t5)) #중복제거하기
print(t5)

