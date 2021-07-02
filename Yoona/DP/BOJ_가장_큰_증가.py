'''
가장 큰 증가 부분 수열

11
1 100 2 2 50 60 3 5 6 7 8

4
2 2 1 2

5
5 1 3 2 7

3
20 10 15

5
5 1 2 3 10

10
102 100 2 3 4 3 5 6 7 8

2
101 100

10
1 100 2 100 50 60 70 80 90 100
답)453

반례) 앞의 수 몇 개의 값이 중간에 생성되는 증가부분수열의 시작점의 수보다 작고 순서가 역순이거나 할 때 에러가 납니다.
6
5 2 10 13 21 17

풀이법)
증가하는 부분 수열(a[j] < a[i]) 에서,
(d[j]) + 자신의 값(a[i])이 현재 d[i]보다 크면, d[i]를 갱신해준다.
이렇게 되면, 부분 수열도 증가하고 있는 것!
'''
from collections import deque
#반례에 의해 틀린 답
# def sol(arr,N):
#     increasing = deque()
#     increasing.append(arr[0])
#     maxV = arr[0]
#     for i in range(1,N):
#         while increasing:
#             if increasing[-1] > arr[i]:
#                 increasing.pop()
#                 if not increasing:
#                     increasing.append(arr[i])
#                     break
#             elif increasing[-1] < arr[i]: #증가하는 부분이거나 비게 되면 되면 추가하고 끝낸다
#                 increasing.append(arr[i])
#                 break
#             else: # 같은 경우엔 그냥 brek 해주기!!
#                 break
#         print(increasing)
#         maxV = max(maxV,sum(increasing))
#
#     return maxV
import copy
def sol(arr,N):

    dp_len = [0]*N
    dp_len[0] = 1
    dp_val = copy.deepcopy(arr)

    for i in range(1,N):
        max_len = 0
        for j in range(i):
            if arr[j] < arr[i] and max_len<dp_len[j]: #증가하는 부분수열 일 때
                max_len = dp_len[j]
                dp_val[i] = max(arr[i]+dp_val[j], dp_val[i])

        dp_len[i] = max_len+1

    return max(dp_val)

#
# N = int(input())
# arr = list(map(int,input().split()))
# print(sol(arr,N))


import copy
def sol3(arr,N):

    dp_val = copy.deepcopy(arr)

    for i in range(1,N):
        for j in range(i):
            if arr[j] < arr[i] and dp_val[i] < arr[i] + dp_val[j]: #증가하는 부분수열 일 때
                dp_val[i] = arr[i] + dp_val[j]

    return max(dp_val)


N = int(input())
arr = list(map(int,input().split()))
print(sol3(arr,N))