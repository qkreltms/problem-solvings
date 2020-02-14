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
# def f(n):
#     for i in range(1, n + 1, 2):
#         print('{:^{padding}}'.format('*' * i, padding=n))
#     for i in range(n - 3, 0, -2):
#         print('{:^{padding}}'.format('*' * i, padding=n))
#
# f(100)

# 2020-02-14
def diamond(n):
    if n % 2 == 0:
        return None
    if n <= 0:
        return None
    m = n // 2
    cnt = 1
    for i in range(0, n, 1):
        if i <= n//2:
            star = i * 2 + 1
            print((" " * m) + ("*" * star))
            m -= 1
            if m < 0:
                m = 0
        else:
            m += 1
            print(" " * m + "*" * (star - cnt * 2))
            cnt += 1
diamond(3)
diamond(1)
diamond(0)
diamond(-1)

















