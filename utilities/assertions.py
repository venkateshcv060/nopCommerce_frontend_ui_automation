def assert_registration_result(register_page, expected):
    if "success_message" in expected:
        actual_success = register_page.get_success_message()
        assert expected["success_message"] in actual_success, (
            f"Expected success message '{expected['success_message']}', "
            f"but got '{actual_success}'"
        )

    if "error_message" in expected:
        actual_errors = register_page.get_error_messages()
        assert expected["error_message"] in actual_errors, (
            f"Expected error message '{expected['error_message']}', "
            f"but got '{actual_errors}'"
        )
