import pytest

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from test_data.register_data import RegisterData
from test_data.user_factory import UserFactory
from utilities.assertions import assert_registration_result
from utilities.read_config import Read_Config


@pytest.mark.usefixtures("setup")
class Test_register_page:

    # @pytest.mark.parametrize("user_data", [RegisterData.VALID_USER,RegisterData.INVALID_USER_NO_PASSWORD])
    # def test_user_registration(self,user_data):
    #     self.driver.get(Read_Config.get_base_url() + "register")
    #     register=RegisterPage(self.driver)
    #     # print("test passed")
    #     register.register_user(user_data["user_input"])
    #     assert_registration_result(register, user_data["expected"])

    @pytest.mark.regression
    @pytest.mark.parametrize("user_data", [UserFactory.valid_user(), UserFactory.invalid_user_no_password()])
    def test_user_registration(self, user_data):
        # self.driver=setup
        self.driver.get(Read_Config.get_base_url() + "register")
        register = RegisterPage(self.driver)
        # print("test passed")
        register.register_user(user_data["user_input"])
        assert_registration_result(register, user_data["expected"])

    # def  test_invalid_user_registration(self):


