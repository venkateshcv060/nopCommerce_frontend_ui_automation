class RegisterData:

    VALID_USER = {
        "user_input": {
            "gender": "male",
            "first_name": "Venkatesh",
            "last_name": "Prasad",
            "email": "henki_test_001@gmail.com",
            "company": "TestCompany",
            "newsletter": True,
            "password": "Test@1234",
            "confirm_password": "Test@1234"
        },
        "expected": {
            "success_message": "Your registration completed"
        }
    }

    INVALID_USER_NO_PASSWORD = {
        "user_input": {
            "gender": "male",
            "first_name": "Venkatesh",
            "last_name": "Prasad",
            "email": "henky_test_002@gmail.com",
            "company": "TestCompany",
            "newsletter": True,
            "password": "",
            "confirm_password": ""
        },
        "expected": {
            "error_message": "Password is required."
        }
    }