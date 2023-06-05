# 문제정보 : https://codeup.kr/problem.php?id=6096

# 풀이
xy = []
for q in range(19): # 바둑판 입력받기
    xy.append(list(map(int, input().split())))


n = int(input())
for p in range(n): # 십자 뒤집기 좌표 입력받고 뒤집기
	x, y = map(int, input().split())
	x -= 1
	y -= 1
	for a in range(19): # 세로줄 뒤집기
		if xy[a][y] == 0:
			xy[a][y] = 1
		else:
			xy[a][y] = 0
	for b in range(19): # 가로줄 뒤집기
		if xy[x][b] == 0:
			xy[x][b] = 1
		else:
			xy[x][b] = 0

for n in range(19): # 십자 뒤집기 결과 출력
    for m in range(19):
        print(xy[n][m], end=' ')
    print()