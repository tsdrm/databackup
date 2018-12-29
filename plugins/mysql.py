#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 14:10
import logging


# import pymysql

from datetime import datetime

import os


class Mysql:
    """
    Plugin implement function to backup from mysql.

    addr: Database ip-addr or domain name.
    port: Database port.
    username: Which user you want to connect to database.
    password: The password with username to connect to database.
    db_name: Which database you want to connect, it's specified database name.
    """

    addr = ""
    port = ""
    username = ""
    password = ""
    db_name = ""

    # db = None

    def __init__(self, addr, port, username, password, db_name):
        self.addr = addr
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

    # def connect_database(self):
    #     """
    #     It will start connecting database if be called.
    #
    #     :return: None
    #     """
    #
    #     logging.info("database mysql will start connecting with addr:{}, username:{}, db_name:{}, port:{}".format(
    #         self.addr, self.username, self.db_name, self.port))
    #     try:
    #         self.db = pymysql.connect(self.addr, self.username, self.password, self.db_name, self.port)
    #     except Exception as e:
    #         logging.critical("database mysql connect with addr:{}, username:{}, db_name:{}, port:{}".format(
    #             self.addr, self.username, self.db_name, self.port
    #         ), e)
    #         raise e
    #
    #     try:
    #         self.db.ping()
    #     except Exception as e:
    #         logging.critical("database mysql connect success but ping crash", e)
    #         raise e
    #
    # def close(self):
    #     if self.db is not None:
    #         try:
    #             self.db.close()
    #         except Exception as e:
    #             pass
    #     else:
    #         raise Exception("database mysql with addr:{}, username:{}, db_name:{}, port:{} already closed".format(
    #             self.addr, self.username, self.db_name, self.port))

    def export(self):
        """
        It export data in mysql server to specified file if be called.

        :return: str. It represents a file path if export execute successfully
        """

        name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        command = "mysqldump -u {} -p {} --host={} --port={} -B {} > {}".format(self.username, self.password, self.addr, self.port, self.db_name, name)
        logging.info("mysqldump with addr:{}, username:{}, db_name:{}, port:{} will start...".format(self.addr, self.username, self.db_name, self.port))
        try:
            output = os.system(command)
            logging.info(output)
        except Exception as e:
            logging.error("mysqldump with addr:{}, username:{}, db_name:{}, port:{}".format(self.addr, self.username, self.db_name, self.port), e)
            raise e

        logging.info("mysqldump with addr:{}, username:{}, db_name:{}, port:{} successfully...".format(self.addr, self.username, self.db_name, self.port))

    def exec(self):
        self.export()
