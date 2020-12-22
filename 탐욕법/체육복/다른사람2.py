'''
set을 써서 중복을 제거했다 왜 난 그생각을 못했을까?
'''
def solution(n, lost, reserve):
    reserved = 0
    lostN = list(set(lost) - set(reserve))
    reserveN = list(set(reserve) - set(lost))
    lostN.sort()
    for l in lostN:
        for x in range(l-1, l+2):
            if x in reserveN:
                reserveN.remove(x)
                reserved += 1
                break
    return n - len(lostN) + reserved