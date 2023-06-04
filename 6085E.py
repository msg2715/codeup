# 문제정보 : https://codeup.kr/problem.php?id=6085

# 1차시도
"""
w, h, b = map(int, input().split())
print(f"{round((w * h * b / 8 / 1024**2) * 100) / 100} MB")
"""

# 풀이
w, h, b = map(int, input().split())
MB = round((w * h * b / 8 / 1024**2), 2)
print(f"{'%.2f'% MB} MB")