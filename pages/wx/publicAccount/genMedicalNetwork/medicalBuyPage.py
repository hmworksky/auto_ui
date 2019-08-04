from pages.wx.publicAccount.genMedicalNetwork.medicalOnlineShopPage import MedicalOnlineShopCtrl


class MedicalBuyPage(MedicalOnlineShopCtrl):
    """购买页面"""

    def buyButtonElement(self):
        """购买按钮"""
        return self.By("buyButtonElement")

    @property
    def addCartElement(self):
        """加入购物车按钮"""
        return self.By('addCartElement')


class MedicalBuyCtrl(MedicalBuyPage):

    def clickBuyButton(self):
        """点击购买按钮"""
        self.info("点击购买按钮")
        return self.buyButtonElement().click()


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    from time import sleep
    from ctrl.wxCtrl import WxCtrl

    driver = BaseWebdriver('sanxing_wx')
    wx = WxCtrl(driver)
    sleep(3)
    wx.enterPublicAccount('MJLHKWB的接口测试号')

    home = MedicalBuyCtrl(driver)
    sleep(3)
    home.enterOnlineShop()
    print(driver.contexts)
    # 购买一个保险商品
    home.enterInsuranceItem()
    sleep(5)
    home.logger.info("###")
    home.clickBuyButton()
    home.logger.info("###2222")
    sleep(10)
    driver.quit()