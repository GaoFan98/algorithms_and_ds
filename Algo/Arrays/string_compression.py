def str_compress(s):
    dict = {}

    if len(s) < 1:
        return False

    for l in s:
        if l not in dict:
            dict[l] = 1
        else:
            dict[l] += 1

    concated = ''

    for key, value in dict.items():
        concated += key + str(value)

    return concated


out = str_compress('AABBBCDdddeEfF')
print(out)
