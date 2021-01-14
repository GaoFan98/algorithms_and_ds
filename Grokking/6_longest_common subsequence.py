def longest_common_substr(input_word, actual_word):
    grid = [[0 for x in range(len(actual_word))] for y in range(len(input_word))]

    result = 0

    for inp in range(len(input_word)):
        for act in range(len(actual_word)):
            if input_word[inp] == actual_word[act]:
                grid[inp][act] = grid[inp - 1][act - 1] + 1
                result = max(result, grid[inp][act])
            else:
                grid[inp][act] = max(grid[inp - 1][act], grid[inp][act - 1])

    return result


out = longest_common_substr('fosh', 'fort')
print(out)
