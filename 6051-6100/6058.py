# 문제정보 : https://codeup.kr/problem.php?id=6058

# 풀이
a = list(map(int, input().split()))
a, b = map(bool, a)
print(not(a or b))