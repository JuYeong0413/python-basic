# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
## 보통 작은따옴표를 많이 사용함
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션
## => 분리가 무엇으로 되어있는지?
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-') ## 파라미터 결합을 '-'으로 시켜준다.
print('python', 'google.com', sep='@')

print()

# end 옵션
## => 끝부분을 어떻게 처리할 것인지?
## print()문은 자동으로 줄바꿈을 해 주지만 end 옵션에 들어간 문자로 다음 print문으로 이어질 수 있다.
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
## 외부 특정한 파일에 내용 작성
import sys ## import => 예약어

print('Learn Python', file=sys.stdout) ## sys.stdout => console out

print()

# format 사용(d, s, f)
## d => 정수(digit)
## s => 문자열(string)
## f => 실수(float)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 2)) ## 좀 더 유연하게 사용 가능
print('{1} {0}'.format('one', 'two')) ## 순서 지정해서 사용 가능
