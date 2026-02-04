import time

import pytest

from pages.checkout_cart_page import CheckoutPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.order_confirmation_page import OrderConfirmation
from pages.product_description_page import ProductPage
from utilities.read_config import Read_Config
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from test_data.user_factory import UserFactory
from test_data.expected_messages import RegisterExpected
from utilities.assertions import assert_registration_result
from utilities.utils import read_json


@pytest.mark.usefixtures("setup")
class Test_Register_And_Login:
    shipping_data = read_json("shipping_data.json")

    @pytest.mark.e2e
    @pytest.mark.regression
    def test_register_then_login_with_same_user(self):
        # self.driver=setup
        home = HomePage(self.driver)
        home.click_register()
        # register = RegisterPage(self.driver)
        valid_user = UserFactory.valid_user()
        register = RegisterPage(self.driver)
        register.register_user(valid_user["user_input"])
        user_email=valid_user["user_input"]['email']
        user_password=valid_user["user_input"]["password"]
        assert valid_user["expected"]["success_message"] in register.get_success_message()
        home.click_logout()
        user_login=LoginPage(self.driver)
        user_login.user_login(user_email,user_password)
        home.click_add_to_cart()
        product = ProductPage(self.driver)
        product.click_product_add_to_cart()
        product.click_product_added_successfully_close()
        home.click_shopping_cart()
        checkout = CheckoutPage(self.driver)
        checkout.click_terms_of_service()
        checkout.click_checkout()
        shipping_info = CheckoutInfoPage(self.driver)
        shipping_info.shipping_user(self.shipping_data["indian_guest"])
        success = OrderConfirmation(self.driver)
        assert "Thank you" in success.get_order_success_msg()

        # self.driver.get(Read_Config.get_base_url() + "login")
        # login = LoginPage(self.driver)
        # login.login(valid_user["email"], valid_user["password"])
        #
        # assert "logout" in self.driver.page_source.lower()