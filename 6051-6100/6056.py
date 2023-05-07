# 문제정보 : https://codeup.kr/problem.php?id=6056

# 풀이
a = list(map(int, input().split()))
a, b = map(bool, a)
print(a ^ b)