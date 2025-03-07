import os
from dotenv import load_dotenv
from second_solution_playwright.pages.page_buttons import PageButtons
from second_solution_playwright.pages.page_social import PageSocial
from second_solution_playwright.pages.page_form import PageForm

load_dotenv()


class BaseClass:
    def __init__(self, page):
        self.page = page
        self.base_url: str = os.getenv('BASE_URL')
        self.page_buttons = PageButtons(self.page)
        self.page_social = PageSocial(self.page)
        self.page_form = PageForm(self.page)