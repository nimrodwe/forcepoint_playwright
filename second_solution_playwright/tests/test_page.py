import pytest
from base_class import BaseClass


class TestSuite:
    @pytest.mark.asyncio
    async def test_button_count(self, setup):
        button_count = await setup.page_buttons.count_buttons()
        assert button_count == setup.page_buttons.expected_count, f"Expected 12 buttons, but got {button_count}"

    @pytest.mark.asyncio
    async def test_facebook_url(self, setup):
        hrefs = await setup.page_social.get_href()
        for href in hrefs:
            assert href == setup.page_social.expected_href, f"Expected Facebook URL, but got {href}"

    @pytest.mark.asyncio
    async def test_form(self, setup):
        await setup.page_form.type_text(setup.page_form.name_input_locator, setup.page_form.name_text)
        await setup.page_form.type_text(setup.page_form.email_input_locator, setup.page_form.email_text)
        await setup.page_form.type_text(setup.page_form.message_input_locator, setup.page_form.message_text)
        captcha_sum = await setup.page_form.sum_captcha_digits()
        await setup.page_form.type_text(setup.page_form.captcha_input_locator, str(captcha_sum))
        await setup.page_form.click_element(setup.page_form.submit_button_locator)
        assert await setup.page_form.get_submit_message() == setup.page_form.expected_submit_message, f"Expected submit message, but got {await setup.page_form.submit_message}"