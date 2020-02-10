# https://www.codewars.com/kata/56747fd5cb988479af000028/
def get_middle(s):
    length = len(s);
    mid = length // 2
    result = ""
    if length % 2 == 0:
        result = s[mid - 1] + s[mid]
    else:
        result = s[mid];
    return result;