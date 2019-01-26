import unittest

def get_max_profit(list):
    cp = list

    max_prof = -100000000000000000000000000

    for i in range(1, len(cp)):
        diff = cp[i] - cp[0]
        if diff > max_prof:
            max_prof = diff

    return max_prof
    

class test(unittest.TestCase):
    def test(self):
        max_prof = get_max_profit([1,3,6])
        self.assertEqual(max_prof, 5)

    def test2(self):
        max_prof = get_max_profit([6,3,1])
        self.assertEqual(max_prof, -3)

    def test3(self):
        max_prof = get_max_profit([6,3,1,8])
        self.assertEqual(max_prof, 2)

unittest.main()