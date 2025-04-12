import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(initialize_browser_state: Page, chromium_page_with_state):
        initialize_browser_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = initialize_browser_state.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        password_input = initialize_browser_state.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        login_button = initialize_browser_state.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = chromium_page_with_state.get_by_test_id('login-page-wrong-email'
                                                                                '-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
