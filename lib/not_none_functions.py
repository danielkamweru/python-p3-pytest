# testing/test_not_none.py

from lib.not_none_functions import get_user_info

def test_user_is_admin():
    """
    Test that get_user_info() returns Daniel and that is_Admin is True
    """
    user = get_user_info()
    
    # Check that the return value is not None
    assert user is not None, "Function should not return None"
    
    # Check that the name is 'Daniel'
    assert user.get("name") == "Daniel", "Expected name to be Daniel"
    
    # Check that is_Admin is True
    assert user.get("is_Admin") is True, "Expected is_Admin to be True"
