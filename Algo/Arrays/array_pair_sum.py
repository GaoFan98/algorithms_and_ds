def pair_sum(arr, k):
    if len(arr) < 2:
        return False

    seen = set()
    output = set()

    for n in arr:
        target = k - n

        if target not in seen:
            seen.add(n)
        else:
            output.add((min(n, target), max(n, target)))

    return output


out = pair_sum([6, 3, 2, -1], 5)

print(out)
