def test_error_message_comment_empty(open_feedback_page):
    """@test description: check out error message, when comment empty
            @preconditions:
            1. user navigates to feedback page
            @steps:
            1. click in comment field
            2. click in result field
            @expected result: user receives message 'Please provide a comment.'
           """
    customer_feedback_page = open_feedback_page
    error_message_empty_comment = customer_feedback_page.click_comment_field().click_result_field(). \
        get_error_message_empty_comment()
    assert error_message_empty_comment == 'Please provide a comment.'


def test_error_message_result_empty(open_feedback_page):
    """@test description: check out error message, when result empty
            @preconditions:
            1. user navigates to feedback page
            @steps:
            1. click in comment field
            2. click in result field
            @expected result: user receives message 'Please enter the result of the CAPTCHA.'
           """
    customer_feedback_page = open_feedback_page
    error_message_empty_result = customer_feedback_page.click_result_field().click_comment_field(). \
        get_error_message_empty_result()
    assert error_message_empty_result == 'Please enter the result of the CAPTCHA.'
