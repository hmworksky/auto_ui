import pytest
import allure
from ctrl.medicalCtrl import MedicalCtrl


@pytest.fixture(scope="module")
def medicalCtrl(driver, project):
    res = MedicalCtrl(driver, 'medicalElement')
    res.enterPublicAccount(project)
    return res


def teardown_function():
    """回到创医网首页"""

    # 每个用例执行完，稍微等待一会
    medicalCtrl().sleep(3)

    # 获取当前CONTEXT,如果不是NATIVE则切换会NATIVE并返回至公众号首页
    context = medicalCtrl().getContext
    if context != 'NATIVE_APP':
        medicalCtrl().backHomePage()


class TestMedical:
    """创医网测试用例"""

    @pytest.mark.smoke2
    def test_click_about_platform(self, medicalCtrl):
        """测试首页点击平台介绍有消息回复"""

        with allure.step("点击平台介绍"):
            medicalCtrl.clickAboutPlatform()

        with allure.step("查看公众号推送消息"):
            publicMessage = medicalCtrl.aboutPlatformLastMessageElement
            assert medicalCtrl.elementExists(publicMessage) == True

    @pytest.mark.smoke1
    def test_click_my_qr_code(self, medicalCtrl):
        """测试首页点击我的二维码有消息回复"""

        with allure.step("点击【我的二维码】"):
            medicalCtrl.clickMyQrCode()

        with allure.step("查看公众号推送消息"):
            medicalCtrl.sleep(3)
            publicMessage = medicalCtrl.qrCodeLastMessageElement
            assert medicalCtrl.elementExists(publicMessage) == True

    @pytest.mark.smoke
    def test_click_personal_center(self, medicalCtrl):
        """点击个人中心跳转创医网会员中心"""

        with allure.step("点击个人中心"):
            medicalCtrl.enterPersonalCenter()

        with allure.step("判断跳转【我的会员】是否成功"):
            # 判断是否有会员编号
            assert medicalCtrl.membershipNumber != ''

    @pytest.mark.smoke
    @pytest.mark.parametrize("itemType", ['insurance', 'card', 'deal', 'physical'])
    def test_buy_item(self, medicalCtrl, itemType):
        """测试购买四种不同类型商品"""
        try:
            with allure.step("购买一个商品"):
                medicalCtrl.info('当前购买{}类型产品'.format(itemType))
                medicalCtrl.buyItem(itemType)

            with allure.step("支付完成校验状态"):

                # 获取支付页面订单金额
                payPageOrderAmount = medicalCtrl.getFirstOrderAmount

                # 获取支付页面订单编号
                payPageOrderNumber = medicalCtrl.getFirstOrderNumber

                # 校验订单状态
                assert "已支付" in medicalCtrl.getFirstOrderStatus
                
            with allure.step("回到公众号首页"):
                medicalCtrl.backHomePage()
                orderDetail = medicalCtrl.getOrderDetail()
            with allure.step("校验订单号"):
                assert payPageOrderNumber == orderDetail['orderNumber']
            with allure.step("校验金额"):
                assert payPageOrderAmount == orderDetail['orderAmount']
        finally:
            with allure.step("返回公众号首页"):
                medicalCtrl.backHomePage()

    @pytest.mark.smoke5
    def test_card_product_confirm_goods(self, medicalCtrl):
        """卡类商品确认收货"""
        try:
            with allure.step("购买一个卡类产品"):
                medicalCtrl.buyItem('card')
            with allure.step("确认收货"):
                medicalCtrl.confirmGoods()
            with allure.step("再次刷新我的订单页面"):
                medicalCtrl.myOrderElement.click()
            with allure.step("第一笔订单应没有确认收货按钮"):
                assert medicalCtrl.elementExists(medicalCtrl.confirmGoodsButtonElement) == False
        finally:
            with allure.step("返回公众号首页"):
                medicalCtrl.backHomePage()

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_activation_card(self, medicalCtrl):
        """卡类产品激活使用"""
        try:
            with allure.step("购买一个卡类产品"):
                medicalCtrl.buyItem('card')
            with allure.step("激活使用"):
                medicalCtrl.activeCard()
            with allure.step("校验激活状态"):
                assert medicalCtrl.activeCtrl.activeStatusMessage == '恭喜您激活成功'
        finally:
            with allure.step("返回公众号首页"):
                medicalCtrl.backHomePage()


if __name__ == '__main__':
    pytest.main(['-s', 'test_medical.py', '-m', 'smoke5'])
