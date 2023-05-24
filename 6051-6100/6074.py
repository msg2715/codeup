# 문제정보 : https://codeup.kr/problem.php?id=6074

# 풀이
a = ord(input())
b = ord('a')
while b <= a:
    print(chr(b), end=' ')
    b += 1