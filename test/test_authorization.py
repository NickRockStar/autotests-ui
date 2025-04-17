import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("email, password", [
    ("user.name@gmail.com", "password"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
])
def test_wrong_email_or_password_authorization(page: Page, email: str, password: str):
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    error_message = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Wrong email or password")
