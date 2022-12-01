import time
from common import env_util
from common.robot_image import SendMsg
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context(storage_state="./data/blankMe_cookie_hyx.json")
    page = context.new_page()

    page.goto(f"https://blankme.{env_util.env}.meetwhale.com/vap/anchor-list")
    page.wait_for_timeout(3000)
    page.click('//*[@id="root-content"]/div/div/div/div[4]/div/div/div/div/div/div/div/table/tbody/tr[2]')
    time.sleep(3)

    time.sleep(3)
