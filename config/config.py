#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/28 22:55

class Config:
    def __init__(self):
        pass

    # Parse the config.
    def parse(self):
        pass

    # Read configuration file from specified path.
    def read_file(self, path):
        try:
            f = open(path, 'r', 1, 'utf-8')  # 打开文件
            contents = f.read()
            print(contents)
        except IOError:
            return
        else:
            f.close()
