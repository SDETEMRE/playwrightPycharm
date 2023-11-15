from playwright.sync_api import sync_playwright

with sync_playwright() as play:
    browser = play.chromium.launch(headless = False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    #page.goto('https://demo.automationtesting.in/')

    # emailbox = page.wait_for_selector('#email')
    # emailbox.type('test@yahoo.com')
    #
    # submitbutton = page.wait_for_selector('#enterimg')
    # submitbutton.click()
    # page.wait_for_timeout(3000)

    usernameBox = page.wait_for_selector('[name=username]')
    usernameBox.type('Admin')

    passwordBox = page.wait_for_selector('[type=password]')
    passwordBox.type('admin123')

    loginButton = page.wait_for_selector('[type=submit]')
    loginButton.click()

    page.wait_for_timeout(3000)