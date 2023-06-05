# 문제정보 : https://codeup.kr/problem.php?id=6086

# 1차시도
"""
m = int(input())
result = 0
p = 1
while result <= m:
    result += p
    p += 1
print(result)
"""

# 풀이
m = int(input())
result = 0
p = 0
while True:
    p += 1
    result += p
    if result >= m:
        break
print(result)