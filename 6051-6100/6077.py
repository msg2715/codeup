# 문제정보 : https://codeup.kr/problem.php?id=6077

# 풀이
a = int(input())
result = 0
for x in range(a + 1):
    if x % 2 == 0:
        result += x
print(result)