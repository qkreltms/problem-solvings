import sys

a,*b = map(int, sys.stdin.read().split())
print(min(b), max(b))