def permute(s):
    out = []

    if len(s) == 1:
        out = [s]

    else:
        for index, el in enumerate(s):
            for perm in permute(s[:index] + s[index + 1:]):
                out += [el + perm]

    return out


out = permute('4630')
print(out)


def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            # print(head[:i])
            # print(head[i + 1:])
            # print(head[i + 1:] + head[:i])
            # print(head[i])
            # print(tail)
            # print(head[i + 1:] + head[:i], head[i] + tail)
            permutations(head[:i] + head[i + 1:], head[i] + tail)


out = permutations('abc')
print(out)
