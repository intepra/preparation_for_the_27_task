#'''
import sys
save_stdin = sys.stdin
sys.stdin = open("in/max1_max2.in")
#'''
n = int(input())
print("test")
max1 = None
max2 = None
min1 = None
min2 = None
for i in range(n):
    a = int(input())
    if max1 is None or ( a >= max1 and a % 2 == 1 ):
        max2 = max1
        max1 = a
    elif max2 is None or ( a >= max2 and a % 2 == 1 ):
        max2 = a
    if  min1 is None or ( a <= min1 and a % 2 == 1 ):
        min2 = min1
        min1 = a
    elif min2 is None or ( a <= min2 and a % 2 == 1 ):
        min2 = a

print(max1, max2)
print(min1, min2)
#'''
sys.stdin = save_stdin
#'''