from playwright.sync_api import sync_playwright, expect


def test_successful_registration() -> None:
    """
        Тестирует успешную регистрацию пользователя и последующий доступ к Dashboard.

        Процесс тестирования включает два основных этапа:
        1. Регистрация нового пользователя:
           - Заполнение формы регистрации
           - Отправка данных
           - Сохранение состояния сессии
        2. Проверка доступа к защищенной странице Dashboard с использованием сохраненной сессии.

        Требования:
        - Доступность тестируемого сайта
        - Корректная работа формы регистрации
        - Возможность сохранения состояния браузера

        Пример использования:
            >>> test_successful_registration()
            [Выполняет регистрацию и проверку доступа к Dashboard]
        """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
