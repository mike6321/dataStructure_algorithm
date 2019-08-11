'''
파이썬 제어문
If 실습
'''
print(type(True)) # 0이 아닌 수, "abc", [1,2,3,....] (1,2,3,...)
print(type(False))

# ex1
if True:
    print('Good')

if False:
    print('Bad')

# ex2
if False:
    print('Bad')
else:
    print('Good!')


case = 'why'
if case:
    print('출력이 되나?')
case = ''
if case:
    print('출력이 되나???? ')


#논리연산자 : and or not

a = 75
b = 40
c = 10

print('and : ',a>b and b<c)
print('or : ',a>b or b<c)
print('not : ',not a>b or b<c)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print('Pass')
else:
    print('Fail')


#다중 조건문
num  = 50

if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')


#ex07
#중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('장학금 80%')
    else: 
        print('장학금 50%')
else:
    print('장학금 없음!')




# in  , not in

q = [10,20,30]
w = [70,80,90,100]
e = {"name": "Lee", "City": "Seoul", "Grade":"A"}
r = (10,12,14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())








