from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list() -> None:
    """
    Выполняет регистрацию пользователя, сохраняет состояние сессии
    и проверяет доступ к защищенной странице Courses.

    Шаги:
    1. Открывает страницу регистрации
    2. Заполняет форму регистрации
    3. Сохраняет состояние аутентификации
    4. Проверяет доступ к странице Courses с сохраненной сессией
    5. Проверяет наличие элементов на странице Courses
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user.name@gmail.com')

        user_input = page.get_by_test_id('registration-form-username-input').locator('input')
        user_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')

        courses_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_text).to_be_visible()
        expect(courses_text).to_have_text('There is no results')
