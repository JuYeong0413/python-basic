# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85]
print(len(c))
d = [1000, 10000, 'Ace', 'Base', 'Captain'] ## 서로 다른 자료형을 한 리스트 안에 담을 수 있다.
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>')
print('c + d', c + d) ## 리스트 + 리스트 = 리스트
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
