from pages.basePage import BasePage


class MedicalUserCenterPage(BasePage):
    """会员中心页面"""

    @property
    def personImage(self):
        """个人头像地址"""
        return self.getAttr(self.By('personImage'), 'src')

    @property
    def userName(self):
        """用户名"""
        return self.getAttr(self.By('userName'))

    @property
    def membershipNumber(self):
        """会员编号"""
        return self.getAttr(self.By('membershipNumber'))

    @property
    def telephoneNumber(self):
        """手机号码"""
        return self.getAttr(self.By('telephoneNumber'))

    @property
    def inviteFriendsQrCodeElement(self):
        """邀请好友二维码"""
        return self.By('inviteFriendsQrCodeElement')

    @property
    def inviteQrCodeText(self):
        """二维码下方文案"""
        return self.getAttr(self.By('inviteQrCodeText'))

    @property
    def settingElement(self):
        """设置"""
        return self.By('settingElement')

    @property
    def accountDetailElement(self):
        """账户详情"""
        return self.By('accountDetailElement')

    @property
    def memberElement(self):
        """我的会员"""
        return self.By('memberElement')

    @property
    def forPaymentElement(self):
        """待付款"""
        return self.By('forPaymentElement')

    @property
    def sendGoodsElement(self):
        """待发货"""
        return self.By('sendGoodsElement')

    @property
    def allOrdersElement(self):
        """全部订单"""
        return self.By('allOrdersElement')

    @property
    def onlineRechargeElement(self):
        """在线充值"""
        return self.By('onlineRechargeElement')

    @property
    def offlineRemittanceElement(self):
        """线下汇款"""
        return self.By('offlineRemittanceElement')

    @property
    def applyForJoiningElement(self):
        """申请加盟"""
        return self.By('applyForJoiningElement')

    @property
    def announcementElement(self):
        """公告"""
        return self.By('announcementElement')


class MedicalUserCenterCtrl(MedicalUserCenterPage):
    """会员中心操作控制层"""

    def enterSetting(self):
        """进入设置页面"""
        self.settingElement.click()

    def enterAccountDetail(self):
        """进入账户详情"""
        self.accountDetailElement.click()

    def enterMember(self):
        """进入我的会员"""
        self.memberElement.click()

    def enterForPayment(self):
        """进入待付款页面"""
        self.forPaymentElement.click()

    def enterSendGood(self):
        """进入发货页面"""
        self.sendGoodsElement.click()

    def enterAllOrder(self):
        """进入全部订单"""
        self.allOrdersElement.click()

    def enterOnlineRecharge(self):
        """进入在线充值"""
        self.onlineRechargeElement.click()

    def enterOfflineRemittance(self):
        """进入线下汇款"""
        self.offlineRemittanceElement.click()

    def enterApplyForJoining(self):
        """进入申请加盟"""
        self.applyForJoiningElement.click()

    def enterAnnouncement(self):
        """进入公告"""
        self.announcementElement.click()