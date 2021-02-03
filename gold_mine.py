def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def create_mat(a,n,m):
    return [[a for i in range(m)] for i in range(n)]
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
    n,m = read_int_arr()
    mat = []
    dp = create_mat(0,n,m)
    for i in range(n):
       mat.append(read_int_arr())


    for j in range(m-1,-1,-1):
        for i in range(n - 1, -1, -1):
                top_right = 0
                bottom_right = 0
                right = 0
                if i+1<n and j+1<m:
                    bottom_right = dp[i+1][j+1]
                if i-1>=0 and j+1<m:
                    top_right = dp[i-1][j+1]
                if j+1<m:
                    right = dp[i][j+1]
                dp[i][j] = mat[i][j]+max(right,bottom_right,top_right)
    print(dp)
t = read_int()
for _ in range(1,t+1):
    print('Case #{}:'.format(_),end=' ')
    solve()
'''
2
3 3
1 3 3
2 1 4
0 6 4
4 4
1 3 1 5
2 2 4 1
5 0 2 3
0 6 1 2

12 and 16

13 12 6 5
14 11 9 1
16 9 5 3
11 11 4 2

          if m-1 == j:
                dp[i][j] = mat[i][j]
            else:
'''
