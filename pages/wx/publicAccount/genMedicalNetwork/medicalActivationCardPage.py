from .medicalOrderPage import MedicalOrderCtrl


class MedicalActivationCardPage(MedicalOrderCtrl):
    """激活卡券页面"""

    @property
    def chineseMedicineTherapyCheckBoxElement(self):
        """中医理疗勾选框"""
        return self.By('chineseMedicineTherapyCheckBoxElement')

    @property
    def activationPageBackElement(self):
        """返回"""
        return self.By('activationPageBackElement')

    @property
    def immediatelyActiveElement(self):
        """立即激活"""
        return self.By('immediatelyActiveElement')

    @property
    def immediatelyActiveConfirmElement(self):
        """立即激活确认弹层确认按钮"""
        return self.By('immediatelyActiveConfirmElement')

    @property
    def immediatelyActiveCancelElement(self):
        """立即激活确认弹层取消按钮"""
        return self.By('immediatelyActiveCancelElement')

    @property
    def activeStatusMessage(self):
        """激活状态文案"""
        return self.By('activeStatusMessage').text

    @property
    def immediateUseElement(self):
        """立即使用"""
        return self.By('immediateUseElement')

    @property
    def continueActiveElement(self):
        """继续激活"""
        return self.By('continueActiveElement')


class MedicalActivationCardCtrl(MedicalActivationCardPage):
    """激活卡券页面控制层"""

    def activeChineseMedicineProduct(self):
        """激活一个中医理疗产品"""

        # 选择中医理疗产品
        self.chineseMedicineTherapyCheckBoxElement.click()

        # 点击立即激活
        self.immediatelyActiveElement.click()

        # 确认激活
        self.immediatelyActiveConfirmElement.click()