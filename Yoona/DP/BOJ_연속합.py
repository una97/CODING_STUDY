'''
문제 이해 9분
구현 10분 미만이나 한 번 틀렸다.
첫번째 시도는 arr[i]와 arr[i-1]+arr[i]와 sum(arr[:i-1])+arr[i] 중 max를 구했는데,
그렇다 보니 중간에서부터 더했을 때 최대가 나오는 부분을 놓쳤었다.

이 문제의 점화식은
dp[i] = dp[i-1] + arr[i]

10
10 -4 3 1 5 6 -35 12 21 -1

10
2 1 -4 3 4 -4 6 5 -5 1

5
-1 -2 -3 -4 -5

'''

def sol(arr):
    dp =[0]*len(arr)
    dp[0] = arr[0]

    for i in range(1,len(arr)):
        val = max(arr[i], dp[i-1]+arr[i]) #현재 값과 이전의 값+현재값 중에 큰 것
        dp[i] = val
    maxV = max(dp)

    return maxV

def sol2(arr):
    for i in range(1,len(arr)):
        val = max(arr[i],arr[i-1]+arr[i])
        arr[i] = val
    maxV = max(arr)
    return maxV

N=int(input())
arr= list(map(int, input().split()))
print(sol(arr))
print(sol2(arr))