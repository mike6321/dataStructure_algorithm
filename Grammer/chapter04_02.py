'''
파이썬 반복문
For 실습

코딩의 핵심
for in <collections>
<Loob body>
'''

for v1 in range(10): # 0~9
    print('v1 is : ',v1)

print()
for v2 in range(1,11): # 1~10
    print('v2 is : ',v2)

print()
for v3 in range(1,11,2):
    print('v3 is : ', v3)

#1~1000까지의 합

sum1 = 0

for v in range(1,1001):
    sum1+=v


print('1~1000 Sum : ',sum1)
print('1~1000 Sum : ',sum(range(1,1001)))

print('1~1000 4의 배수의 합 : ',sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# Iterable 리턴함수 : range, reversed enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park','Choi','Lee','Yoo']

for name in names:
    print(name)


# 예제2
lotto_numbers = [11,19,21,28,36,37]

for n in lotto_numbers:
    print("Current number : ",n)

# 예제3
word = "Beautiful"
for s in word:
    print("word : ",s)

# 예제4
my_info = {
    "name" : "Lee",
    "Age" : 33,
    "City" : "Seoul"
}

for k in my_info:
    print("key : ",k)
print()
for k in my_info:
    print("key : ",my_info[k])
print()
for k in my_info.values():
    print("key : ",k)

# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break
number = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for n in number:
    if n == 34:
        print('Found : 34!')
        break
    else:
        print('Not Fount : 34!')

# continue
lt = ["1",2,5,True,4.3,complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type : ",v,type(v))


# for - else  : for문이 끝까지 찾고 나서 else를 탑니다.
numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break

else:
    print('Not Found : 24')


#구구단 출력(중첩 for 문)
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i*j),end='')
    print()
        

# 변환 예제
name2 = 'Aceman'

print('Reverseed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple',tuple(reversed(name2)))
print('Set',set(reversed(name2)))












