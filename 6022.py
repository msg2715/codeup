"""
6022 : [기초-입출력] 연월일 입력받아 나누어 출력하기(설명)(py)
시간 제한: 1 Sec  메모리 제한: 128 MB


6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

입력
6자리 숫자로 이루어진 연월일(YYMMDD)이 입력된다.

출력
년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력한다.

입력 예시   
200304

출력 예시
20 03 04
"""

a = input()
print(a[0:2], a[2:4], a[4:6])