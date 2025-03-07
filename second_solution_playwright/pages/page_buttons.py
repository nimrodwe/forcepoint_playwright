from playwright.async_api import Page


class PageButtons:
    def __init__(self, page: Page):
        self.page = page
        self.buttons = page.locator("[class^='et_pb_button et_pb_button_']")
        self.counter = int
        self.expected_count = 12

    async def count_buttons(self) -> int:
        return await self.buttons.count()