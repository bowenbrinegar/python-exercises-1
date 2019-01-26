
import unittest

def swap(letters, right, left):
    temp = letters[right]
    letters[right] = letters[left]
    letters[left] = temp

def permutations(letters, pos, results):
    if (pos == 0):
        word = ''
        for l in letters:
            word = word + l
        results.append(word)
    else:
        for i in range(pos):
            permutations(letters, pos - 1, results)

            if pos % 2 == 0:
                swap(letters, 0, pos - 1)
            else:
                swap(letters, i, pos - 1)

    return results

def reverse(str):
    return str[::-1]

def checkPalindrome(original, perms):
    for word in perms:
        if original == reverse(word):
            return True
    return False


def main(str):
    letters = list(str)
    perms = permutations(letters, len(letters), [])
    return checkPalindrome(str, perms)



class tests(unittest.TestCase):
    def test1(self):
        self.assertTrue(main('cats'))

    def test2(self):
        self.assertTrue(main('bob'))


unittest.main()