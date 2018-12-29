import unittest

import os

import config


class MyTestCase(unittest.TestCase):
    def test_config(self):
        # Read configuration file success.
        path = os.path.dirname(__file__) + '/test/user.conf'
        conf = config.new_config(path)
        conf.print()
        self.assertEqual(len(conf.info), 4)
        self.assertEqual(conf.info["key1"], 'key1')
        self.assertEqual(conf.info["key2"], '')
        self.assertEqual(conf.info["key3"], 'key3')
        self.assertEqual(conf.info["key4"], '"http://www.baidu.com"')

        # Configuration file is not exist.
        path = "test.conf"
        try:
            config.new_config(path)
        except FileNotFoundError as e:
            print("file path {} is not exist".format(path))
        except Exception as e:
            raise e


if __name__ == '__main__':
    print("Current path is: {}".format(os.getcwd()))
    unittest.main()
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(unittest.makeSuite(MyTestCase))
    # runner = xmlrunner.XMLTestRunner(output='report')
    # runner.run(test_suite)
