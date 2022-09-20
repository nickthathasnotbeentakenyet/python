from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Sally","Brown") == "Brown; Sally"
    assert make_full_name("S","B") == "B; S"
    assert make_full_name("Sally","Brown-Wazovsky") == "Brown-Wazovsky; Sally"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("B; S") == "B"
    assert extract_family_name("Brown-Wazovsky; Sally") == "Brown-Wazovsky"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Br; S") == "S"
    assert extract_given_name("Brown; Sally J") == "Sally J"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])