# Chapter09-2
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제1
with open('./resource/test1.csv', 'r') as f:
    reader = csv.reader(f) ## open 함수에서의 변수를 reader에다가 인자료 넘겨주면 csv파일을 사용할 준비가 되었다는 것
    # next(reader) # Header Skip
    # 객체 확인
    print(reader)
    # 타입 확인
    print(type(reader))
    # 속성 확인
    print(dir(reader)) # __iter__
    print()

    for c in reader:
        # print(c)
        # 타입 확인(리스트)
        # print(type(c))
        print(' : '.join(c))

# 예제2
with open('./resource/test2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') ## 잘못된 구분자를 사용하면 하나로 가져옴

    for c in reader:
        print(c)

# 예제3
with open('./resource/test1.csv', 'r') as f:
    reader = csv.DictReader(f)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        # print(c)
        for k, v in c.items():
            print(k, v)
        print('--------------')
