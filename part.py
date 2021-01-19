def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def solve():
    n = read_int()
    arr = read_int_arr()

    if sum(arr)%2 == 0:
        cols = sum(arr)//2
        dp = [[False for i in range((cols)+1)] for i in range(n+1)]
        for i in range(n+1):
            for j in range(cols+1):
                if i == 0 :
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
                elif arr[i-1]<= cols:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][cols]
    else:
        return False

t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(ans)
'''
1 
4
2 4 10 2
'''
