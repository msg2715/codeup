# 문제정보 : https://codeup.kr/problem.php?id=6080

# 풀이
n, m = map(int, input().split())
for a in range(1, n + 1):
    for b in range(1, m + 1):
        print(a, b)