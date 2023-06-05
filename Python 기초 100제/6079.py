# 문제정보 : https://codeup.kr/problem.php?id=6079

# 풀이
a = int(input())
bout = 0
plus_num = 0
while bout < a:
    plus_num += 1
    bout += plus_num
print(plus_num)