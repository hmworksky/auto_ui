from appium import webdriver
import threading
from conf.settings import APPIUM_SERVER
from common.tools import load_yaml


class BaseWebdriver:
    _instance_lock = threading.Lock()

    def __new__(cls, desired, *args, **kwargs):
        if not hasattr(BaseWebdriver, "_instance"):
            with BaseWebdriver._instance_lock:
                if not hasattr(BaseWebdriver, "_instance"):
                    BaseWebdriver._instance = object.__new__(cls)
        desc = cls.getConf('device').get(desired)
        return webdriver.Remote(APPIUM_SERVER, desc)

    @staticmethod
    def getConf(confName):
        """获取项目配置"""
        return load_yaml(confName)