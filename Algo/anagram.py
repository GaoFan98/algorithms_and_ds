def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s1.replace(' ', '').lower()

    return s1 == s2


out = anagram('clint eastwood', 'old west action')
print(out)
