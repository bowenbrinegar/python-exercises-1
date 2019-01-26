import unittest

def battleship(m):
    clearRow = []
    for i in range(len(m[0])):
        clearRow.append(0)

    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 0:
                m[row] = clearRow

    print(m)
    return m

class test(unittest.TestCase):
    def test1(self):
        m = [
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,0,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,0,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1]
        ]
        
        res = battleship(m)

        for y in res[2]:
            self.assertEqual(y, 0)

        for y in res[6]:
            self.assertEqual(y, 0)
        



unittest.main()