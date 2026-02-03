import pytest

from pages.base_page import BasePage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_home_page:

    @pytest.mark.smoke
    def test_launch_application(self):
        home=HomePage(self.driver)
        assert "Home page" in home.get_title()

    @pytest.mark.smoke
    def test_base_url(self):
        # base=BasePage(self.driver)
        assert "http" in BasePage(self.driver).get_current_url()






