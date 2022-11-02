import time

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.bilibili.com/video/BV1bh411p7Zb/?vd_source=f95e0eaa2951f6c18ede3a0ac9dfea77")

    time.sleep(8)

    browser.close()

import re


