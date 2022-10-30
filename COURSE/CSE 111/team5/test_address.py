from address import * 
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("667 Lake street, Salt Lake, ID 83880") == "Salt Lake"
    assert extract_city("123 W Main, Rexburg, ID 83440") == "Rexburg"
    assert extract_city("78 Pine St, Avon Park, FL 33825") == "Avon Park"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("667 Lake street, Salt Lake,            UT 83880") == "UT"
    assert extract_state("123 W Main, Rexburg, ID 83440") == "ID"
    assert extract_state("78 Pine St, Avon Park, FL 33825") == "FL"

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("123 W Main, Rexburg, ID 83440") == "83440"
    assert extract_zipcode("78 Pine St, Avon Park, FL 33825") == "33825"


pytest.main(["-v", "--tb=line", "-rN", __file__])