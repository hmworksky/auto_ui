from pages.wx.publicAccount.genMedicalNetwork.medicalPayPage import MedicalPayCtrl
from pages.wx.publicAccount.genMedicalNetwork.medicalOrderPage import MedicalOrderCtrl
from pages.wx.publicAccount.genMedicalNetwork.medicalUserCenterPage import MedicalUserCenterCtrl
from pages.wx.publicAccount.genMedicalNetwork.medicalActivationCardPage import MedicalActivationCardCtrl
from ctrl.wxCtrl import WxCtrl


class MedicalCtrl(MedicalPayCtrl, WxCtrl, MedicalOrderCtrl, MedicalUserCenterCtrl):

    def __init__(self, driver, project):
        super().__init__(driver, project)
        self.activeCtrl = MedicalActivationCardCtrl(self.driver)

    def activeCard(self):
        """激活一个卡商品"""

        # 先买一个卡商品
        self.buyItem()

        # 跳转激活卡商品
        self.jumpCardActivePage()

        # 激活卡商品
        self.activeCtrl.activeChineseMedicineProduct()

    def buyItem(self, buyType='insurance'):
        """创医网购买一个产品"""

        # 进入商城
        self.sleep(3)
        self.info("进入商城")
        self.enterOnlineShop()

        # 购买一个商品
        self.info('进入选择商品流程')
        self.buyItems(buyType)

        # 点击购买，如果是卡类商品需要页面向下滑动
        self.info("点击购买")
        if buyType == 'card':
            self.swipeUp()
        self.clickBuyButton()

        # 确认结算
        self.sleep(3)
        self.info("确认结算")
        self.clickConfirmSettle()

        # 填写收获信息并提交订单
        self.sleep(3)
        self.info("使用已经存在的收获地址提交订单")
        self.useAlreadyExistsAddressOrder(buyType)

        # 确认支付
        self.info("确认支付")
        self.confirmPay()


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    import re
    drivers = BaseWebdriver('sanxing_wx')
    home = MedicalCtrl(drivers, 'medicalElement')
    try:
        home.enterPublicAccount('MJLHKWB的接口测试号')
        home.sleep(3)
        data = home.orderLastMessageElement.text
        home.info(data)
        orderNo = re.findall(r'支付单号：(.*)\n支付时间', data)[0]
        amount = re.findall(r'支付金额：(.*)\n支付方式', data)[0]
        home.info(orderNo)
        home.info(amount)
        # home.buyItem('card')
    finally:
        driver.quit()
