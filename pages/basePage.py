import os
from common.logger import Logger
from common.tools import load_yaml
from traceback import extract_stack
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(Logger):

    def __init__(self, driver, project=None):
        self.project = project
        self.driver = driver
        super().__init__(project)

    def By(self, name, more=False, timeout=3):
        """定位元素,more:查找多个，timeout:默认等待3秒"""

        # 获取函数调用栈
        func = extract_stack()[-2]

        # 获取函数名
        func_name = func[2]

        # 获取文件名
        class_name = os.path.splitext(os.path.basename(func[0]))[0]

        # 获取定位信息
        obj = load_yaml('element/{}'.format(self.project))
        find_data = obj.get(class_name).get(func_name)

        # 打印日志
        class_memo = obj.get(class_name).get('memo')
        func_memo = find_data.get('memo')
        format_str = "【{}】页面，【{}】元素".format(class_memo, func_memo)
        self.info("当前开始定位：{}".format(format_str))
        try:
            return self.findByObj(find_data, more, timeout)
        except NoSuchElementException:
            self.error("未定位到该元素，请检查配置：{}".format(format_str))
            return False
        except TimeoutException:
            self.critical("定位元素超时！！！：{}".format(format_str))
            return False

    def wait(self, element, timeout=3):
        """等待元素出现"""
        WebDriverWait(self.driver, timeout=timeout).until(lambda driver: driver.find_element_by_xpath(element))

    def findByObj(self, obj, more, timeout=3):
        """根据不同类型选择不同定位方式"""

        method = obj.get('type', 'xpath')
        value = obj.get('value')

        if method == 'xpath':
            self.wait(value, timeout)
            return self.byXpath(value, more)
        elif method == 'id':
            return self.byId(value, more)
        elif method == 'text':
            return self.byText(value, more)

    @staticmethod
    def getAttr(element, attr='text'):
        """获取定位对象的attr属性"""
        if attr == 'text':
            return element.text
        return element.get_attribute(attr)

    def byText(self, element, more=False, contains=False):
        """text定位,more:定位多个,contains模糊匹配"""
        if not contains:
            element = "//android.widget.TextView[@text='{}']".format(element)
        else:
            element = "//android.widget.TextView[contains(@text,'{}')]".format(element)
        if more:
            return self.driver.find_elements_by_xpath(element)

        return self.byXpath(element)

    def byXpath(self, element, more=False):
        """Xpath定位,more:定位多个"""
        if more:
            self.info(element)
            return self.driver.find_elements_by_xpath(element)
        return self.driver.find_element_by_xpath(element)

    def byCss(self, element, more=False):
        """Css定位,more:定位多个"""
        if more:
            return self.driver.find_elements_by_css_selector(element)
        return self.driver.find_element_by_css_selector(element)

    def byId(self, element, more=False):
        """Id定位,more:定位多个"""
        if more:
            return self.driver.find_elements_by_xpath(element)
        return self.driver.find_element_by_id(element)

    def switchContent(self, webview):
        """切换NATIVE及WEBVIEW"""
        self.driver.switch_to.context(webview)

    @property
    def getContext(self):
        """获取当前Context"""
        return self.driver.current_context

    @property
    def getAllContext(self):
        """获取当前所有Context"""
        return self.driver.contexts

    def getSize(self):
        """获取屏幕大小"""
        # size = self.driver.get_window_size()
        x = 1080
        y = 1980
        return x, y

    def swipeUp(self):
        """向上滑动"""
        width, height = self.getSize()
        self.driver.swipe(width / 2, height * 4 / 5, width / 2, height / 5, 500)

    def swipeDown(self):
        """向下滑动"""
        width, height = self.getSize()
        self.driver.swipe(width / 2, height / 4, width / 2, height * 4 / 5, 500)

    def swipeLeft(self):
        """向左滑动"""
        width, height = self.getSize()
        self.driver.swipe(width / 5, height / 2, width * 4 / 5, height / 2, 500)

    def swipeRight(self):
        """向右滑动"""
        width, height = self.getSize()
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def switch_app(self):
        """切换NATIVE_APP"""
        if self.getContext != 'NATIVE_APP':
            self.driver.switch_to.context('NATIVE_APP')

    @staticmethod
    def elementExists(element):
        if element:
            return True
        return False

    def switchWxToolsWebview(self):
        """切换微信ToolsWEBVIEW"""
        self.info('开始切换WEBVIEW')
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
        self.info('切换至{}WEBVIEW成功'.format(self.getContext))

    @staticmethod
    def enter(element):
        """点击某个对象"""
        element.click()

    def sleep(self, num):
        from time import sleep
        sleep(num)


