import pytest

from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_register_page:


    def test_valid_user_registration(self):
        home=HomePage(self.driver)
        title=home.get_title()
        assert "Home page" in title
        home.click_register()
        print("test pass")

    def  test_invalid_user_registration(self):


