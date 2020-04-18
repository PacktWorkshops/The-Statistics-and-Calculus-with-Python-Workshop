import unittest
import numpy as np
import linear

class TestLinear(unittest.TestCase):

    def test_inverse(self):
        z = np.array([[37, 20, 12],
                      [15, 32, 4],
                      [5,  40, 2]
                     ])
        r = np.array([[435],[178],[70]])
        # result = np.array(linear.inverse(z,r))
        result = np.linalg.inv(z).dot(r)
        X = np.array(  [[10. ], [0.25], [5. ]] )
        print("X: ", type(X), "result: ", type(result))
        np.testing.assert_array_almost_equal(result, X)

    def test_solve(self):
        import numpy as np
        z = np.array([[37, 20, 12],
                      [15, 32, 4],
                      [5,  40, 2]
                     ])
        y = np.array([[10.0], [0.25], [5.0]])
        r = np.array([[435],[178],[70]])
        import numpy as np
        # Method 2: Using solve() function
        result = np.linalg.solve(z,r)
        print("y: ", type(y), "result: ", type(result))
        np.testing.assert_array_almost_equal(result, y)

    def test_concatenation(self):
        import numpy as np
        # Concatenation
        u = np.array([[37, 20, 12],
            [15, 32,  4],
            [ 5, 40,  2]])
        a = np.array([[37, 20, 12]])
        b = np.array([[15, 32, 4]])
        c = np.array([[5,  40, 2]])
        result = np.concatenate((a, b, c), axis=0)
        np.testing.assert_array_equal(result, u)
