import pytest
from base_class import BaseClass


class TestsSuite(BaseClass):
    @pytest.mark.asyncio
    async def test_button_count(self, setup):
        button_count = await BaseClass.count_buttons(self)
        assert button_count == 12, f"Expected 12 buttons, but got {button_count}"
