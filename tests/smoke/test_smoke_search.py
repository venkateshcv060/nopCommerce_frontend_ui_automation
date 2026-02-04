import time

import pytest

from pages.home_page import HomePage


class Test_Search:

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_search_box(self):
        home=HomePage(self.driver)
        home.search_product("company")
        assert "computer" in home.get_page_source()





