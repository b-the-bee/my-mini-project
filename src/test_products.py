def fast_user_choice():
    # possible_options = [0, 1, 2, 3, 4]
    fast_choice = 2
    return fast_choice
    

def products_get_user_choice():
    user_choice = fast_user_choice()
    return user_choice

def test_products_get_user_choice_happy():
    expected = [0, 1, 2, 3, 4]
    result = products_get_user_choice()
    assert result in expected
