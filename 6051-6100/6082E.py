# 문제정보 : https://codeup.kr/problem.php?id=6082

# 1차시도
"""
a = int(input())
result = None
for n in range(1, a + 1):
    if n % 3 == 0:
        print("X", end=' ')
    else:
        print(n, end=' ')
"""

# 결과
a = int(input())
result = None
for n in range(1, a + 1):
    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9 :
        print("X", end=' ')
    else:
        print(n, end=' ')