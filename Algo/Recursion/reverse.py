def reverse(s):
    if len(s) <= 1:
        return s

    return s[-1:] + reverse(s[:-1])


out = reverse('Hello world')
print(out)
