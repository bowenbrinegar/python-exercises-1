import unittest

def productOfThree(list):
    cp = list

    highest = max(cp[0], cp[1])
    lowest = min(cp[0], cp[1])

    highest_product_2 = cp[0] * cp[1]
    lowest_prodcut_2 = cp[0] * cp[1]

    prod_of_three = cp[0] * cp[1] * cp[2]

    for i in range(2, len(cp)):
        prod_of_three = max(prod_of_three, highest_product_2 * cp[i], lowest_prodcut_2 * cp[i])

        highest_product_2 = max(highest_product_2, highest * cp[i], lowest * cp[i])
        lowest_prodcut_2 = min(lowest_prodcut_2, highest * cp[i], lowest * cp[i])

        highest = max(highest, cp[i])
        lowest = min(lowest, cp[i])


    return prod_of_three

class tests(unittest.TestCase):
    def test1(self):
        res = productOfThree([1,2,3,4])
        self.assertEqual(24, res)

    def test2(self):
        res = productOfThree([1,2,3])
        self.assertEqual(6, res)

    def test3(self):
        res = productOfThree([1,2,-3,4,-6])
        self.assertEqual(72, res)

unittest.main()