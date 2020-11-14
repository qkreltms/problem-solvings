# 통과 되면 안되는 문제인데 통과가 되어버렸다...
phone_book = ['123', '12', '145', '567', '88']

def solution(phone_book):
  phone_book.sort()
  if (len(phone_book) == 1):
    return True
  jubdooau = phone_book[0]
  phone_book = phone_book[1:]
  for i in phone_book:
    if jubdooau == i[0:len(jubdooau)]:
      return False
  return solution(phone_book)

print(solution(phone_book))

## 다른 사람이 푼 방식
## 정규식 사용문제 (젤 괜찮은듯)
import re
def solution(phoneBook):

    for b in phoneBook:
        #정규식 생성
        p = re.compile("^"+b)
        for b2 in phoneBook:
            if b != b2 and p.match(b2):
                return False
    return True

##### 조합을 사용한다
# 예를 들어 [12, 123,145]을 조합하면 ((12,123),(12,145),(123,145))
#  가 나오는데 여기서 비교한다.
# 단 정렬 필수임 왜냐면 [123,12,145]입력시 (123,12)가 나오기 때문에 아래의 로직이 틀릴수 있다.
# 정렬을 안쓰려면 40번째줄 if문을 왼쪽, 오른쪽 두 번비교하면 될듯?
    from itertools import combinations as c
def solution(phoneBook):
    answer = True
    sortedPB = sorted(phoneBook, key= len)
    for (a,b) in c( sortedPB,2):
        if a == b[:len(a)]:
            answer = False
    return answer