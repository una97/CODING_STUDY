import sys

'''
6
10 20 10 30 20 50
구간 최댓값, 값 업데이트는 세그멘트 트리와 같은 자료구조로 O(nlogn)이고,
비교할 횟수가 n번이므로 총 O(nlong)
'''
def sol2(arr):
    dp = [0]*len(arr)

    dp[0] = 1 #초기화
    for i in range(1,len(arr)):
        maxV = 0
        # dp[i] =1
        for j in range(i):
            if arr[j]<arr[i] and maxV<dp[j]:
                # dp[i] = max(dp[i],dp[j]+1)
                maxV =dp[j]
        dp[i] = maxV+1

    # for i in range(1,len(arr)):
    #     val = 0
    #     for j in range(i):
    #         if arr[j]<arr[i]:
    #             val = max(val,dp[j])
    #     dp[i] = val+1

        # if arr[i] > arr[i-1]:
        #     val =0
        #     for j in range(i):
        #         if arr[j]<arr[i]:
        #             val = max(val,dp[j])
        #
        #     dp[i] = max(dp[i-1], val)+1
        #     # print(val)
        # elif arr[i] < arr[i-1]:
        #     val = 0
        #     for j in range(i):
        #         if arr[j] < arr[i]:
        #             val = max(val, dp[j])
        #     if val==0:
        #         dp[i]=1
        #     else:
        #         dp[i] = val + 1
        # elif arr[i]==arr[i-1]:
        #     dp[i] = dp[i-1]
        print(dp)
    return max(dp)

def sol(arr):

    dp = [0]*len(arr)

    dp[0] = 1 #초기화
    for i in range(1,len(arr)):
        maxV = 0
        # dp[i] =1
        for j in range(i):
            if arr[j]<arr[i] and maxV<dp[j]:
                # dp[i] = max(dp[i],dp[j]+1)
                maxV =dp[j]
        dp[i] = maxV+1
    return max(dp)


N = int(input())
arr = list(map(int,input().split()))
print(sol(arr))
print(sol([30,30,30]))
print(sol([30,10,20,10,10,10]))
print(sol([10,20,30,40,60,10,20,30,50,90,30]))