# 문제정보 : https://codeup.kr/problem.php?id=6097

# 풀이
wh = [] # 격자판 리스트
w, h = map(int, input().split()) # 격자판의 세로, 가로 지정

for q in range(w): # 입력값대로 격자판 생성
    wh.append([])
    for y in range(h):
        wh[q].append(0)
        
n = int(input())
for p in range(n): # 막대의 길이, 방향, 좌표를 입력하고 격자판 채우기
    l, d, x, y = map(int, input().split())
    if d == 0:
        for l in range(l):
            wh[x-1][y+l-1] = 1
    else:
        for l in range(l):
            wh[x+l-1][y-1] = 1
        
for n in range(w): # 십자 뒤집기 결과 출력
    for m in range(h):
        print(wh[n][m], end=' ')
    print()