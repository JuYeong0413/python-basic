# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) ## len() : 공백 포함 길이


# 빈 문자열
str1_t1 = ''
str2_t2 = str() ## 오브젝트 호출

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# I'm Boy
print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"regro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test' ## 있는 그대로 표시
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
'''
String
Multi line
Test
'''

print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul!Daejeon!Busan!Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)


print("Capitalize: ", str_o1.capitalize()) ## 첫 번째 글자를 대문자로 바꿔준다.
print("endswith?: ", str_o2.endswith("!"))
print("replace", str_o1.replace("thon", ' Good'))
print("sorted: ", sorted(str_o1)) ## 정렬해서 리스트 형태로 반환
print("split: ", str_o4.split('!'))

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str)) # __iter__

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_sl = "Nice Python"
print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3]) # 0 1 2
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_sl[:10]
print(str_sl[1:9:2]) ## 몇 개 단위로 점프하면서 가져오는지
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2]) ## 처음부터 끝까지 두 칸 간격으로
print(str_sl[::-1])

# 아스키 코드(또는 유니코드)
a = 'z'
# 아스키 코드로
print(ord(a)) ## z에 해당하는 아스키 숫자 값은 122
# 문자로
print(chr(122)) ## 아스키 코드 -> 알파벳
