import unittest

def dfs(row, col, m):
    if row + 1 < len(m) and m[row + 1][col] == 1:
            m[row + 1][col] = 0
            dfs(row + 1, col, m)
    if row > 0 and m[row - 1][col] == 1:
            m[row - 1][col] = 0
            dfs(row - 1, col, m)
    if col + 1 < len(m[0]) and m[row][col + 1] == 1:
            m[row][col + 1] = 0
            dfs(row, col + 1, m)
    if col > 0 and m[row][col - 1] == 1:
            m[row][col - 1] = 0
            dfs(row, col - 1, m)

def island(m):
    count = 0
    
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == 1:
                dfs(row, col, m)
                count += 1

    return count


class test(unittest.TestCase):
    def test1(self):
        m = [
            [1,1,0,1,0,0,0],
            [0,1,0,0,0,0,0],
            [0,1,0,0,1,1,1],
            [0,0,1,0,0,0,1],
            [0,0,0,0,0,0,1],
            [0,1,0,1,0,0,0]
        ]
        
        self.assertEqual(6, island(m))

unittest.main()