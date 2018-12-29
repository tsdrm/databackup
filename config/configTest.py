import unittest

import os

import xmlrunner

from config import config


class MyTestCase(unittest.TestCase):
    def test_config(self):
        conf = config.new_config("./test/user.conf")
        conf.print()
        self.assertEqual(len(conf.info), 4)
        self.assertEqual(conf.info["key1"], 'key1')
        self.assertEqual(conf.info["key2"], '')
        self.assertEqual(conf.info["key3"], 'key3')
        self.assertEqual(conf.info["key4"], '"http://www.baidu.com"')


if __name__ == '__main__':
    print("Current path is: %s", os.getcwd())
    # unittest.main()
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(MyTestCase))
    runner = xmlrunner.XMLTestRunner(output='report')#指定报告放的目录
    runner.run(test_suite)
