# lib/testing/subdirectory/bool_test.py

from lib.bool_functions import return_true

def test_return_true():
    """Test that return_true() returns True."""
    assert return_true() is True
