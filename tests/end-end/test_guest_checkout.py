import pytest

from pages.checkout_cart_page import CheckoutPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.home_page import HomePage
from pages.product_description_page import ProductPage
from utilities.utils import read_json


@pytest.mark.usefixtures("setup")
class Test_guest_checkout:
    shipping_data = read_json("shipping_data.json")

    @pytest.mark.e2e
    @pytest.mark.regression
    @pytest.mark.parametrize("user",[shipping_data["indian_guest"]])
    def test_guest_user_checkout(self,user):
        # self.driver=setup
        home=HomePage(self.driver)
        home.click_add_to_cart()
        product=ProductPage(self.driver)
        product.click_product_add_to_cart()
        product.click_product_added_successfully_close()
        home.click_shopping_cart()
        checkout=CheckoutPage(self.driver)
        checkout.click_terms_of_service()
        checkout.click_checkout()
        checkout.click_checkout_as_guest()
        shipping_info=CheckoutInfoPage(self.driver)
        shipping_info.shipping_user(user)
        print("test pass")

