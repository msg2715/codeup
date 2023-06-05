# 문제정보 : https://codeup.kr/problem.php?id=6045

# 풀이
a, b, c = map(int, input().split())
print(f"{a+b+c} {format((a+b+c)/3, '.2f')}")