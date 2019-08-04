from .medicalConfirmSettlePage import MedicalConfirmSettleCtrl


class MedicalPayPage(MedicalConfirmSettleCtrl):
    """创医网支付信息页面"""

    @property
    def orderNo(self):
        """订单编号"""
        return self.By('orderNo').text

    @property
    def payIntegral(self):
        """支付积分"""
        return self.By('payIntegral').text

    @property
    def eWalletAvailableBalance(self):
        """电子钱包可用余额"""
        return self.By('eWalletAvailableBalance').text

    @property
    def bonusAvailableBalance(self):
        """奖金钱包余额"""
        return self.By('bonusAvailableBalance').text

    @property
    def orderAmount(self):
        """订单金额"""
        return self.By('orderAmountElement').text

    @property
    def confirmPayElement(self):
        """确认支付按钮"""
        return self.By('confirmPayElement')

    @property
    def backPayElement(self):
        """返回按钮"""
        return self.By('backPayElement')

    @property
    def paymentConfirmationLayerConfirmElement(self):
        """点击确认支付后到支付弹层确认按钮"""
        return self.By('paymentConfirmationLayerConfirmElement')

    @property
    def paymentConfirmationLayerCancelElement(self):
        """点击确认支付后到支付弹层取消按钮"""
        return self.By('paymentConfirmationLayerCancelElement')


class MedicalPayCtrl(MedicalPayPage):
    """支付信息页面操作类"""

    def confirmPay(self, operation='confirm'):
        """点击确认支付"""
        self.info("点击确认支付")
        self.confirmPayElement.click()

        # 弹层确认或取消
        if operation == 'confirm':
            self.info("支付弹层点击确认")
            self.paymentConfirmationLayerConfirmElement.click()
        else:
            self.info("支付弹层点击取消")
            self.paymentConfirmationLayerCancelElement.click()

    def backPay(self):
        """返回不支付"""
        self.info("点击返回按钮不支付")
        self.backPayElement.click()