import numpy as np
import linear
import uniitest

class Test(uniitest.TestCase):

    def test_inverse(self):
        z = np.array([[37, 20, 12],
                      [15, 32, 4],
                      [5,  40, 2]
                     ])
        r = np.array([[435],[178],[70]])
        result = linear.inverse(z,r)
        X = [[10.  ]
            [ 0.25]
            [ 5.  ]]
        self.assertEquals(result, X)

    def test_solve(self):
        z = np.array([[37, 20, 12],
                      [15, 32, 4],
                      [5,  40, 2]
                     ])
        r = np.array([[435],[178],[70]])
        import numpy as np
        # Method 2: Using solve() function
        result = np.linalg.solve(z,r)
        self.assertEquals(result, y)

    def test_concatenation(self):
        import numpy as np
        # Concatenation
        a = np.array([[37, 20, 12]])
        b = np.array([[15, 32, 4]])
        c = np.array([[5,  40, 2]])
        result = np.concatenate((a, b, c), axis=0)
        self.assertEquals(result, u)
