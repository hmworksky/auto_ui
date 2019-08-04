from pages.basePage import BasePage


class WxHomePage(BasePage):

    @property
    def publicAccountElement(self):
        """通讯录公众号"""
        return self.byId('com.tencent.mm:id/a7y')

    @property
    def addressSearchElement(self):
        """通讯录搜索框"""
        return self.byXpath('//android.widget.ImageButton[@content-desc="搜索"]')

    @property
    def searchInputElement(self):
        """通讯录搜索框"""
        return self.byId('com.tencent.mm:id/lh')

    def choosePublicAccount(self, publicAccountName):
        """选择公众号"""
        self.byText(publicAccountName).click()

    def searchPublicAccount(self, publicAccountName):
        """进入公众号"""

        # 点击公众号
        self.info('点击公众号')
        self.publicAccountElement.click()

        # 搜索
        self.sleep(0.5)
        self.info('点击搜索')
        self.addressSearchElement.click()
        self.info('输入公众号:{}'.format(publicAccountName))
        self.searchInputElement.send_keys(publicAccountName)

        # 选择点击公众号
        self.info('选择点击公众号')
        self.choosePublicAccount(publicAccountName)

    def homeElement(self):
        """微信"""
        pass

    @property
    def addressBookElement(self):
        """通讯录"""
        return self.byText('通讯录')

    def enterAddressBook(self):
        """进入通讯录"""
        self.addressBookElement.click()

    @property
    def findElement(self):
        """发现"""
        return self.byText('发现')

    @property
    def littleProgramEntrance(self):
        """小程序入口"""
        return self.byText('小程序')

    def littleProgramChoice(self, name):
        """
        小程序列表
        :param name: 小程序名字
        :return:
        """


    @property
    def selfElement(self):
        """我"""
        return self.byXpath('//android.widget.RelativeLayout[4]/android.widget.LinearLayout')


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    driver = BaseWebdriver('sanxing_wx')
    m = WxHomePage(driver)
    m.sleep(5)
    print('等待？')
    m.findElement.click()