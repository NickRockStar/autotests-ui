from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.get_by_test_id("dashboard-toolbar-title-text")

    def is_title_visible(self) -> bool:
        return self.title.is_visible()
