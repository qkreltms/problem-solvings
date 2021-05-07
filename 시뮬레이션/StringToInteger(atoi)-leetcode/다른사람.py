def myAtoi(self, str: str) -> int:
    # runtime: 32ms
    import re
    str = str.strip()
    str = re.findall('^[\+\-]*\d+', str)
    MAX, MIN = 2**31-1, -2**31
    try:
        res = int("".join(str))
        return max(min(res, MAX), MIN)
    except:
        return 0