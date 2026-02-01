#
# import configparser
# config=configparser.RawConfigParser()
# config.read(".\\Configurations\\config.ini")
#
# class Read_Config:
#     @staticmethod
#     def get_swag_url():
#         url=config.get('user login info','swag_url')
#         return url
#
#     @staticmethod
#     def get_username():
#         username=config.get('user login info', 'username')
#         return username
#
#     @staticmethod
#     def get_password():
#         password = config.get('user login info', 'password')
#         return password
#
#     @staticmethod
#     def get_inventory_url():
#         inventory_url = config.get('user login info', 'inventory_url')
#         return inventory_url
#
#     @staticmethod
#     def get_checkout_first_name():
#         get_firstname= config.get('user login info', 'checkout_first_name')
#         return get_firstname
#
#     @staticmethod
#     def get_checkout_last_name():
#         get_lastname = config.get('user login info', 'checkout_last_name')
#         return get_lastname
#
#     @staticmethod
#     def get_checkout_postal_code():
#         get_postal_code = config.get('user login info', 'checkout_postal_code')
#         return get_postal_code



import yaml
import os

class Read_Config:

    @staticmethod
    def get_base_url():
        config_path = os.path.join(os.getcwd(), "config", "qa.yaml")
        with open(config_path) as f:
            data = yaml.safe_load(f)
        return data["app"]["base_url"]
