#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/29 14:10

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


    def __init__(self, addr, port, username, password, db_name):
        self.addr = addr
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name


    def connect_database(self):
        """
        It will start connecting database if be called.

        :return: bool. true: Connect database successfully, otherwise, it's failed.
        """
        return 1

    def export(self):
        """
        It export data in mysql server to specified file if be called.

        :return: str. It represents a file path if export execute successfully
        """
        pass

    def exec(self):
        status = self.connect_database()
        if not status:
            pass

        self.export()