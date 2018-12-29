#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/28 22:55


class Config:
    __lines = []  # Multi lines read from configuration file.
    info = {}  # Dictionary contain the configuration information after __lines were dealt.
    __path = ""  # Just record the configuration file path given.

    def __init__(self, path):
        self.__path = path
        self.read_file(self.__path)

    def parse(self):
        """
        Parse the config.

        :return:
        """
        for line in self.__lines:
            line = line.strip()
            # It's comment if line start with '#', '='.
            if line.startswith('#') or line.startswith('='):
                continue

            # It's unexpected line if not contain '='.
            if line.find('=') == -1:
                continue


            # Put configuration information in form key-value into filed 'info'.
            line_contents = line.split("=")
            if len(line_contents) == 1:
                self.info[line_contents[0]] = ""
            if len(line_contents) == 2:
                self.info[line_contents[0]] = line_contents[1]


    def read_file(self, path):
        """
        Read configuration file from specified path line by line.

        :param path:
        :return:
        """
        try:
            f = open(path, 'r', 1, 'utf-8')  # 打开文件
            self.__lines = f.readlines()
        except IOError as e:
            raise e
        else:
            f.close()

    def print(self):
        for key in self.info:
            print("{}: {}".format(key, self.info[key]))


def new_config(path):
    """
    Make a config dictionary which contain the config info via path.

    :param path: Given file path of configuration file.
    :return: The map incorporate the config info.
    """
    config = Config(path)
    config.parse()
    return config

