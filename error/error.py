#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 0:37


class Error:
    messageInfo = ""

    def __init__(self, message):
        self.messageInfo = message

    def string(self):
        return "%(message)s" % {'message': self.messageInfo}

    def print(self):
        print(self.messageInfo)


def new(message):
    if not isinstance(message, str):
        raise TypeError('%s must be str' % message)
    return Error(message)
