import pytest
import ex2_function as vs
# Checks if format_cnpj() outputs the correct integer list from a cnpj string
def test_correct_format():
  assert vs.format_cnpj("11.222.333/0001-00") == [1,1,2,2,2,3,3,3,0,0,0,1,0,0]
  assert vs.format_cnpj("11222333000100") == [1,1,2,2,2,3,3,3,0,0,0,1,0,0]
# Checks if format_cnpj() outputs an empty list when it encounters invalid cnpj string sizes.
def test_invalid_string_size():
  assert vs.format_cnpj("021236830975") == []
  assert vs.format_cnpj("1111111111111111111") == []
  assert vs.format_cnpj("1") == []
# Checks if validate_cnpj() outputs the correct message when it receives a valid CNPJ string.
def test_correct_validate_cnpj():
  assert vs.validate_cnpj("11.222.333/0001-81") == "Valid CNPJ"
  assert vs.validate_cnpj("11222333000181") == "Valid CNPJ"
# Checks if validate_cnpj() correctly outputs an invalid message when the input CNPJ is invalid.
def test_invalid_validate_cnpj():
  assert vs.validate_cnpj("11222333000100") == "Invalid CNPJ"
  assert vs.validate_cnpj("11.222.333/0001-00") == "Invalid CNPJ"
