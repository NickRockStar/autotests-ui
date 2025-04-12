from playwright.sync_api import Page, expect


def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text('There is no results')
