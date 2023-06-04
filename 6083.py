# 문제정보 : https://codeup.kr/problem.php?id=6083

# 풀이
r, g, b = map(int, input().split())
combo = 0
for m in range(r):
	for n in range(g):
		for o in range(b):
			print(m, n, o)
			combo += 1
print(combo)