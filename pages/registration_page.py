from playwright.sync_api import Page


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_test_id("registration-first-name-input")
        self.last_name_input = page.get_by_test_id("registration-last-name-input")
        self.email_input = page.get_by_test_id("registration-email-input")
        self.password_input = page.get_by_test_id("registration-password-input")
        self.confirm_password_input = page.get_by_test_id("registration-confirm-password-input")
        self.submit_button = page.get_by_test_id("registration-submit-button")

    def fill_registration_first_name_input(self, first_name: str) -> None:
        self.first_name_input.fill(first_name)

    def fill_registration_last_name_input(self, last_name: str) -> None:
        self.last_name_input.fill(last_name)

    def fill_registration_email_input(self, email: str) -> None:
        self.email_input.fill(email)

    def fill_registration_password_input(self, password: str) -> None:
        self.password_input.fill(password)

    def fill_registration_confirm_password_input(self, password: str) -> None:
        self.confirm_password_input.fill(password)

    def click_registration_submit_button(self) -> None:
        self.submit_button.click()
