# n, m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))  # cf. str은 iterable
#
# def dfs(x, y):
#     # 범위 검사
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)
#
# # 미래도시
# INF = int(1e9)
#
# n,m = map(int, input(). split())
#
# graph = [[INF] * (n+1) for _in range(n+1)]
#
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a==b:
#             graph[a][b] = 0
#
# for_ in range(m):
# a,b= map(int, input(), split())
# graph[a][b] = 1
# graph[a][b] = 1
#
# x,k = map(int ,input(), split())
#
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1,n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])
#
# distance = graph[1][k] + graph[k][x]
#
# if distance >= INF:
#     PRINT("-1")
#
# else:
#     print(distance)
#
#
# # 피보나치 소스코드
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
#
# print(fibo(4))
#
# # 피보나치수열 소스코드(재귀적)\
# d = [0] * 100
#
# def fibo(x):
#     # 종료조건 (1혹은 2일때 1을 반환)
#     if x==1 or x==2:
#         return 1
#     if d[x] != 0:
#      return d[x]
#
#     d[x] = fibo(x-1) + fibo(x-2)
#     return d[x]
#
# print(fibo(99))
#
# #------
# d = [0] * 101
#
# def pibo(x):
#     print ('f(' + str(x) + ')', end = ' ')
#     if x ==1 or x ==2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     d[x] = pibo(x-1) + pibo(x-2)
#         return d[x]
# pibo(100)
# #여기서 리스트는 101개 초기화했는데 계산 가능한 피보나치 수열은
# # 100까지이다. 왜 1개가 빌까? memojation 을 위해 1~100까지의
# # 배열을 0으로 초기화했다. 그리고 d[x] = fibo(x-1)+fibo(x-2)
# # 인 점화식을 저장하기위해 하나의 배열이 더필요하다.p212
#
# #배열
# a = list()
# for i in range(10):
#     a.append(i)
# print(a)
#
# a = []
# for i in range(10):
#     tmp = []
#     for j in range(5):
#         tmp.append(j)
#     a.append(tmp)
#
# print(a)
#
# b = [0]*100
# print(b)
#
# b=[[0]*3]*3
# b[1][1] = 1
# print(b)
#
# c = [[0]*3 for _ in range(3)]
# c[1][1] = 1
# print(c)
#
# a = [[0]*4 for i in range(5)]
# for i in a:
#     for j in i:
#         print(j,end=" ")
#     print()
#
# d=[0] * 100
# d[1] = 1
# d[2] = 1
# n = 99
# for i in range(3,n+1):
#     d[i] = d[i-1] + d[i-2]
# print(d[n])
#
# #다이나믹 프로그래밍 p219
x=int(input())
d =[0] * 30001
for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d[x])
#최단경로문제

