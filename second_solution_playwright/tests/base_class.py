import os
from dotenv import load_dotenv
from second_solution_playwright.pages.page_buttons_section import PageButtons

load_dotenv()


class BaseClass(PageButtons):
    def __init__(self, page):
        super().__init__(page)
        self.base_url = os.getenv('BASE_URL')
        self.page_buttons = PageButtons(self.page)
