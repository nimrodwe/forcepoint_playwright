import time

import pytest
from base_class import BaseClass


class TestsSuite:
    @pytest.mark.asyncio
    async def test_button_count(self, setup):
        base = BaseClass(setup)
        button_count = await base.page_buttons.count_buttons()
        assert button_count == base.page_buttons.expected_count, f"Expected 12 buttons, but got {button_count}"

    @pytest.mark.asyncio
    async def test_facebook_url(self, setup):
        base = BaseClass(setup)
        hrefs = await base.page_social.get_href()
        for href in hrefs:
            assert href == base.page_social.expected_href, f"Expected Facebook URL, but got {href}"

    @pytest.mark.asyncio
    async def test_form(self, setup):
        base = BaseClass(setup)
        await base.page_form.type_text(base.page_form.name_input_locator, base.page_form.name_text)
        await base.page_form.type_text(base.page_form.email_input_locator, base.page_form.email_text)
        await base.page_form.type_text(base.page_form.message_input_locator, base.page_form.message_text)
        captcha_sum = await base.page_form.sum_captcha_digits()
        await base.page_form.type_text(base.page_form.captcha_input_locator, str(captcha_sum))
        await base.page_form.click_element(base.page_form.submit_button_locator)
        assert await base.page_form.get_submit_message() == base.page_form.expected_submit_message, f"Expected submit message, but got {await base.page_form.submit_message}"