from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_authorization() -> None:
    """
    Тестирует обработку системы при попытке входа с неверными учетными данными.

    Проверяет следующие аспекты:
    1. Система корректно отображает форму авторизации
    2. При вводе неверных данных появляется соответствующее сообщение об ошибке
    3. Сообщение об ошибке содержит правильный текст

    Шаги выполнения:
    1. Открывает страницу авторизации
    2. Заполняет поле email значением "user.name@gmail.com"
    3. Заполняет поле password значением "password"
    4. Нажимает кнопку входа
    5. Проверяет видимость сообщения об ошибке
    6. Проверяет текст сообщения об ошибке ("Wrong email or password")

    Ожидаемый результат:
    - После отправки формы появляется сообщение об ошибке
    - Текст сообщения соответствует ожидаемому

    Пример использования:
        >>> test_wrong_email_or_password_authorization()
        [Выполняет тест и проверяет сообщение об ошибке]
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill("password")

        login_button = page.get_by_test_id('login-page-login-button')
        login_button.click()

        wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
