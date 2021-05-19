def unique_int(id_list):
    unique_int = 0

    for i in id_list:
        unique_int ^= i

    return unique_int


out = unique_int([1, 2, 3, 2, 1])
print(out)

# Bitwise XOR check
