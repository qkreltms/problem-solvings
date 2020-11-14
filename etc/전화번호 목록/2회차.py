from re import compile 
def solution(phone_book):
  for pb1 in phone_book:
    # pb1로 시작하는지 찾는 regex
    regex = compile("^"+pb1)
    for pb2 in phone_book:
      if pb1 != pb2:
        if regex.match(pb2):
          return False
  return True


print(solution(["119", "97674223", "1195524421"]), False)
print(solution(["123", "456", "789"]), True)
print(solution(["12", "123", "1235", "567", "88"]), False)