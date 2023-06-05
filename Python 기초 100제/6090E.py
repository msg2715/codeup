# 문제정보 : https://codeup.kr/problem.php?id=6090

# 1차시도
"""
a, m, d, n = map(int, input().split())
p = 1
result = []
for x in range(round(n+1)):
    p *= m
    result.append(p)
    p += d
    result.append(p)
print(result)
print(result[n+6])
"""

# 풀이
a, m, d, n = map(int, input().split())
count = 1
while count != n:
    a *= m
    a += d
    count += 1
print(a)