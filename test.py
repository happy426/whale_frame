import time
from common import env_util
from common.robot_image import SendMsg
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(storage_state="./data/blankMe_cookie_hyx.json")
    page = context.new_page()

    page.goto(f"https://blankme.{env_util.env}.meetwhale.com/vap/live-list")
    text = page.inner_text('.ant-table-tbody >> //tr[2]//td/div')
    page.wait_for_timeout(1000)
    page.click('.ant-table-tbody >> //tr[2]')
    with context.expect_page() as new_page_info:
        page.click("text='场控视角'")
    new_page = new_page_info.value
    new_page.wait_for_timeout(1000)
    content = new_page.inner_html('text="实时直播内容" >> //../div[2]')
    if "暂无直播内容</div>" in content:
        print('暂无直播内容')

    time.sleep(3)
