# 문제정보 : https://codeup.kr/problem.php?id=6084

# 풀이
h, b, c, s = map(int, input().split())
bit = h * b * c * s / 8
print(round(bit / (1024**2) * 10) / 10, "MB")