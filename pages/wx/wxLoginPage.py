from pages.basePage import BasePage


class WxLoginPage(BasePage):

    @property
    def loginElement(self):
        """登录"""
        return self.byId('com.tencent.mm:id/ecv')

    @property
    def telephoneInputElement(self):
        """手机号输入框"""
        return self.byId('com.tencent.mm:id/lh')

    @property
    def switchLoginTypeElement(self):
        """用微信号、QQ号、邮箱登录"""
        return self.byId('com.tencent.mm:id/cum')

    def inputUsername(self, username):
        """输入用户名"""
        self.usernameElement.send_keys(username)

    def inputPassword(self, password):
        """输入密码"""
        self.passwordElement.send_keys(password)

    def loginByUserPassword(self):
        """用户名密码登录"""
        self.loginButtonElement.click()

    @property
    def usernameElement(self):
        """账号输入框"""
        return self.byXpath("//android.widget.EditText[@text='请填写微信号']")

    @property
    def passwordElement(self):
        """密码输入框"""
        return self.byXpath("//android.widget.EditText[@text='请填写密码']")

    @property
    def telephoneLoginElement(self):
        """手机号登录"""
        return self.byId('com.tencent.mm:id/cum')

    @property
    def loginButtonElement(self):
        """登录按钮"""
        return self.byId('com.tencent.mm:id/cun')


if __name__ == '__main__':
    from common.baseDriver import BaseWebdriver
    driver = BaseWebdriver('sanxing_wx')
    m = WxLoginPage(driver)
    m.loginButtonElement()