'''
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

1
5
50 10 100 20 40
30 50 70 10 60
'''
#
# def sol(A,N):
#     if N == 1:
#         return max(A)
#
#     dp = [[0]*N for _ in range(2)] # [[0]*N]*2 랑은 다른 얘기임
#
#     #초기화
#     dp[0][0] = A[0][0]
#     dp[1][0] = A[1][0]
#     #이렇게 안하고 dp를 하나 더 크게 선언하고, 0번째 열에 다 0으로 채워도 된다.
#     dp[0][1] = A[0][1]+dp[1][0]
#     dp[1][1] = A[1][1] + dp[0][0]
#
#
#     for col in range(2,N):
#         for row in range(2):
#             if row == 0:
#                 dp[row][col] = A[row][col] + max(dp[row+1][col-1],dp[row+1][col-2])
#             else:
#                 dp[row][col] = A[row][col] + max(dp[row-1][col-1], dp[row-1][col-2])
#
#     return max(map(max, dp))
def sol(A, N):
    if N == 1:
        return max(A)

    dp = [[0] * (N + 1) for _ in range(2)]  # [[0]*N]*2 랑은 다른 얘기임

    # 초기화
    dp[0][1] = A[0][0]
    dp[1][1] = A[1][0]

    for col in range(2, N+1):
        for row in range(2):
            if row == 0:
                dp[row][col] = A[row][col-1] + max(dp[row + 1][col - 1], dp[row + 1][col - 2])
            else:
                dp[row][col] = A[row][col-1] + max(dp[row - 1][col - 1], dp[row - 1][col - 2])
    print(dp)
    return max(dp[0][N], dp[1][N])
tests = int(input())

for _ in range(tests):
    N = int(input())
    A = [list(map(int,input().split())) for _ in range(2)]
    print(sol(A,N))