# 문제정보 : https://codeup.kr/problem.php?id=6067

# 풀이
a = int(input())
if a < 0:
    if a % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")