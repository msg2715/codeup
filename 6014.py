"""
6014 : [기초-입출력] 실수 1개 입력받아 3번 출력하기(py)
시간 제한: 1 Sec  메모리 제한: 128 MB


실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

입력
실수 1개가 입력된다.

출력
입력받은 실수를 줄을 바꿔 3번 출력한다.

입력 예시
0.1

출력 예시
0.1
0.1
0.1
"""

a = input()
for x in range(0, 3):
    print(a)