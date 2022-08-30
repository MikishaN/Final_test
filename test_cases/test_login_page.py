import time

import pytest

from unilities.data_generator import random_string


def test_wrong_creds_check(open_login_page):
    """@test description: check, that user can't login with wrong creds
    @preconditions:
    1. user navigates to login page
    @steps:
    1. enter wrong email and wrong password
    2. click Log in button
    @expected result: user receives message 'Invalid email or password.'
    """
    login_page = open_login_page
    validation_message = login_page.enter_email(random_string()).enter_password(
        random_string()).click_login_button().get_error_messages()
    assert validation_message == 'Invalid email or password.'


def test_login_button_state_email_empty(open_login_page):
    """@test description: check, that the Login button is not active, when  email empty
       @preconditions:
       1. user navigates to login page
       @steps:
       1. enter password
       2. check the Login button
       @expected result: the Login button is not active'
       """
    login_page = open_login_page
    login_page.enter_email('').enter_password(random_string())
    actual_result = login_page.is_login_button_active()
    assert actual_result is False, 'Login button is active'


def test_login_button_state_pass_empty(open_login_page):
    """@test description: check, that the Login button is not active, when  password empty
           @preconditions:
           1. user navigates to login page
           @steps:
           1. enter password
           2. check the Login button
           @expected result: the Login button is not active'
           """
    login_page = open_login_page
    login_page.enter_email(random_string()).enter_password('')
    actual_result = login_page.is_login_button_active()
    assert actual_result is False, 'Login button is active'


def test_error_message_email_empty(open_login_page):
    """@test description: check out error message, when email empty
            @preconditions:
            1. user navigates to login page
            @steps:
            1. click in email field
            2. click in password field
            @expected result: user receives message 'Please provide an email address.'
           """
    login_page = open_login_page
    error_message_empty_email = login_page.click_email_field().click_password_field().get_error_message_empty_email()
    assert error_message_empty_email == 'Please provide an email address.'


def test_error_message_password_empty(open_login_page):
    """@test description: check out error message, when password empty
            @preconditions:
            1. user navigates to login page
            @steps:
            1. click in password field
            2. click in email field
            @expected result: user receives message 'Please provide a password.'
           """
    login_page = open_login_page
    error_message_empty_password = login_page.click_password_field().click_email_field(). \
        get_error_message_empty_password()
    assert error_message_empty_password == 'Please provide a password.'


def test_open_forgot_password_page(open_login_page):
    """@test description: test verifies that login page can be opened
            @preconditions:
            1. user navigates to login page
            @steps:
            1. click "Forgot password"
            @expected: user redirected to Forgot password page
            """
    login_page = open_login_page
    forgot_password_page = login_page.open_forgot_password_page()
    assert forgot_password_page.is_forgot_form_present() is True, "Forgot password page is not opened"
