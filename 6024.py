"""
6024 : [기초-입출력] 단어 2개 입력받아 이어 붙이기(설명)(py)
시간 제한: 1 Sec  메모리 제한: 128 MB


알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

입력
알파벳과 숫자로 이루어진 2개의 단어가 공백으로 구분되어 입력된다.

출력
입력된 2개의 단어를 순서대로 붙여 출력한다.

입력 예시   
hello world

출력 예시
helloworld
"""

a, b = input().split()
print(a + b)