# 문제정보 : https://codeup.kr/problem.php?id=6054

# 1차시도 실패
"""
a = list(map(int, input().split()))
a, b = map(bool, a)
print(a == b) # 0 0을 입력했을 때 오류가 발생
"""

# 풀이
a = list(map(int, input().split()))
a, b = map(bool, a)
print(a and b)