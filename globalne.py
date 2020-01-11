import unittest
a = 3
class T(unittest.TestCase):

    def setUp(self):
        T.a = 8

    def test1hh(self):
        T.a = T.a *6
        print(T.a)


    def test2(self):
        pass


if __name__== "__main__":
    unittest.main()