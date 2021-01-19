def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def solve():
    n,sum = read_int_arr()
    arr = read_int_arr()
    dp = [[False for i in range(sum+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True
            elif arr[i-1]<=j:
                if dp[i-1][j-arr[i-1]]:
                    dp[i][j] =  dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum]
t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(ans)
'''
1
3 14
2 3 7 8 10
'''
