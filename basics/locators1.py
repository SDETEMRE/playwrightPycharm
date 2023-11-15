from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/')

    emailbox = page.wait_for_selector('#email')
    emailbox.type('test@yahoo.com')

    submitbutton = page.wait_for_selector('#enterimg')
    submitbutton.click()
    page.wait_for_timeout(3000)