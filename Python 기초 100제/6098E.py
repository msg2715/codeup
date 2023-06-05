# 문제정보 : https://codeup.kr/problem.php?id=6098

# 풀이
xy = []
ax, bx = 1, 1
for p in range(10):
	xy.append(list(map(int, input().split())))

while xy[ax][bx] != 2: # 현재 자신의 위치에 있는 숫자가 2가 될 때 까지 반복
    xy[ax][bx] = 9 # 현재 자신의 위치를 9로 설정
    if xy[ax][bx+1] == 0 or xy[ax][bx+1] == 2: # 자신의 오른쪽 위치에 있는 숫자가 0 or 2
        bx += 1 # 오른쪽으로 이동
    elif xy[ax+1][bx] == 0 or xy[ax+1][bx] == 2: # 자신의 아래쪽 위치에 있는 숫자가 0 or 2
        ax += 1 # 아래쪽으로 이동
    else:
        break
xy[ax][bx] = 9 # 자신의 위치를 9로 설정

for x in range(10): # 결과 출력
    for y in range(10):
        print(xy[x][y], end=' ')
    print()