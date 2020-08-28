#enumerate() 함수 사용하기

index = 0
for color in ['red','yellow','blue','black','gray']:
    print(index,color)
    index = index + 1

 # 외부 index 함수 없이 앞에 숫자를 매겨주는 함수가 enumerate
 for index, color in enumerate(['red','yellow','blue','black','gray']):
     print(index,color)