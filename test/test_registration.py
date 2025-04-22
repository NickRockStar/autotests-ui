from playwright.sync_api import expect

import fixtures.pages


@fixtures.pages.registration_page
def test_successful_registration(registration_page, dashboard_page):
    registration_page.page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_page.fill_registration_first_name_input("Иван")
    registration_page.fill_registration_last_name_input("Петров")
    registration_page.fill_registration_email_input("ivan.petrov@example.com")
    registration_page.fill_registration_password_input("SecurePass123!")
    registration_page.fill_registration_confirm_password_input("SecurePass123!")

    registration_page.click_registration_submit_button()

    expect(dashboard_page.dashboard_title).to_be_visible()
    expect(dashboard_page.dashboard_title).to_have_text("Dashboard")
