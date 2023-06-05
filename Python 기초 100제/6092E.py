# 문제정보 : https://codeup.kr/problem.php?id=6092

# 1차시도
"""
a = int(input())
b = list(map(int, input().split()))
d = []
for i in range(24):
    d.append(0)
for i in range(a):
    d[b[i]] += 1
for i in range(1, 24):
    print(d[i], end='')
"""
a = int(input())
b = list(map(int, input().split()))
d = []
for i in range(24):
    d.append(0)
for i in range(a):
    d[b[i]] += 1
for i in range(1, 24):
    print(d[i], end=' ')