# import time
#
# from playwright.sync_api import sync_playwright, expect
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=100)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.baidu.com/")
#     # print(page.inner_html('#s-top-left:has(a) > a:nth-child(2)'))
#     print(page.inner_html(":nth-match([class='hotsearch-item even'], 2) >> a"))
#     # time.sleep(2)
#     # with context.expect_page() as new_page_info:
#     #     page.locator('//*[@id="s-top-left"]/a[6]').click()
#     # new_page = new_page_info.value
#     time.sleep(2)
#
#     browser.close()

import re


