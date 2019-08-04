import os
import yaml
from conf.settings import CONF_DIR
from traceback import extract_stack


def load_yaml(filename):
    """get yaml object"""
    # 格式化文件名
    filename = filename if filename.endswith('.yaml') else "{}.yaml".format(filename)
    file_path = os.path.join(CONF_DIR, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
        obj = yaml.load(data, Loader=yaml.Loader)
        return obj


if __name__ == '__main__':
    import re
