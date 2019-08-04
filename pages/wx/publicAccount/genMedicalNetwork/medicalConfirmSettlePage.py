from .medicalSettlePage import MedicalSettleCtrl


class MedicalConfirmSettlePage(MedicalSettleCtrl):
    """创医网确认结算收获地址页面"""

    @property
    def consigneeNameElement(self):
        """收货人姓名"""
        return self.By('consigneeNameElement')

    @property
    def consigneePhoneElement(self):
        """收货人手机"""
        return self.By('consigneePhoneElement')

    @property
    def consigneeAddressSelectorElement(self):
        """请选择收获地址下拉框"""
        return self.By('consigneeAddressSelectorElement')

    @property
    def consigneeAddressConfirmElement(self):
        """收获地址弹层确认按钮"""
        return self.By('consigneeAddressConfirmElement')

    @property
    def consigneeAddressInputElement(self):
        """收获地址输入框"""
        return self.By('consigneeAddressInputElement')

    @property
    def consigneeBackFixOrderElement(self):
        """返回修改商品按钮"""
        return self.By('consigneeBackFixOrderElement')

    def consigneeSubmitOrderElement(self, buyType=None):
        """提交订单按钮"""
        cardFlag = 3 if buyType == 'card' else 4
        element = '//*[@id="poShipForm"]/div[{}]/div/div/div[2]/button'.format(cardFlag)
        return self.byXpath(element)


class MedicalConfirmSettleCtrl(MedicalConfirmSettlePage):
    """创医网确认结算页面操作类"""

    def useNewAddressConfirmOrder(self, name='default', phone=13830000001, address='test', isCard=False):
        """
        使用新收获地址提交订单
        :param name: 收货人姓名
        :param phone: 收货人手机号
        :param address: 收货人地址
        :param isCard: 是否是卡类商品，卡类商品提交订单定位与其它不一致
        :return:
        """

        # 输入收货人姓名
        self.info('输入收货人姓名：{}'.format(name))
        self.consigneeNameElement.send_keys(name)

        # 输入收货人手机
        self.info('输入收货人手机：{}'.format(phone))
        self.consigneePhoneElement.send_keys(phone)

        # 选择收获地区
        self.info('选择默认收获地区')
        self.consigneeAddressSelectorElement.click()
        self.consigneeAddressConfirmElement.click()

        # 输入收货人地址
        self.info('输入收货人地址：{}'.format(address))
        self.consigneeAddressInputElement.send_keys(address)

        # 继续走已经存在地址的流程
        self.useAlreadyExistsAddressOrder(isCard)

    def useAlreadyExistsAddressOrder(self, buyType=None):
        """使用默认地址提交订单"""

        # 提交订单前页面滑动到底部
        self.info('提交订单前页面滑动到底部')
        self.swipeUp()
        self.sleep(2)

        # 提交订单
        self.info('提交订单')
        self.consigneeSubmitOrderElement(buyType).click()