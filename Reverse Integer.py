def reverse(x: int) -> int:
    if x < 0:
        x = -x
        n = -int(str(x)[::-1])
        return n if n > -2 ** 31 else 0
    else:
        n = int(str(x)[::-1])
        return n if n < 2 ** 31 else 0


print(reverse(-123))
