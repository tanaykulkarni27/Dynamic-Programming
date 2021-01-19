def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def solve():
    n,cap = read_int_arr()
    wt = read_int_arr()
    prc = read_int_arr()
    dp = [[-1 for i in range(cap+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j>=wt[i-1]:
                dp[i][j] = max(prc[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][cap]
t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(ans)
'''
1
3 50
10 20 30
60 100 120

ans = 220 for this test case
'''
