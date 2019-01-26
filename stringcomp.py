import unittest

def compress(s):
    prev = None
    count = 0
    results = {}

    for i in range(len(s)):
        if prev != s[i]:
            count = 1
        results[s[i]] = count
        prev = s[i]
        count += 1

    final = ''
    for key, value in sorted(results.items()):
        if value == 1:
            final = final + key
        else:
            final = final + key + str(value)

    return final

class tests(unittest.TestCase):
    def test1(self):
        self.assertEqual('a3b4c2d', compress('aaabbbbccd'))

    def test2(self):
        self.assertEqual('abcd', compress('abcd'))

unittest.main()