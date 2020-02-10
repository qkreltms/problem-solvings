# def f(n):
#     space = 0
#     star = 1
#     sw = 0
#     m = n//2
#
#     for k in range(n):
#         if sw == 0:
#             print(' '*(m+space), end='')
#             print('*'*star)
#
#             if (m + space) == 0:
#                 sw = 1
#                 space = 0
#                 continue
#             star += 2
#             space -= 1
#         else:
#             star -= 2
#             space += 1
#             print(' '*space, end='')
#             print('*'*star)
#
#
# f(7)
#
#
def f(n):
    for i in range(1, n + 1, 2):
        print('{:^{padding}}'.format('*' * i, padding=n))
    for i in range(n - 3, 0, -2):
        print('{:^{padding}}'.format('*' * i, padding=n))
f(100)