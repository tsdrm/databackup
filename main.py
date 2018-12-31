#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tangs
# datetime:2018/12/28 22:09

import logging
import os
import ast
from plugins import mysql
from plugins import file
from datetime import datetime


def package(folder, file_name, mysql_name):
    temp_folder = os.path.join(folder, datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    zip_name = temp_folder + ".zip"

    try:
        command = "mkdir {}".format(temp_folder)
        output = os.system(command)
        logging.info("package exec command: {} output:{}".format(command, output))

        command = "cp -rf {} {} {}".format(file_name, mysql_name, temp_folder)
        output = os.system(command)
        logging.info("package exec command: {} output:{}".format(command, output))

        command = "zip -r {} {}".format(zip_name, temp_folder)
        logging.info("package exec command: {} output:{}".format(command, output))

    except OSError as e:
        logging.error("package with temp_folder:{}, file_name:{}, mysql_name:{} error".format(
            temp_folder, file_name, mysql_name), e)
        return zip_name

    return zip_name


def exec_plugin(config):
    if not isinstance(config, dict):
        raise Exception("config is not dict", dict)

    users = config.get("users", {})
    if len(users) == 0:
        logging.info("users is empty, process will return")
        return True

    export_folder = config.get("export_folder")

    for user in users:
        user_config = users[user]
        if not isinstance(user_config, dict):
            logging.error("user({}) config is not dict".format(user))
            raise Exception("user({}) config is not dict".format(user), users[user])

        # The user doesn't backup if field export letter than 1.
        if user_config["export"] < 1:
            continue

        mysql_final_name = ""
        file_final_name = ""
        if "mysql" in user_config.keys():
            mysql_config = user_config["mysql"]
            if not isinstance(mysql_config, dict):
                logging.error("mysql_config with user({}) is not dict".format(user), user_config["mysql"])
                raise Exception("mysql_config with user({}) is not dict".format(user), user_config["mysql"])

            extra_file = mysql_config.get("extra_file")
            db_name = mysql_config.get("db_name")
            mysql_export_name = mysql_config.get("export_name")
            if extra_file != "" or db_name != "":
                mysql_plugin = mysql.Mysql("", "", "", "", db_name=db_name, extra_file=extra_file, folder=export_folder,
                                           export_name=mysql_export_name)
                mysql_final_name = mysql_plugin.exec()
                if mysql_final_name == "-1":
                    logging.error("mysql plugin exec with user({}) failed".format(user))
                    continue

        if "file" in user_config.keys():
            file_config = user_config["file"]
            if not isinstance(file_config, dict):
                logging.error("file_config with user({}) is not dict".format(user), user_config["file"])
                raise Exception("file_config with user({}) is not dict".format(user), user_config["file"])

            file_path = file_config.get("path")
            file_export_name = file_config.get("export_name")
            if file_path != "":
                file_plugin = file.File(file_path, export_folder, file_export_name)
                file_final_name = file_plugin.exec()
                if file_final_name == "-1":
                    logging.error("file plugin exec with user({}) failed".format(user))
                    continue

        return package(export_folder, file_final_name, mysql_final_name)


if "__main__" == __name__:

    # Read config.json
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        f = open(config_path, mode="r", encoding="utf-8")
        config_str = f.read()
        f.close()
    except Exception as e:
        raise e

    config_dict = ast.literal_eval(config_str)
    log_file = config_dict.get("log_file", "/var/log/data_backup.log")

    logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        level=logging.DEBUG,
                        filename=log_file,
                        filemode="/var/log/data_backup")

    logging.info("data backup will start ...")

    is_success = exec_plugin(config_dict)
    if not is_success:
        logging.error("data package failed")
    else:
        logging.info("data package successfully")
