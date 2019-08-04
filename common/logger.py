import logging
import os.path
import time
from colorama import Fore, Style
from conf.settings import LOG_PATH


class Logger(object):
    def __init__(self, logger='default'):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        :param logger:  定义对应的程序模块名name，默认为root
        """

        # 创建一个logger
        self.logger = logging.getLogger(name=logger)
        self.logger.setLevel(logging.INFO)  # 指定最低的日志级别 critical > error > warning > info > debug

        # 创建一个handler，用于写入日志文件
        rq = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        log_name = LOG_PATH + '/' + rq + ".log"

        console_handler = logging.StreamHandler()  # 日志输出到屏幕控制台
        console_handler.setLevel(logging.INFO)  # 设置日志等级

        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_name, encoding='utf-8')
            file_handler.setLevel(logging.WARNING)

            formatter = logging.Formatter("%(asctime)s %(name)s- %(levelname)s - %(message)s")
            # %(asctime)s	字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
            # %(name)s 自定义的模块名

            console_handler.setFormatter(formatter)  # 选择一个输出格式，可以定义多个输出格式
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)  # 增加指定的handler
            self.logger.addHandler(console_handler)

    def debug(self, msg):
        """
        定义输出的颜色debug--white，info--green，warning/error/critical--red
        :param msg: 输出的log文字
        :return:
        """
        self.logger.debug(Fore.WHITE + "DEBUG - " + str(msg) + Style.RESET_ALL)

    def info(self, msg):
        self.logger.info(Fore.GREEN + "INFO - " + str(msg) + Style.RESET_ALL)

    def warning(self, msg):
        self.logger.warning(Fore.YELLOW + "WARNING - " + str(msg) + Style.RESET_ALL)

    def error(self, msg):
        self.logger.error(Fore.RED + "ERROR - " + str(msg) + Style.RESET_ALL)

    def critical(self, msg):
        self.logger.critical(Fore.RED + "CRITICAL - " + str(msg) + Style.RESET_ALL)


if __name__ == '__main__':
    log = Logger(logger="test")
    log.debug("debug")
    log.info("info")
    log.error("error")
    log.warning("warning")
    log.critical("critical")