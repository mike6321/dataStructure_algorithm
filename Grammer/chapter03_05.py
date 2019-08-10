'''
파이썬 딕셔너리
범용적으로 가장 많이 사용
딕셔너리 자료형 (순서x, 키 중복x, 수정o, 삭제o)
'''

#선언
a = {'name':'Choi', "phone":"01077627318","Birth":"20191029"}
b = {0:"Hello Phython"}
c = {'arr': [1,2,3,4,5]}
d = {
    'Name' : 'NiceMan',
    'City' : 'Seoul',
    'Age' : 29,
    'Grade' : 'S',
    'Status' : True
}

#튜플안에 리스트로 넣는 방법(자주쓰이지는 않는다.)
e = dict([
    ('Name' , 'NiceMan')
])

#편한 방법
f = dict(
    Name = 'NiceMan',
    City = 'Seoul',
    Age = 29,
    Grade = 'S',
    Status = True
)


print('a - ',type(a),a)
print('b - ',type(b),b)
print('c - ',type(c),c)
print('d - ',type(d),d)
print('e - ',type(e),e)
print('f - ',type(f),f)

#출력
print('a - ', a['name'])
print('a - ', a.get('name'))
#둘의 차이
#에러 발생
#print('a - ', a['name1'])
#없을때 None 발생 (훨씬더 안전 대부분 get을 씁니다.)
print('a - ', a.get('name1'))

print('b - ',b.get(0))

print('f - ', f.get('City'))
print('f - ',f.get('Age'))


# 딕셔너리 추가
a['Address'] = 'seoul'
print(a)

a['name'] = '수정합니까?'
print(a)
a['Rank'] = [1,2,3]
print(a)

#키의 갯수를 샙니다.
print('a - ',len(a))
print('b - ',len(b))
print('c - ',len(c))
print('d - ',len(d))

#dict_keys, dict_values, dict_items : 반복분(__iter__)에서 사용가능

print('a - ',a.keys())
print('b - ',b.keys())
print('c - ',c.keys())
print('d - ',d.keys())

#리스트로 형변환
print('c - ',list(c.keys()))
print('d - ',list(d.keys()))
print()


print('a - ',a.values())
print('b - ',b.values())
print('c - ',c.values())

#키값과 value 값을 동시에 튜플형태로 가져오기
print('a - ',a.items())
print('b - ',b.items())
print('c - ',c.items())

print('a - ',a.pop('name'))
print(a)

print('f - ',f.popitem())
print(f)

#birth라는 key가 a에 있습니까? [key값 있는지 진위여부(True/False)]
print('a - ', 'birth' in a)


#수정 & 추가
a['test'] = 'test dictionary';
print(a)
a['phone'] = '01064286921'
print(a)

a.update(birth = '910904')
print('a - ',a)

temp = {'address' : 'Busan'}
a.update(temp)
print('a- ',a)


