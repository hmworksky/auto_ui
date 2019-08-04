import os

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件目录
CONF_DIR = os.path.dirname(__file__)

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'log')

# appium server url
APPIUM_SERVER = 'http://localhost:4723/wd/hub'
