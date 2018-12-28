import unittest

from error import error

class MyTestCase(unittest.TestCase):
    def test_error(self):
        err = error.Error()
        err.new("halo")
        err.print()

        err = error.Error()
        err.print()



if __name__ == '__main__':
    unittest.main()
