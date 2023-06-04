# 문제정보 : https://codeup.kr/problem.php?id=6093

# 풀이
a = int(input())
b = list(map(int, input().split()))
b = b[::-1]
for i in b:
    print(i, end=' ')