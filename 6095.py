# 문제정보 : https://codeup.kr/problem.php?id=6095

# 풀이
xy = []
for i in range(20):
    xy.append([])
    for j in range(20):
        xy[i].append(0)

n = int(input())
for z in range(n):
    x, y = map(int, input().split())
    xy[x][y] = 1

for n in range(1, 20):
    for m in range(1, 20):
        print(xy[n][m], end=' ')
    print()