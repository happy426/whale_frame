import time

import allure
import pytest
from playwright.sync_api import Browser
from common.robot_image import SendMsg


class TestAlivia:

    @pytest.fixture(autouse=False)
    def setup(self, browser: Browser):
        self.browser = browser
        self.page = self.browser.new_page(locale="zh-CN")
        self.page.goto("https://whale-login.stage.meetwhale.com/login")
        self.page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[1]/div/span/input', "18709873932")
        self.page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[2]/div/span/input', "Huang666")
        # Check input[type="checkbox"]
        self.page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[4]/label/span[1]/input').check()
        # Click button:has-text("登 录")
        self.page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[5]/button/span').click()
        self.page.wait_for_url("https://blankme.stage.meetwhale.com/assets-new/content")
        self.page.click('//*[@id="whale_privacy_btn_ok"]')

    @allure.step("登录")
    def test_login(self, browser: Browser):
        # 创建飞书消息对象
        feishu = SendMsg()
        self.browser = browser
        self.page = self.browser.new_page(locale="zh-CN")
        self.page.goto("https://whale-login.stage.meetwhale.com/login")
        if "https://whale-login.stage.meetwhale.com/login" != self.page.url:
            title = "登录界面进入异常"
            feishu.send_post(title, env='stage', bug='致命', path=self.page.screenshot())
            pytest.fail()
        self.page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[1]/div/span/input', "18709873932")
        self.page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[2]/div/span/input', "Huang66")
        # Check input[type="checkbox"]
        self.page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[4]/label/span[1]/input').check()
        # Click button:has-text("登 录")
        self.page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[5]/button/span').click()
        self.page.wait_for_timeout(3000)
        if "https://whale-login.stage.meetwhale.com/login" == self.page.url:
            title = "未登录成功"
            # 发送消息函数
            feishu.send_post(title, env='stage', bug='严重', path=self.page.screenshot())
            pytest.fail()
        allure.attach(self.page.screenshot(), '登录成功', allure.attachment_type.PNG)
        print("登录成功")

    @allure.step("字段校验")
    def test_zd(self, setup):
        self.page.goto('https://blankme.stage.meetwhale.com/assets-new/content/share')
        feishu = SendMsg()
        self.page.locator('//*[@id="folder_section"]/div[2]/div/div/div/div/div/div/div/div/div/div[2]').click()
        time.sleep(3)
        content = self.page.locator('//*[@id="content-list-container"]/div[1]/div/div[3]/div/div/div/div/div/div/table/thead/tr/th').all_inner_texts()
        if "名称" == content[1]:
            title = "字段正确"
            # 发送消息函数
            feishu.send_post(title, env='stage', bug='一般', path=self.page.screenshot())
        allure.attach(self.page.screenshot(), '字段校验', allure.attachment_type.PNG)
        print(content)




