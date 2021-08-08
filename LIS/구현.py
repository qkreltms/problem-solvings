# def solution(s):
#     m=['zero','one','two','three','four','five','six','seven','eight','nine']
#     for i, e in enumerate(m):
#         j=s.find(e)
#         if j != -1:
#             l=len(e)
#             s=s[0:j]+str(i)+s[j+l:]
#     return int(s)
# print(solution('one4seveneight2three45sixsevensix'))


# def solution(places):
#     global visited
#     visited = []
#     def isInrange(i,j,k,l):
#         if 3 > abs(i-k)+abs(j-l):
#             return True
#         return False
    
#     def guridoogiOk(h,iy,ix,y,x,ly,lx):
#         if x >= 0 and y >= 0 and x <= lx and y <= ly:
#             node = h[y][x]
#             if visited[y][x] or node == 'X':
#                 return
#             if not isInrange(y,x,iy,ix):
#                 return
#             if visited[ly][lx]:
#                 return
#             visited[y][x] = True
#             guridoogiOk(h,y,x,y-1,x,ly,lx)
#             guridoogiOk(h,y,x,y,x+1,ly,lx)
#             guridoogiOk(h,y,x,y+1,x,ly,lx)
#             guridoogiOk(h,y,x,y,x-1,ly,lx)
        
#     def f(h):
#         global visited
#         for i in range(0, 5):
#             for j in range(0, 5):
#                 if h[i][j] == 'P':
#                     for k in range(i, 5):
#                         for l in range(0, 5):
#                             if i == k and l <= j:
#                                 continue
#                             if h[k][l] == 'P':
#                                 if isInrange(i,j,k,l):
#                                     guridoogiOk(h,i,j,i,j,k,l)
#                                     if visited[k][l] == True:
#                                         return 0
#                                     visited = [[False for _ in range(5)] for _ in range(5)]
#         return 1
           
#     ans = []
#     for p in places:                        
#         visited = [[False for _ in range(5)] for _ in range(5)]
#         ans.append(f(p))
#     return ans
    


# print(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]), 0)
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]]), 1)
# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]), 10111)
# print(solution([["XXXXX", 
#                  "PXPXX", 
#                  "OPXXX", 
#                  "XXXXX", 
#                  "XXXXX"]]), 0)
# print(solution([["OOOOP", 
#                  "OOOOX", 
#                  "OOOOP", 
#                  "OOOOO", 
#                  "OOOOO"]]), 0)


