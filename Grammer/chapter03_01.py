#Chapter03-1
# 숫자형

# 파이썬 지원 자료형
'''
int : 정수
float : 실수
complex : 복소수
boolean : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple :  튜플(시퀀스)
set : 집합
dict : 사전
'''

# 데이터 타입
str1 = "Python"
bool = False
str2 = 'Anaconda'
float_v = 10.0 # 10 == 10.0
int_v = 7
list = [str1, str2]
dic  = {
    "name" : "Machine Learning",
    "version" : 2.0
}

#데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dic))
print(list)

tuple = (7,8,9)
set = {7,8,9}

# 숫자형 연산자 
'''
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x**y - > 2**3
'''

#정수 선언
i = 77
i2 = -14
big_int = 777777777777777777777777777777777777777777777777777777

#정수 출력
print(i)
print(i2)
print(big_int)

#실수 출력
f = 0.999999
f2 = 3.141592
f3 = -3.9
f4 = 3/9
print(f)
print(f2)
print(f3)
print(f4)
print()


# 연산 실습


#형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

#타입출력
print(type(a),type(b),type(c),type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))

