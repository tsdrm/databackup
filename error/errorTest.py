import unittest

from error import error


class MyTestCase(unittest.TestCase):
    def test_error(self):
        message = "halo, this is a error"
        err = error.new("halo, this is a error")
        err.print()
        self.assertEqual(message, err.string())

        message = "it's just a test error called {}".format('halo')
        err = error.new(message)
        err.print()
        self.assertEqual(message, err.string())


if __name__ == '__main__':
    unittest.main()
