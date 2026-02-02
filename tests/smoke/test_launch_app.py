import pytest

from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_home_page:

    @pytest.mark.smoke
    def test_launch_application(self):
        home=HomePage(self.driver)
        title=home.get_title()
        assert "Home page" in title


