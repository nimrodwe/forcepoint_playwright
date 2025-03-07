import pytest_asyncio
from playwright.async_api import async_playwright
from second_solution_playwright.tests.base_class import BaseClass


@pytest_asyncio.fixture(scope="function")
async def setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        context = await browser.new_context()
        page = await context.new_page()

        # Calling the base class which needs to receive the page object
        base = BaseClass(page)
        await page.goto(base.base_url)
        yield page
        await page.close()
        await browser.close()

