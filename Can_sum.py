def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
# using Memoization
def can_sum(current_sum,target,arr,index,memo):
    tt = memo.get((index,current_sum))
    if tt!= None:
        return tt
    if target == current_sum:
        return True
    elif (target<current_sum or target>current_sum) and index>=len(arr):
        return False
    else:
        temp = can_sum(current_sum,target,arr,index+1,memo)#Excluding current sum
        memo[(index+1,current_sum)] = temp
        if current_sum+arr[index]<=target:
            temp_2 = can_sum(current_sum+arr[index],target,arr,index+1,memo)
            memo[(index+1,current_sum+arr[index])] = temp_2
        else:
            temp_2 = False
        if temp:
            return True
        elif temp_2:
            return True
        else:
            return False
def solve():
    target = read_int()
    arr = read_int_arr()
    return  can_sum(0,target,arr,0,dict())
t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(ans)
'''
1
7
5 3 4 7
'''
