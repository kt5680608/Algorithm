import sys
from collections import Counter
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

tmp = A*B*C
tmp = str(tmp)
arr = [0] * 10
for i in range(len(tmp)):
    arr[int(tmp[i])] += 1

print(arr)