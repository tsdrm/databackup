import unittest

import os

from config import config

class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)
    def test_halo(self):
        c = config.Config()
        c.read_file(".\\test\\user.conf")


if __name__ == '__main__':

    print("Current path is: %s", os.getcwd())
    unittest.main()
