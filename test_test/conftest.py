import pytest
from playwright.sync_api import Browser
from common import env_util


@pytest.fixture(scope='session')
def login_hyx(browser: Browser):
    context = browser.new_context(locale="zh-CN")
    # context.add_init_script(js)
    page = context.new_page()
    page.goto("https://whale-login.prod.meetwhale.com/login")
    # 输入账号密码
    page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[1]/div/span/input', "18709873932")
    page.fill('//*[@id="container"]/section/div[2]/div/div[3]/div[2]/div/span/input', "Huang666")
    # Check input[type="checkbox"]
    page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[4]/label/span[1]/input').check()
    # Click button:has-text("登 录")
    page.locator('//*[@id="container"]/section/div[2]/div/div[3]/div[5]/button/span').click()
    page.wait_for_timeout(3000)
    # page.locator('//*[@id="whale_privacy_btn_ok"]').click()
    # Save storage state into the file
    # 保存json  此处的相对路径是根据main函数的相对路径
    context.storage_state(path="../data/blankMe_cookie_hyx.json")
    print("登录成功")
    yield
    print("执行完毕")


@pytest.fixture(scope='session')
def api(playwright):
    request_context = playwright.request.new_context(
        base_url=f'https://blankme.{env_util.env}.meetwhale.com'
    )
    yield request_context
    request_context.dispose()

