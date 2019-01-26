import unittest

# this breaks if its not 3 characters
def scramble(list):
    cp = list
    results = []

    amount = 1
    for i in range(len(cp)):
        amount *= i + 1

    j = 0

    turn = False
    while len(results) < amount:
        if (j == len(cp) - 2):
            j = 0

        if turn:
            temp = cp[j]
            cp[j] = cp[j + 1]
            cp[j+ 1] = temp
            turn = False
        else:
            temp = cp[j + 2]
            cp[j + 2] = cp[j]
            cp[j] = temp
            turn = True

        word = ""
        for k in range(len(cp)):
            word = word + cp[k]

        if not word in results:
            results.append(word)

        j += 1

    return results
        

def permutations(str):
    cp = str
    letters = list(cp)

    final_index = int(len(letters) - 1)
    final_letter = letters[final_index]
    
    letters.pop(final_index)
    
    words = scramble(letters)
    results = []

    for w in words:
        cur = list(w)
        res = []
        for i in range(len(cur) + 1):
            res[i] = final_letter
            
            # stuck here
            
            
            for k in range(len(cur) + 1):
                word = word + cur[k]

            if not word in results:
                results.append(word)

    
    return results

    

class tests(unittest.TestCase):
    def test(self):
        res = permutations('cats')
        self.assertIn("scat", res)
        self.assertIn("csat", res)
        self.assertIn("cast", res)
        self.assertIn("cats", res)
        self.assertIn("scta", res)
        self.assertIn("csta", res)
        self.assertIn("ctsa", res)
        self.assertIn("ctas", res)
        self.assertIn("satc", res)
        self.assertIn("astc", res)
        self.assertIn("atsc", res)
        self.assertIn("atcs", res)
        self.assertIn("sact", res)
        self.assertIn("asct", res)
        self.assertIn("acst", res)
        self.assertIn("acts", res)
        self.assertIn("stac", res)
        self.assertIn("tsac", res)
        self.assertIn("tasc", res)
        self.assertIn("tacs", res)
        self.assertIn("stca", res)
        self.assertIn("tsca", res)
        self.assertIn("tcsa", res)
        self.assertIn("tcas", res)

unittest.main()