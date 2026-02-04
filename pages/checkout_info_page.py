from selenium.webdriver.common.by import By
from pages.base_page import BasePage



class CheckoutInfoPage(BasePage):
        SHIP_TO_SAME_ADDRESS_CHECKBOX=(By.ID,"ShipToSameAddress")
        BILLING_FIRST_NAME=(By.ID,"BillingNewAddress_FirstName")
        BILLING_LAST_NAME = (By.ID, "BillingNewAddress_LastName")
        BILLING_EMAIL=(By.ID,"BillingNewAddress_Email")
        BILLING_SELECT_COUNTRY_DROPDOWN=(By.ID,"BillingNewAddress_CountryId")#104  India
        #BILLING_SELECT_STATE_DROPDOWN=(By.ID,"BillingNewAddress_StateProvinceId")#856   Karnataka
        BILLING_SELECT_STATE_DROPDOWN=(By.CSS_SELECTOR,"#BillingNewAddress_StateProvinceId")
        BILLING_CITY_NAME=(By.ID,"BillingNewAddress_City")
        BILLING_ADDRESS_1=(By.ID,"BillingNewAddress_Address1")
        BILLING_ADDRESS_2=(By.ID,"BillingNewAddress_Address2")
        BILLING_POSTAL_CODE=(By.ID,"BillingNewAddress_ZipPostalCode")
        BILLING_PHONE_NUMBER=(By.ID,"BillingNewAddress_PhoneNumber")
        BILLING_FAX_NUMBER=(By.ID,"BillingNewAddress_FaxNumber")
        BILLING_ADDRESS_SAVE_BUTTON=(By.ID,"save-billing-address-button")

        BILLING_ADDRESS_CONTINUE_BUTTON=(By.XPATH,"//button[@onclick='Billing.save()']")
        SHIPPING_ADDRESS_CONTINUE_BUTTON=(By.XPATH,"//button[@onclick='Shipping.save()']")

        SHIP_BY_GROUND = (By.ID,"shippingoption_0")
        SHIP_NEXT_DAY_AIR=(By.ID,"shippingoption_1")
        SHIP_SECOND_DAY_AIR=(By.ID,"shippingoption_2")
        SHIPPING_METHOD_CONTINUE_BTN=(By.CSS_SELECTOR,".button-1.shipping-method-next-step-button")

        CHECK_OR_MONEY_ORDER_PAYMENT=(By.ID,"paymentmethod_0")
        CREDIT_CARD_PAYMENT=(By.ID,"paymentmethod_1")
        PAYMENT_METHOD_CONTINUE_BTN=(By.CSS_SELECTOR,".button-1.payment-method-next-step-button")
        PAYMENT_INFO_CONTINUE_BTN=(By.CSS_SELECTOR,".button-1.payment-info-next-step-button")

        CONFIRM_ORDER_BUTTON=(By.CSS_SELECTOR,".button-1.confirm-order-next-step-button")





        def __init__(self, driver):
          self.driver=driver

        def click_ship_to_same_address(self):
            self.click(self.SHIP_TO_SAME_ADDRESS_CHECKBOX)

        def enter_billing_first_name(self,first_name):
           self.send_keys(self.BILLING_FIRST_NAME, first_name)

        def enter_billing_last_name(self,last_name):
           self.send_keys(self.BILLING_LAST_NAME, last_name)

        def enter_billing_email(self,email):
            self.send_keys(self.BILLING_EMAIL,email)

        def select_billing_country(self,country_name):
            self.select_by_text(self.BILLING_SELECT_COUNTRY_DROPDOWN,country_name)

        def select_billing_state(self,state_name):
            self.select_by_text(self.BILLING_SELECT_STATE_DROPDOWN,state_name)

        def enter_billing_city(self,city_name):
            self.send_keys(self.BILLING_CITY_NAME,city_name)

        def enter_address1(self, address1):
            self.send_keys(self.BILLING_ADDRESS_1,address1)

        def enter_address2(self, address2):
            self.send_keys(self.BILLING_ADDRESS_2, address2)

        def enter_postal_code(self,postal_code):
            self.send_keys(self.BILLING_POSTAL_CODE,postal_code)

        def enter_phone_number(self,phone_no):
            self.send_keys(self.BILLING_PHONE_NUMBER,phone_no)

        def click_billing_save(self):
            self.click(self.BILLING_ADDRESS_SAVE_BUTTON)

        def click_billing_continue(self):
            self.click(self.BILLING_ADDRESS_CONTINUE_BUTTON)

        def click_shipping_address_continue(self):
            self.click(self.SHIPPING_ADDRESS_CONTINUE_BUTTON)

        def click_next_day_air(self):
            self.click(self.SHIP_NEXT_DAY_AIR)

        def click_shipping_method_continue(self):
            self.click(self.SHIPPING_METHOD_CONTINUE_BTN)

        def click_cheque_or_money_order(self):
            self.click(self.CHECK_OR_MONEY_ORDER_PAYMENT)

        def click_credit_card(self):
            self.click(self.CREDIT_CARD_PAYMENT)

        def click_payment_continue(self):
            self.click(self.PAYMENT_METHOD_CONTINUE_BTN)

        def click_payment_info_continue(self):
            self.click(self.PAYMENT_INFO_CONTINUE_BTN)

        def click_confirm(self):
            self.click(self.CONFIRM_ORDER_BUTTON)

        def shipping_user(self, user):
            self.click_ship_to_same_address()
            self.enter_billing_first_name(user["first_name"])
            self.enter_billing_last_name(user["last_name"])
            self.enter_billing_email(user["email"])
            self.select_billing_country(user["country"])
            self.select_billing_state(user["state"])
            self.enter_billing_city(user["city"])
            self.enter_address1(user["address1"])
            self.enter_postal_code(user["postal_code"])
            self.enter_phone_number(user["phone"])
            self.click_billing_continue()

            self.click_shipping_address_continue()

            self.click_next_day_air()
            self.click_shipping_method_continue()

            self.click_cheque_or_money_order()
            self.click_payment_continue()

            self.click_payment_info_continue()
            self.click_confirm()






