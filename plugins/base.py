#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 15:35


class Base:
    """
    Base class of plugins backup data.
    It provides function 'exec' to start the data backup process.
    """

    def __init__(self):
        pass

    def exec(self):
        raise Exception("Base.exec is not initiate")
