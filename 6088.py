# 문제정보 : https://codeup.kr/problem.php?id=6088

# 풀이
a, d, n = map(int, input().split())
result = []
for x in range(1, n):
    a += d
    result.append(a)
print(result[-1])