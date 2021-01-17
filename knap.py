def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def knap(weights,values,index,capacity):
    if index<0 or capacity<=0:
        return 0
    else:
        temp = knap(weights,values,index-1,capacity)   #Excluding current Item
        temp_2 = values[index]+knap(weights, values, index - 1, capacity-weights[index])  # Including current Item
        return max(temp,temp_2)
def solve():
    n,c = read_int_arr()
    weights = read_int_arr()
    values = read_int_arr()
    ans = knap(weights,values,len(weights)-1,c)
    return ans
t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(ans)

