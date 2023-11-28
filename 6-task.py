def convert(s: str, numRows: int):
    if numRows == 1 or numRows == len(s):
        return s
    count = 0

    result = ['' for i in range(numRows)]
    for i in range(len(s)):
        if count == 0:
            result[count] += s[i]
            k = 1
            count += k
        elif count == numRows - 1:
            result[count] += s[i]
            k = -1
            count += k
        else:
            result[count] += s[i]
            count += k
    return ''.join(result)


print(convert("helloworld", 4))
