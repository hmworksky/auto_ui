from pages.wx.publicAccount.genMedicalNetwork.medicalHomePage import MedicalHomePageCtrl


class MedicalOnlineShopPage(MedicalHomePageCtrl):
    """创医网在线商城首页"""

    @property
    def shopHomeElement(self):
        """首页按钮"""
        return self.By('shopHomeElement')

    @property
    def shoppingCartElement(self):
        """购物车"""
        return self.By('shoppingCartElement')

    @property
    def userCenterElement(self):
        """个人中心"""
        return self.By('userCenterElement')

    @property
    def myOrderElement(self):
        """我的订单"""
        return self.By('myOrderElement')

    @property
    def insuranceProductsElement(self):
        """保险类产品TAB"""
        return self.By('insuranceProductsElement')

    @property
    def cardServiceElement(self):
        """卡式服务"""
        return self.By('cardServiceElement')

    @property
    def dealsElement(self):
        """特惠产品"""
        return self.By('dealsElement')

    @property
    def physicalProductsElement(self):
        """实物产品"""
        return self.By('physicalProductsElement')

    @property
    def insuranceFirstItemElement(self):
        """保险类产品第一个商品"""
        return self.By('insuranceFirstItemElement')

    @property
    def cardFirstItemElement(self):
        """卡式服务第一个商品"""
        return self.By('cardFirstItemElement')

    @property
    def dealFirstItemElement(self):
        """特惠产品第一个商品"""
        return self.By('dealFirstItemElement')

    @property
    def physicalFirstItemElement(self):
        """实物产品第一个商品"""
        return self.By('physicalFirstItemElement')


class MedicalOnlineShopCtrl(MedicalOnlineShopPage):
    """商城首页操作层"""

    def buyItems(self, buyType='insurance'):
        """
        判断购买哪个产品
        insurance: 保险类
        card: 卡式服务
        deal: 特惠产品
        physical：实物产品
        """

        if buyType == 'insurance':
            self.enterInsuranceItem()
        elif buyType == 'card':
            self.enterCardItem()
        elif buyType == 'deal':
            self.enterDealItem()
        elif buyType == 'physical':
            self.enterPhysicalItem()

    def enterInsuranceItem(self):
        """点击进入保险类商品页面"""

        # 切换保险类商品TAB
        self.info("切换保险类商品TAB")
        self.insuranceProductsElement.click()

        # 点击第一个商品
        self.info("点击第一个商品")
        self.insuranceFirstItemElement.click()

    def enterCardItem(self):
        """点击进入卡式服务类商品页面"""

        # 切换卡式服务类商品TAB
        self.cardServiceElement.click()

        # 点击第一个商品，这里注意要切换WEBVIEW，识别完了需要切换回去
        self.switchContent('WEBVIEW_Terrace')
        self.cardFirstItemElement.click()

        # 这里注意要切换回WEBVIEW
        self.switchWxToolsWebview()

    def enterDealItem(self):
        """点击进入特惠产品类商品页面"""

        # 切换特惠产品类商品TAB
        self.dealsElement.click()

        # 点击第一个商品
        self.dealFirstItemElement.click()

    def enterPhysicalItem(self):
        """点击进入实物产品类商品页面"""

        # 切换实物产品类商品TAB
        self.physicalProductsElement.click()

        # 点击第一个商品
        self.physicalFirstItemElement.click()


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    from time import sleep
    from ctrl.wxCtrl import WxCtrl

    driver = BaseWebdriver('sanxing_wx')
    wx = WxCtrl(driver)
    sleep(3)
    wx.enterPublicAccount('MJLHKWB的接口测试号')

    home = MedicalOnlineShopCtrl(driver)
    sleep(3)
    home.enterOnlineShop()
    print(driver.contexts)
    # 购买一个保险商品
    home.enterInsuranceItem()
    driver.quit()
