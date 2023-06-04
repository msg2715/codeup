# 문제정보 : https://codeup.kr/problem.php?id=6091

# 1차시도
"""
a, b, c = map(int, input().split())
result = 1
while result % a != 0 and result % b !=0 and result % c != 0:
    result += 1
print(result)
"""

# 결과
a, b, c = map(int, input().split())
result = 1
while result % a != 0 or result % b !=0 or result % c != 0:
    result += 1
print(result)