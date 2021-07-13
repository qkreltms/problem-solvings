'''
'''
from re import compile
def solution(book):
    book.sort()
    for p in book:
        regex = compile("^"+p)
        for target in book:
            if target == p:
                continue
            if regex.match(target):
                return False
    return True