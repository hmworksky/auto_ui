import re
from pages.basePage import BasePage


class MedicalHomePage(BasePage):
    """创医网公众号首页"""

    @property
    def homePageMessage(self):
        """主页消息列表"""
        res = self.byId('com.tencent.mm:id/ae').find_elements_by_class_name('android.widget.RelativeLayout')
        self.info('message_list:{}'.format(res))
        self.info('message_list_length:{}'.format(len(res)))
        return res

    @property
    def systemBackMessageElement(self):
        """用户输入后系统回复消息"""
        return self.By('systemBackMessageElement')

    @property
    def aboutPlatformLastMessageElement(self):
        """系统回复的平台介绍最后一条消息"""
        return self.By('aboutPlatformLastMessageElement')

    @property
    def orderLastMessageElement(self):
        """系统回复的最后一条下单信息"""
        return self.By('orderLastMessageElement')

    @property
    def qrCodeLastMessageElement(self):
        """系统回复的最后一条二维码信息"""
        return self.By('qrCodeLastMessageElement')

    @property
    def topCloseElement(self):
        """顶部左上关闭X按钮"""
        return self.By('topCloseElement')

    @property
    def threePointElement(self):
        """右上角微信点点点"""
        return self.byId('com.tencent.mm:id/kz')

    @property
    def inputKeyboardElement(self):
        """输入键盘"""
        return self.By('inputKeyboardElement')

    @property
    def textInputElement(self):
        """消息输入框"""
        return self.By('textInputElement')

    @property
    def sendButtonElement(self):
        """发送按钮"""
        return self.By('sendButtonElement')

    @property
    def aboutNetworkElement(self):
        """关于创医网"""
        return self.byText("关于创医网")

    @property
    def platformIntroduceElement(self):
        """平台介绍"""
        return self.byText("平台介绍")

    @property
    def onlineShopElement(self):
        """在线商城"""
        return self.By("onlineShopElement")

    @property
    def mineElement(self):
        """我的"""
        return self.By('mineElement')

    @property
    def myQrCodeElement(self):
        """我的二维码"""
        return self.By('myQrCodeElement')

    @property
    def personalCenterElement(self):
        """个人中心"""
        return self.By('personalCenterElement')


class MedicalHomePageCtrl(MedicalHomePage):

    def backHomePage(self):
        """返回项目主页"""
        if self.getContext != 'NATIVE_APP':
            # 切换至NATIVE
            self.switch_app()

            # 返回公众号首页
            self.topCloseElement.click()

    def getLastMessage(self):
        """获取聊天信息数量"""
        return len(self.homePageMessage)

    def enterOnlineShop(self):
        """进入在线商城"""

        self.onlineShopElement.click()

        # 切换WEBVIEW
        self.switchWxToolsWebview()

    def clickMyQrCode(self):
        """点击【我的二维码】生成二维码"""
        self.mineElement.click()
        self.myQrCodeElement.click()

    def enterPersonalCenter(self):
        """进入个人中心"""
        self.mineElement.click()
        self.personalCenterElement.click()

        # 切换WEBVIEW
        self.switchWxToolsWebview()

    def clickAboutPlatform(self):
        """点击平台介绍介绍"""
        self.sleep(3)
        self.aboutNetworkElement.click()
        self.platformIntroduceElement.click()

    def getOrderDetail(self):
        """获取系统最后一条订单信息"""
        detail = {}
        res = self.orderLastMessageElement.text
        orderNumber = re.findall(r'支付单号：(.*)\n支付时间', res)[0]
        orderAmount = re.findall(r'支付金额：(.*)\n支付方式', res)[0]
        detail['orderNumber'] = orderNumber
        detail['orderAmount'] = orderAmount
        return detail

    def inputQuery(self, msg):
        """公众号中输入文本查询"""

        # 开启输入
        self.inputKeyboardElement.click()

        # 发送消息
        self.textInputElement.send_keys(msg)
        self.sendButtonElement.click()


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    from time import sleep
    from ctrl.wxCtrl import WxCtrl

    driver = BaseWebdriver('sanxing_wx')
    wx = WxCtrl(driver)
    sleep(3)
    wx.enterPublicAccount('MJLHKWB的接口测试号')

    home = MedicalHomePageCtrl(driver, 'medicalElement')
    sleep(3)
    home.getMessageLength()
    sleep(10)

    driver.quit()