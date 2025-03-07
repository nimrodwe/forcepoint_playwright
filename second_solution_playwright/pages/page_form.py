from playwright.async_api import Page, Locator


class PageForm:
    def __init__(self, page: Page):
        self.page = page
        self.name_input_locator = page.locator('#et_pb_contact_name_0')
        self.email_input_locator = page.locator('#et_pb_contact_email_0')
        self.message_input_locator = page.locator('#et_pb_contact_message_0')
        self.captcha_input_locator = page.locator('input[name="et_pb_contact_captcha_0"]')
        self.submit_button_locator = page.locator('button[name="et_builder_submit_button"].et_pb_contact_submit').nth(0)
        self.submit_message_locator = page.locator("div.et-pb-contact-message p")
        self.expected_submit_message = "Thanks for contacting us"
        self.name_text = "jack"
        self.email_text = "jack@example.com"
        self.message_text = "Hello, this is a test message."

    async def safe_execute(self, action, action_name: str, *args):
        try:
            await action(*args)
        except Exception as e:
            raise Exception(f'Error executing {action_name}: {str(e)}')

    async def type_text(self, locator: Locator, text: str):
        await self.safe_execute(locator.fill, "type_text", text)

    async def click_element(self, locator: Locator):
        await self.safe_execute(locator.click, "click_element")

    async def sum_captcha_digits(self):
        first_digit = await self.captcha_input_locator.get_attribute('data-first_digit')
        second_digit = await self.captcha_input_locator.get_attribute('data-second_digit')
        return int(first_digit) + int(second_digit)

    async def get_submit_message(self):
        return await self.submit_message_locator.text_content()
