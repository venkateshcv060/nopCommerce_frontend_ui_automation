import pytest

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from test_data.register_data import RegisterData
from utilities.assertions import assert_registration_result


@pytest.mark.usefixtures("setup")
class Test_register_page:

    @pytest.mark.parametrize("user_data", [RegisterData.VALID_USER,RegisterData])
    def test_user_registration(self,user_data):
        home=HomePage(self.driver)
        home.click_register()
        register=RegisterPage(self.driver)
        # print("test passed")
        register.register_user(user_data["input"])
        assert_registration_result(register, user_data["expected"])

    # def  test_invalid_user_registration(self):


