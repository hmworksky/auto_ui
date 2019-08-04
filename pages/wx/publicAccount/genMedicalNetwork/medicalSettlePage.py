from pages.wx.publicAccount.genMedicalNetwork.medicalBuyPage import MedicalBuyCtrl


class MedicalSettlePage(MedicalBuyCtrl):
    """创医网结算页面"""

    @property
    def confirmSettleElement(self):
        """确认结算"""
        return self.By('confirmSettleElement')


class MedicalSettleCtrl(MedicalSettlePage):
    """创医网结算页面操作类"""

    def clickConfirmSettle(self):
        """点击确认结算"""
        return self.confirmSettleElement.click()

