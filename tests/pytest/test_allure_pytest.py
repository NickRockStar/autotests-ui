import allure


# Вариант № 1
@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...

    with allure.step("Start browser"):
        ...


# @allure.step("Closing browser")
# def create_course(title: str):
#     with allure.step(f"Creating course with title '{title}'"):
#         ...


# with allure.step(f"Creating course with title '{title}'"):
    def close_browser(title: str):
        ...


# Вариант № 2
def test_feature():
    with allure.step("Opening browser"):
        ...

    with allure.step("Creating course"):
        ...

    with allure.step("Closing browser"):
        ...


# Вариант № 3 -> подставляет в титл вариант 1
# def test_feature2():
#     open_browser()
#     create_course(title="Locust")
#     create_course(title="Python")
#     create_course(title="Playwright")
#     close_browser()
