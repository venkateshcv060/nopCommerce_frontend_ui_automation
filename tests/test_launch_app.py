import pytest

from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_home_page:

    def test_launch_application(self):
        home=HomePage(self.driver)
        title=home.get_title()
        assert "Home page" in title
        home.click_register()
        print("test pass")


