# 문제정보 : https://codeup.kr/problem.php?id=6087

# 풀이
a = int(input())
for x in range(1, a+1):
    if not x % 3 == 0:
        print(x, end=' ')