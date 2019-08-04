from pages.basePage import BasePage


class MedicalOrderPage(BasePage):
    """我的订单"""

    @property
    def firstOrderStatusElement(self):
        """最新订单的订单状态"""
        return self.By('firstOrderStatusElement')

    @property
    def firstOrderAmountElement(self):
        """最新订单的订单金额"""
        return self.By('firstOrderAmountElement')

    @property
    def firstOrderNumberElement(self):
        """最新订单的订单编号"""
        return self.By('firstOrderNumberElement')

    @property
    def toUseCardElement(self):
        """卡类产品去使用按钮"""
        return self.By('toUseCardElement')

    @property
    def toActivateTheUseButtonElement(self):
        """去激活使用按钮"""
        return self.By('toActivateTheUseButtonElement')

    @property
    def giveOthersElement(self):
        """赠送他人按钮"""
        return self.By('giveOthersElement')

    @property
    def orderBackButtonElement(self):
        """订单详情返回按钮"""
        return self.By('orderBackButtonElement')

    @property
    def deliveryStatus(self):
        """订单详情发货状态"""
        return self.By('deliveryStatus').text

    @property
    def activeConfirmButtonElement(self):
        """确认激活弹层【确认】按钮"""
        return self.By('activeConfirmButtonElement')

    @property
    def activeCancelButtonElement(self):
        """确认激活弹层【取消】按钮"""
        return self.By('activeCancelButtonElement')

    @property
    def confirmGoodsButtonElement(self):
        """确认收货按钮"""
        return self.By('confirmGoodsButtonElement')

    @property
    def confirmGoodsConfirmElement(self):
        """确认收货确认按钮"""
        return self.By('confirmGoodsConfirmElement')


class MedicalOrderCtrl(MedicalOrderPage):
    """我的订单操作类"""

    @property
    def getFirstOrderNumber(self):
        """我的订单最新一笔订单订单状态"""
        return self.getAttr(self.firstOrderNumberElement)

    @property
    def getFirstOrderStatus(self):
        """我的订单最新一笔订单订单状态"""
        return self.getAttr(self.firstOrderStatusElement)

    @property
    def getFirstOrderAmount(self):
        """我的订单最新一笔订单订单状态"""
        return self.getAttr(self.firstOrderAmountElement)

    def confirmGoods(self):
        """确认收货"""
        self.confirmGoodsButtonElement.click()
        self.confirmGoodsConfirmElement.click()

    def jumpCardActivePage(self):
        """跳转卡类产品激活页面"""

        # 订单页面点击【去使用】按钮
        self.toUseCardElement.click()

        # 点击去激活使用
        self.toActivateTheUseButtonElement.click()

        # 弹层点击确认
        self.activeConfirmButtonElement.click()