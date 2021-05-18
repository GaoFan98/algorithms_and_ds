def nearest_sqrt(num):
    if num < 0:
        return ValueError

    if num == 1:
        return 1

    low = 0
    high = (num / 2) + 1

    while low + 1 < high:
        mid = low + (high - low)
        square = mid ** 2

        if square == mid:
            return mid

        elif square < num:
            low = mid

        else:
            high = mid


out = nearest_sqrt(16)
print(out)
