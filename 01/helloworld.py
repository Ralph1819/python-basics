#helloworld.py

print('hello world')

a = 2
if a < 1:
    print(a)
    print('big')

b=20
def my_func(i):
    if i > 10:
        print('big')
        print('...')

    print('my_func end')



def my_func(i):
    print('블록 시작(함수정의)')
    if i > 10:
        print('블록 시작(조건문)')
    print()
    print()
    print()


#블록 시작(전역범위)
print('hello World')
a=2
if a > 1:   #블록 시작(조건문)
    b = 1
    print(a)
    print('big')
    #블록 끝(조건문)

