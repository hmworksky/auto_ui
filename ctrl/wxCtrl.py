from pages.wx.wxLoginPage import WxLoginPage
from pages.wx.wxHomePage import WxHomePage


class WxCtrl(WxLoginPage, WxHomePage):

    def login(self, username, password):
        """微信登录"""

        # 点击登录
        self.loginElement.click()

        # 切换微信号、QQ号登录
        self.switchLoginTypeElement.click()

        # 输入账号密码
        self.inputUsername(username)
        self.inputPassword(password)

        # 点击登录
        self.loginByUserPassword()

    def enterLittleProgram(self, name):
        """
        进入小程序
        :param name: 小程序名字
        :return:
        """
        # 点击发现
        self.sleep(3)
        self.findElement.click()

    def enterPublicAccount(self, publicAccountName):
        """进入公众号"""

        self.info('进入公众号流程开始')

        self.sleep(3)
        # 点击通讯录
        self.info('点击通讯录')
        self.enterAddressBook()

        # 点击搜索进入公众号
        self.sleep(3)
        self.searchPublicAccount(publicAccountName)


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    driver = BaseWebdriver('sanxing_wx')
    wx = WxCtrl(driver)
    wx.enterPublicAccount('MJLHKWB的接口测试号')
