#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/30 14:31
from datetime import datetime
import logging
import os

from plugins import base


class File(base.Base):
    """


    """

    def __init__(self, path, folder, export_name):
        base.Base.__init__(self)
        self.path = path
        self.folder = folder
        self.export_name = export_name
        if export_name == "":
            self.export_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") +".zip"

    def exec(self):
        name = os.path.join(self.folder, self.export_name)
        command = "zip -q -r {} {}".format(name, self.path)

        logging.info("file with command:{} will start ...".format(command))

        try:
            output = os.system(command)
            logging.info(output)
        except Exception as e:
            logging.error("file with command:{} crash".format(command), e)

        logging.info("file with command:{} successfully".format(command))
