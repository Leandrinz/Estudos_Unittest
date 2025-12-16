import unittest

def setUpModule():
    print(">> setUpModule")

def tearDownModule():
    print(">> tearDownModule")

class TestCiclo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(">> setUpClass")

    @classmethod
    def tearDownClass(cls):
        print(">> tearDownClass")

    def setUp(self):
        print(">> setUp")

    def tearDown(self):
        print(">> tearDown")

    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()
