from faker import Faker
import random
import string

fake = Faker()

class UserFactory:

    @staticmethod
    def _generate_password(length=10):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    @staticmethod
    def valid_user():
        password = UserFactory._generate_password()

        return {"user_input":{
            "gender": random.choice(["male", "female"]),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": f"{fake.user_name()}@gmail.com",
            "company": fake.company(),
            "newsletter": random.choice([True, False]),
            "password": password,
            "confirm_password": password
        },
        "expected": {
            "success_message": "Your registration completed"
        }}



    @staticmethod
    def invalid_user_no_password():
        return {"user_input":{
            "gender": random.choice(["male", "female"]),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": f"{fake.user_name()}@gmail.com",
            "company": fake.company(),
            "newsletter": random.choice([True, False]),
            "password": "",
            "confirm_password": ""
        },
        "expected": {
            "error_message": "Password is required."
        }}
