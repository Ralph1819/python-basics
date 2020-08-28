# for  반복문
# for in sequnce 객체
for number in [10,20,30,40]:
    result = number**2
    print(result,end=' ',)

else:
    print('')

a = ['cat', 'cow', 'tiger']
for animal in a: # animal 은 for 문을 받아줄 변수
    print(animal,end=' ')
else:
    print('')

#복합 자료형을 for문에서 사용하는 경우
l = [('둘리',10),('마이콜',30),('또치',11)]
for t in l:
    print('이름 : %s, 나이:%d' % t)


# 10번 반복하는 Loop
for i in range(1, 11):
    print(i,end=' ')
else:
    print('')


# 1~10 합을 구하기
s = 0
for n in range(1,11):
    s += n
print(s)

# break 문
for n in range(10):
    print(n, end=' ')
else:
    print('\n-------')

for n in range(10):
    if n > 5:
        break
    print(n, end=' ')
else:
    print('\n---------')




for n in range(10):
    if n <= 5:
        continue
    print(n, end=' ')
else:
    print('\n정상루프 종료')



print('\n---------구구단1-----------')

for i in range(1, 10):
    for j in range(1,10):
        print("%d X %d =%d" % (i,j, i*j)) # (i) 변수에 괄호를 친건지 튜플인지 구별 안되니까 튜플임을 표기할때는 i, <- 쉼표 표기한다
    print("---------------")

print('\n---------구구단1-----------')

for i in range(1, 10):
    for j in range(1, 10):
        print("{0} X {1} = {2}".format(j,i,j*i),end='\t')
    else:
        print('')

print('\n--------삼각형---------')
for i in range(10):
    for j in range(0, i +1):
        print('*',end='')
    else:
        print('')

print('\n--------삼각형-2--------')
for i in range(10):
    print('*'*i)