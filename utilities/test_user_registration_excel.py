import os

import pytest

from pages.home_page import HomePage
from pages.register_page import RegisterPage
from test_data.register_data import RegisterData
from test_data.user_factory import UserFactory
from utilities.assertions import assert_registration_result
from utilities.excel_reader import get_excel_data
from utilities.read_config import Read_Config



@pytest.mark.usefixtures("setup")
class Test_User_Registration_Excel:
    excel_path=os.path.join()(os.getcwd(),"test_data","register_data.xlsx")
    test_data=get_excel_data(excel_path,"Register")


    @pytest.mark.regression
    @pytest.mark.parametrize("user_data", test_data)
    def test_user_registration(self, user_data):
        # self.driver=setup
        self.driver.get(Read_Config.get_base_url() + "register")
        register = RegisterPage(self.driver)
        # print("test passed")
        register.register_user(user_data)
        assert_registration_result(register, user_data["expected"])