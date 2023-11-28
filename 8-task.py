def myAtoi(self, s: str) -> int:
    result = ''
    space = True
    minus = True
    for i in s:
        if i in '-+' and minus:
            result += i
            minus = False
            space = False
        elif i.isdigit():
            result += i
            space = False
            minus = False
        elif i in " " and space:
            continue
        else:
            break
    try:
        n = int(result)
        if 2 ** 31 - 1 >= n >= -2 ** 31:
            return n
        elif n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return -2 ** 31
    except ValueError:
        return 0

