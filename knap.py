def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
# Knapsack problem with  memoization
def knap(weights,values,capacity,index,memo):
    if index == -1 or capacity <= 0:
        return 0
    elif memo[index][capacity] != -1:
        print(memo)
        return memo[index][capacity]
    else:
        temp = knap(weights,values,capacity,index-1,memo)
        temp_2 = values[index]+knap(weights,values,capacity-weights[index],index-1,memo)
        memo[index][capacity] = max(temp_2,temp)
        return memo[index][capacity]
def solve():
    n,c = read_int_arr()
    weights = read_int_arr()
    values = read_int_arr()
    dp = [[-1 for i in range(c+1)]for i in range(n+1)]
    ans =  knap(weights,values,c,n-1,dp)
    print(dp)
    return ans
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

'''
