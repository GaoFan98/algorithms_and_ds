def uni_char(s):
    dict = {}

    for l in s:
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1
            return False

    return bool(dict) if bool(dict) else False


out = uni_char('aabcs')
print(out)
