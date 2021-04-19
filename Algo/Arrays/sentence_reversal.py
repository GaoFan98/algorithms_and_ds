def sentence_reversal(s):
    return (' '.join(s.split()[::-1]))


out = sentence_reversal('     Hello         world!')
print(out)
