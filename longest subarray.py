def read_int():
    return int(input())
def read_int_arr():
    return [int(i) for i in input().split()]
def read_str_arr():
    return [i for i in input().split()]
def solve():
    ans = []
    i = 0
    arr = read_int_arr()
    while i<len(arr):
        j = i
        k = i+1
        count = 0
        while (j<len(arr) and k<len(arr))and arr[j]<=arr[k]:
            count+=1
            j+=1
            k+=1
        if count>=len(ans):
            ans = arr[i:k]
        i = max(i+1,j)
    return ans
t = read_int()
for _ in range(1,t+1):
    ans = solve()
    print("Case #{}:".format(_),end=' ')
    print(*ans)

