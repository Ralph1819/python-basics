#1~10 합을 구하기
s,count =0,1
#for n in range(1,11):
#   s +=n
#print(s)

s, count = 0,1
while count < 11:
    s +=count
    count += 1
print(s)

s= 0
count = 0
while count < 10 :
    s += (count +1)
    count += 1

print(s)

#break
i=0
while i <10:
    if i >5:
        break
    print(i,end=' ')
    i += 1

print("\n-----------------------------")


# #continue
# for n in range(10):
#     if n<=5:
#         continue
#         print(n,end=' ')


###왜 무한루프에 빠지는거야 ??
i = 0
while i < 10:
    if i <=5:
        i += 1
        continue
    print(i,end=' ')
    i += 1

print('\n-------------------------')

# 무한루프

while True :
