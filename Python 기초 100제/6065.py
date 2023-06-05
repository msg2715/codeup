# 문제정보 : https://codeup.kr/problem.php?id=6065

# 풀이
a = list(map(int, input().split()))
for x in a:
    if x % 2 == 0:
        print(x)