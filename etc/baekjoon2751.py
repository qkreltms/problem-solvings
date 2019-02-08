# def merge_sort(src_list):
#     if len(src_list) == 1:  # 길이가 1개 일 경우 더 줄일 수 없음으로 반환
#         return src_list
#     mid = len(src_list) // 2
#     left_list = src_list[:mid]
#     right_list = src_list[mid:]
#     left_list = merge_sort(left_list)
#     right_list = merge_sort(right_list)
#     return merge(left_list, right_list)  # 정렬된 리스트 반환
#
#
# def merge(left_list, right_list):
#     ans = []
#
#     while len(left_list) or len(right_list):  # 둘 중 하나라도 리스트 값이 있을 때
#         if len(left_list) and len(right_list):  # 둘 다 값이 있을 때
#             if left_list[0] <= right_list[0]:  # 대소 구분
#                 ans.append(left_list[0])  # 왼쪽 젤 앞 값을 ans에 넣음
#                 left_list = left_list[1:]  # 왼쪽 한 칸 줄임
#             else:
#                 ans.append(right_list[0])  # 오른쪽 젤 앞 값을 ans에 넣음
#                 right_list = right_list[1:]  # 오른쪽 한 칸 줄임
#
#         elif len(left_list):  # 왼쪽만 값이 있을 경우
#             ans.append(left_list[0])  # 왼쪽 젤 앞 값을 넣음
#             left_list = left_list[1:]  # 왼쪽 한 칸 줄임
#
#         elif len(right_list):  # 오른쪽만 값이 있을 경우
#             ans.append(right_list[0])  # 오른쪽 젤 앞 값을 넣음
#             right_list = right_list[1:]  # 오른쪽 한 칸 줄임
#     return ans
#
# import sys
# n = int(input())
# A = []
# for _ in range(n):
#     A.append(int(sys.stdin.readline()))
#
# for i in merge_sort(A):
#     sys.stdout.write(str(i) + "\n")

import sys
n = int(input())
A = []
for _ in range(n):
    A.append(int(sys.stdin.readline()))

for i in sorted(A):
    sys.stdout.write(str(i) + "\n")
