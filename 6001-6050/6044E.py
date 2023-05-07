# 문제정보 : https://codeup.kr/problem.php?id=6044

# 1차시도 실패
"""
a, b = map(int, input().split())
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{format(a/b,".2f")}")
"""

# 풀이
a, b = map(int, input().split())
print(f"{a+b}\n{a-b}\n{a*b}\n{a//b}\n{a%b}\n{format(a/b,'.2f')}")