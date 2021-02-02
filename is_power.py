def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def pp(a,n):
    if n == 0:
        return 1
    else:
        half = pp(a,n//2)
        if n%2 == 0:
            return  half*half
        else:
            return half * half*a
def solve():
    ans = 0
    n = read_int()
    inc = 1;temp = 2
    while temp<n:
        temp = pp(2,inc)
        inc+=1
    if temp == n:
        print(True)
    else:
        print(False)
t = read_int()
for _ in range(1,t+1):
    print('Case #{}:'.format(_),end=' ')
    solve()
'''
2
31
64
'''
