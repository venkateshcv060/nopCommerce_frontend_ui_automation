class RegisterData:

    VALID_USER = {
        "gender": "male",
        "first_name": "Venkatesh",
        "last_name": "Prasad",
        "email": "venky_test_001@gmail.com",
        "company": "TestCompany",
        "newsletter": True,
        "password": "Test@1234",
        "confirm password":"Test@1234"
    }

    INVALID_USER_NO_PASSWORD = {
        "gender": "male",
        "first_name": "Venkatesh",
        "last_name": "Prasad",
        "email": "venky_test_002@gmail.com",
        "company": "TestCompany",
        "newsletter": True,
        "password": "",
        "confirm password": ""
    }
