from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.locator('//*[@id=":r0:"]')
    email_input.fill('user.name@gmail.com')

    user_input = page.locator('//*[@id=":r1:"]')
    user_input.fill('username')

    password_input = page.locator('//*[@id=":r2:"]')
    password_input.fill('password')

    registrasion_button = page.get_by_test_id('registration-page-registration-button')
    registrasion_button.click()

    page.wait_for_selector('text=Dashboard', state='visible')
