import sys
file = open('in.txt')
sys.stdin = file

t = int(input())
p = 0
n = 0
z = 0

for x in input().split():
    x = int(x)
    if x < 0:
        n += 1
    elif x > 0:
        p += 1
    else:
        z += 1

print("%.3f" % float(p/t))
print("%.3f" % float(n/t))
print("%.3f" % float(z/t))
