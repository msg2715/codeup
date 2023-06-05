# 문제정보 : https://codeup.kr/problem.php?id=6070

# 풀이
a = int(input())
if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")