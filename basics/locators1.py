
from playwright.sync_api import sync_playwright

with sync_playwright as play:
    browser = play.chromium.launch(headless = False)
    page.browse
