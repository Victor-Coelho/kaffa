import pytest
from main import check_cnpj_string

# Test for invalid characters where it should be a punctiation character.
def test_invalid_punct():
    assert check_cnpj_string("02~123=683`0975/31") == "Invalid formatted CNPJ: incorrect punctuation."
    assert check_cnpj_string("02s123.683/0975-31") == "Invalid formatted CNPJ: incorrect punctuation."
# Test for invalid CNPJ string size.
def test_invalid_size():
    assert check_cnpj_string("021236830975") == "Invalid CNPJ format: invalid number of characters."
    assert check_cnpj_string("1111111111111111111") == "Invalid CNPJ format: invalid number of characters."
    assert check_cnpj_string("")
    assert check_cnpj_string("1")
# Test for invalid characters - there should be only numbers or the correct punctuation characters.
def test_invalid_characters():
    assert check_cnpj_string("02123683d9753a") == "Invalid formatted CNPJ: incorrect characters;  all characters must be numbers."
    assert check_cnpj_string("02.123.683/0975-3a") == "Invalid formatted CNPJ: incorrect characters;  all characters, aside from punctiation characters, must be numbers."
# Tests for valid input of a formatted CNPJ string
def test_valid_formatted_string():
    assert check_cnpj_string("12.345.678/9012-34") == "CNPJ is correctly formatted."
# Tests for valid input of a numbers only CNPJ string
def test_valid_numbers_only_string():
    assert check_cnpj_string("12345678901234") == "CNPJ is correctly formatted."