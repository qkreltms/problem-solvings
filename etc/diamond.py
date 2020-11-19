# # def f(n):
# #     space = 0
# #     star = 1
# #     sw = 0
# #     m = n//2
# #
# #     for k in range(n):
# #         if sw == 0:
# #             print(' '*(m+space), end='')
# #             print('*'*star)
# #
# #             if (m + space) == 0:
# #                 sw = 1
# #                 space = 0
# #                 continue
# #             star += 2
# #             space -= 1
# #         else:
# #             star -= 2
# #             space += 1
# #             print(' '*space, end='')
# #             print('*'*star)
# #
# #
# # f(7)
# #
# #
# # def f(n):
# #     for i in range(1, n + 1, 2):
# #         print('{:^{padding}}'.format('*' * i, padding=n))
# #     for i in range(n - 3, 0, -2):
# #         print('{:^{padding}}'.format('*' * i, padding=n))
# #
# # f(100)

# # 2020-02-14
# def diamond(n):
#     if n % 2 == 0:
#         return None
#     if n <= 0:
#         return None
#     m = n // 2
#     cnt = 1
#     for i in range(0, n, 1):
#         if i <= n//2:
#             star = i * 2 + 1
#             print((" " * m) + ("*" * star))
#             m -= 1
#             if m < 0:
#                 m = 0
#         else:
#             m += 1
#             print(" " * m + "*" * (star - cnt * 2))
#             cnt += 1
# diamond(3)
# diamond(1)
# diamond(0)
# diamond(-1)
'''
h는 홀수만 가능
h=1
*

h=3
 *
***
 *
h=5
    *
   ***
  *****
   ***
    *
    h=7
     *
    ***
   *****
  *******
   *****
    ***
     *
'''
'''
1,3,5,3,1
1,3,5,7,5,3,1
* = 1, 1+(i*2) (i=0, ..., h//2+1)
2 1 0 1 2
3 2 1 0 1 2 3
' ' = h//2, ...,0  (i=-1)

h//2+1 까지만 돌고 거쳐간 i는 저장한다.
저장한 i 배열로 나머지를 순회한다.
'''


def f(h):
    step = []
    step2 = []
    for i in range(0, h//2+1):
        print(' '*(h//2-i), end='')
        print('*'*(1+(i*2)))
        step.append(i)
        step2.append(1+(i*2))
    step.pop()
    step2.pop()
    step2.reverse()
    for i in step:
        print(' '*(i+1), end='')
        print('*'*step2[i])


f(1)
f(3)
f(5)
f(7)
f(9)

