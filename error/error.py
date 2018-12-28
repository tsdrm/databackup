#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 0:37


class Error:
    messageInfo = ""

    def __init__(self):
        pass

    def new(self, message):
        self.messageInfo = message
        return self

    def string(self):
        return "%(message)s" % {'message': self.messageInfo}

    def print(self):
        print("%s", self.messageInfo)
