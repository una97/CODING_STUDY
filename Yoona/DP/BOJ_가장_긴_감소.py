'''
6
10 30 10 20 20 10

6
10 30 5 20 20 10

4
10 30 5 40

4
10 30 5 10
'''

'''
가장 긴 증가 부분 수열
'''
def sol_increasing(arr,N):
    dp = [1]*N
    for i in range(1,N):
        max_len = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_len = max(max_len,dp[j]) #나보다 작은 것 들 중에 증가 부분수열의 최장 길이를 구한다.
        dp[i] += max_len
    return max(dp)

def sol_increasing2(arr,N):
    dp = [1]*N
    for i in range(1,N):
        for j in range(i):
            if arr[j] < arr[i] and dp[j]>=dp[i]: #나보다 작고, 나보다 증가하는 길이가 작은 애의 것은 신경쓸 필요가 없음.
                dp[i] += 1

    return max(dp)
'''
가장 긴 감소 부분 수열 
'''
def sol_decreasing(arr,N):
    dp = [1]*N
    for i in range(N-2,-1,-1): #거꾸로
        for j in range(N-1,i,-1):
            if arr[j] < arr[i] and dp[j]>=dp[i]: #나보다 작고, 나보다 증가하는 길이가 작은 애의 것은 신경쓸 필요가 없음.
                dp[i] += 1

    return max(dp)


N = int(input())
arr = list(map(int,input().split()))
print(sol_decreasing(arr,N))
print(sol_increasing(arr,N))