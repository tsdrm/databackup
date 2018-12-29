#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 15:55

import logging


class Logger:
    logger = None

    __level_debug = 0
    __level_info = 1
    __level_warning = 2
    __level_error = 3
    __level_critical = 4

    def __init__(self):
        self.logger = logging.getLogger()

    def set_level(self, level):
        if not isinstance(level, int):
            raise Exception("level({}) is not int".format(level))
        if level < 0 or level > 4:
            raise Exception("unexpected level, please set between 0~4")
        self.logger.level = level

    def log_to_file(self, path):
        # self.logger.addHandler()
        logging.basicConfig()

    def debug(self, message):
        pass

    def info(self, message):
        pass

    def warning(self, message):
        pass

    def error(self, message):
        pass

    def critical(self, message):
        pass
