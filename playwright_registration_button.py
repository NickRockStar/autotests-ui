from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    
    disable_button = page.get_by_test_id('registration-page-registration-button')
    expect(disable_button).to_be_disabled()

    email_input = page.locator('//*[@id=":r0:"]')
    email_input.fill('user.name@gmail.com')

    user_input = page.locator('//*[@id=":r1:"]')
    user_input.fill('username')

    password_input = page. locator('//*[@id=":r2:"]')
    password_input.fill('password')

    expect(disable_button).to_be_editable()

    page.wait_for_timeout(3000)
