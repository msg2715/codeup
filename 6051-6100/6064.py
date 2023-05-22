# 문제정보 : https://codeup.kr/problem.php?id=6064

# 풀이
a, b, c = map(int, input().split())
print((a if (a <= b) else b) if ((a if (a <= b) else b)<c) else c)