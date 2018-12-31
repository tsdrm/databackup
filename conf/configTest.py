import ast
import unittest

import os

from conf import config


class MyTestCase(unittest.TestCase):
    def test_config(self):
        # Read configuration file success.
        path = os.path.dirname(__file__) + '/test/user.conf'
        conf = config.new_config(path)
        conf.print()
        self.assertEqual(len(conf.info), 5)
        self.assertEqual(conf.info["key1"], 'key1')
        self.assertEqual(conf.info["key2"], '')
        self.assertEqual(conf.info["key3"], 'key3')
        self.assertEqual(conf.info["key4"], '"http://www.baidu.com"')
        self.assertEqual(conf.info["key5"], '{"a":"a", "b": "c", "c": 1}')

        key5_string = conf.info["key5"]
        my_dict = ast.literal_eval(key5_string)
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict["a"], "a")
        self.assertEqual(my_dict["b"], "c")
        self.assertEqual(my_dict["c"], 1)

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
