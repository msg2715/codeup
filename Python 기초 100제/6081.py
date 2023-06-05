# 문제정보 : https://codeup.kr/problem.php?id=6081

# 풀이
a = input()
n = int(a, 16)
for x in range(1, 16):
    print(f"{'%X' % n}*{'%X' % x}={'%X'%(n*x)}")