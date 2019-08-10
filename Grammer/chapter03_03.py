# 파이썬 리스트
# 자료구조에서 중요!
# 리스트 자료형(순서 o, 중복 o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70,75,80,85] # len
d = [1000,10000,'Ace','Base','Captine'] # 서로다른 자료형을 한 리스트에 담을 수 있다.
e = [1000, 10000, d]
f = [21.42, 'foobar', 3, 4, False, 3.141592]
print(len(c))
print(e)

#인덱싱
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('d - ',type(d),d)
print('d - ',d[1])
print('d - ',d[0]+d[1]+d[1])
print('d - ',d[-1])
print('e - ',e[-1][-1])
print('e - ',type(e[-1][-1]))
print('e - ',list(e[-1][-1])) #해당 문자 리스트로 형 변 환
print('e - ',e[-1][0:])

#리스트 연산
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print('c+d - ',c+d) #리스트 더하기 리스트 = 리스트
print('c*3 - ',c*3)
print('Test'+str(c[0]))

#값 비교
print(c == c[:3]+c[3:])
print(c[:3])
print(c[3:])

#Identity
temp = c
print(temp , c)
#같은 집 주소를 보고있음
print(id((temp)))
print(id((c)))

#리스트 수정, 삭제
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
'''c = [70,75,80,85]'''
#c[0] = 4
c[1:2]  = ['a','b','c']
c[1:2]  = [['a','b','c']] # 이렇게 하면 리스트안에 리스트가 들어간다.
print(c)
c[1] = ['c','h','o','i'] #슬라이싱을 쓰지 않고 인덱스를 지정하면 리스트가 들어간다.
print(c)

#제거
c[1:3] = []
print(c)

del c[2]
print('del - c : ', c )

#리스트 함수
a = [5,2,3,1,4]
print('a : ',a)

#뒤에다 붙이고 싶을때
'''
이렇게는 안된다.
a[5] = 10
print(a)
'''
a.append(10)
print('a : ',a)
a.sort() #오름차순 정렬
print('a : ',a)
a.reverse() #내림차순 정렬
print('a : ',a)
print('a : ',a.index(3)) # 인덱스 가져오기

a.insert(2,7)# 두번째 위치에 7을 넣기
print('a : ',a)

#del의 활용, remove()
del a[a.index(2)]
print('a : ',a)

a.remove(4)
print('a : ',a)

#마지막 원소 갖고오기
pop = a.pop()
print(pop)
print('a : ',a)

#내가 찾는값이 몇개가 중복되어 있는지 확인
print(a.count(4))

ex = [8,9]
a.extend(ex)
print(a)