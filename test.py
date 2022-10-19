import time
from common import env_util
from common.robot_image import SendMsg
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(storage_state="./data/blankMe_cookie_hyx.json")
    page = context.new_page()

    page.goto(f"https://blankme.{env_util.env}.meetwhale.com/vap/live-detail/725")
    page.wait_for_timeout(3000)
    page.locator("text=确定").click()
    with context.expect_page() as new_page_info:
        page.click('//*[@id="rc-tabs-0-tab-anchor"]')
        page.click('//*[@id="rc-tabs-0-panel-anchor"]/div/div/div/div[3]/div[1]/span[1]/div/span/span/img')
    new_page = new_page_info.value
    time.sleep(3)

    time.sleep(3)
