import pytest
from main import check_cnpj_string

def test_invalid_punct():
    assert check_cnpj_string("02~123=683`0975/31") == "Invalid formatted CNPJ: incorrect punctuation."
    assert check_cnpj_string("02s123.683/0975-31") == "Invalid formatted CNPJ: incorrect punctuation."
def test_invalid_size():
    assert check_cnpj_string("021236830975") == "Invalid CNPJ format: invalid number of characters."
    assert check_cnpj_string("1111111111111111111") == "Invalid CNPJ format: invalid number of characters."
def test_invalid_characters():
    assert check_cnpj_string("02123683d9753a") == "Invalid formatted CNPJ: incorrect characters;  all characters must be numbers."
    assert check_cnpj_string("02.123.683/0975-3a") == "Invalid formatted CNPJ: incorrect characters;  all characters, aside from punctiation characters, must be numbers."
