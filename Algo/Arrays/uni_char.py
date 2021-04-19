def uni_char(s):
    dict = {}

    if len(s) < 1:
        return False

    for l in s:
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1
            return False

    return bool(dict) if bool(dict) else False


out = uni_char('abcs')
print(out)
