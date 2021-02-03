def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def create_mat(a,n,m):
    return [[a for i in range(m)] for i in range(n)]
def p(n,k):
    if k>n:
        return 0
    elif k==0:
        return 1
    else:
        return k*p(n-1,k-1)+p(n-1,k)

def solve():
    n,k = read_int_arr()
    dp = create_mat(0,n+1,k+1)
    for i in range(n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = j*dp[i-1][j-1]+dp[i-1][j]
    print(dp[n][k])
t = read_int()
for _ in range(1,t+1):
    print('Case #{}:'.format(_),end=' ')
    solve()
'''
1
100 50

'''
