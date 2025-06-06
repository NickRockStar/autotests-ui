from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str): # Метод для загрузки страницы
        self.page.goto(url, wait_until='networkidle')

    def reload(self):  # Метод для перезагрузки страницы
        self.page.reload(wait_until='domcontentloaded')
