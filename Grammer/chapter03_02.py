# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1),type(str2),type(str3),type(str4))
#문자열 길이 출력
print(len(str1))

# 빈 문자열
str1_t1 = ''
str_t2 = str()

print(type(str1_t1), len(str1_t1))

#이스케이프 문자 사용
# I'm Boy
print("I'm Boy")
# 에러 발생print('I'm Boy')
print('I\'m Boy')

print('a \t b')
print('a\nb')

escapte_str1 = 'Do you have a \"retro Games?\"'
print(escapte_str1)
escapte_str2 = 'What\'s on TV'
print(escapte_str2)

# 탭 , 줄 바꿈
t_s1 = 'Click \t Start!'
t_s2 = 'New Line\nCheck!'

print(t_s1)
print(t_s2)
print()

#Row String 출력(파일경로를 복사할 때 유용)
raw_s1 = r'D:\Python\test'

print(raw_s1)

#멀티라인 입력
#multe_str = "asdfjasdlfkjadlskfjklasfjgggggggggggggggggggggggggggggggggg"
multi_str = \
'''
String
Multi line
Test
'''
print(multi_str)

#문자열 연산
str_o1 = "phython"
str_o2 = "Apple!"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3) #세번 반복
print(str_o1+str_o3)
print('y' in str_o1)  # str_o1 에 y가 있니?
print('n' in str_o1)  # str_o1 에 n가 있니?
print('P' not in str_o2) # 대소문자 구별


# 문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1),type(str(10.1)))
print(str(False), type(str(False)))

# 문자열 함수 (upper, isalnum, startswith, countm endswith, isalpha...)
#1. 첫 번째 시작 문자를 대문자로 변환
print("Capitalize: ", str_o1.capitalize())
#2. 마지막에 해당 문자가 들어 있는지 (True/False)
print("endswith?: ", str_o2.endswith("!"))
#3. 특정 문자 변환
print("replace", str_o1.replace("phy","GOOD"))
#4. 정렬
print("sorted : ",sorted(str_o1))
#5. 특정 문자로 구분을 주어 배열로 변환
print("split : ", str_o4.split(' '))


#반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) #__iter__

for i in im_str :
    print(i)

#슬라이싱 연습
str_s1 = "Nice Python"
print(str_s1[0:4]) # 0 1 2 3
print(str_s1[5:11])
print(str_s1[5:]) #5부터 끝까지 가져와!
print(str_s1[:len(str_s1)])
print(str_s1[1:9:2]) #2칸씩 띄어서
print(str_s1[-5:]) #음수는 뒤에서 샌다
print(str_s1[::2])
print(str_s1[::-1]) # 거꾸로 출력