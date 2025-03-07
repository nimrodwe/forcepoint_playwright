from playwright.async_api import Page


class PageSocial:
    def __init__(self, page: Page):
        self.page = page
        self.facebook_icons_class = page.locator('a[title="Follow on Facebook"]')
        self.expected_href: str = 'https://www.facebook.com/Ultimateqa1/'

    async def get_href(self) -> list[str]:
        hrefs: list[str] = await self.facebook_icons_class.evaluate_all(
            "(elements) => elements.map(el => el.getAttribute('href'))"
        )
        return hrefs
