# Kaffa - Pre-qualification Test Resolution
Author: Víctor Coelho
## Requirements
These solutions require [Python](https://www.python.org/) and [Pytest](https://docs.pytest.org/en/stable/) to be installed.
## How to Build and Run Exercises Solutions
Exercise solutions can be run from the **main.py** in conjunction with the **input.txt** that contains an assortment of CNPJ strings. From the root of the repository, use the command:\
``
python main.py < input.txt
``

To see the ouput in your terminal.

## Testing with Pytest
Both Solutions also come with Pytest tests. To run these tests, from the root of the repository, use the command in your terminal:\
``
pytest -v
``

Pytest will then display the results of all tests created for the solutions of exercises. Below all test functions are described.
## Video with Execution and Solution Explanation
[This link](https://youtu.be/05HetbCzM9E) leads to a video explanation of both Exercise Solutions and, also, an example of running **Pytest** and the **main.py** function.
### Exercise 1 Tests
**File: ex1_test.py**

**test_invalid_punct():** Test for invalid characters where it should be a punctiation character.
**test_invalid_size():** Test for invalid CNPJ string size.
**test_invalid_characters():** Tests for invalid characters - there should be only numbers or the correct punctuation characters.
**test_valid_formatted_string():** Tests for valid input of a formatted CNPJ string
**test_valid_numbers_only_string():** Tests for valid input of a numbers only CNPJ string\
**test_valid_numbers_only_string():** Tests for valid input of a numbers only CNPJ string

### Exercise 2 Tests
**File: ex2_test.py**

**test_correct_format():** Checks if format_cnpj() outputs the correct integer list from a cnpj string\
**test_invalid_string_size():** Checks if format_cnpj() outputs an empty list when it encounters invalid cnpj string sizes.\
**test_correct_validate_cnpj():** Checks if validate_cnpj() outputs the correct message when it receives a valid CNPJ string.
**test_invalid_validate_cnpj():** Checks if validate_cnpj() correctly outputs an invalid message when the input CNPJ is invalid.


## Exercise 1: Validate CNPJ format
File name: **ex1_function.py** \
Function name: **check_cnpj_string()cnpj** - receives a **cnpj** string as input, returns if the CNPJ format is valid or invalid.

Exercise 1 solution involved creating an algorithm to run through each CNPJ string passed as parameter, checking for possible inconsistencies when compared to two possible expected formats:

Formatted CNPJ string: "xx.xxx.xxx/xxxx-xx"\
Number only CNPJ string: "xxxxxxxxxxxxxx"\
Where **x** must be a valid number between 0-9.

These are the conditions and the algorithm checks for:
### String Size
There are only two accepted string sizes - 18 characters for formatted CNPJ strings and 14 characters for numbers only CNPJ strings. 
### Formatted CNPJ string punctuation
For formatted CNPJ strings, checks if all correct punctuation characters are on their correct positions.
### Formatted CNPJ string contains only numbers as their digits
For formatted CNPJ strings, checks if all digits are numbers
### Number only CNPJ string contains only numbers as their digits
Checks if a number only CNPJ string contains only numbers.

If the string passes all inconsistency tests, it is correctly formatted.

## Exercise 2: Validate CNPJ digits
File name: **ex2_function.py**\
Functions: 
**format_cnpj(cnpj)** - receives a **cnpj** string as input. Outputs a list of integers based on input string.\
**generate_validation_digit(cnpj, digit_number)** - receives a **cnpj** integer list and a **digit_number** informing what validation digit should be generated. Outputs integer with generated validation number.\
**validate_cnpj(cnpj)** - receives a **cnpj** string as input. Outputs a message informing if it is a valid cnpj string based on its validation digits.

Exercise 2 solution involved utilizing an algorithm to generate validation digits for a given CNPJ string and compare the generated digits with the actual validation digits from the input CNPJ string. The **validate_cnpj** function invokes **generate_validation_digit** to generate the two validation digits that are the last two digits from a CNPJ. Compares the generated validation digits with the actual input validation digits. If they are the same, outputs a message that the CNPJ is valid. Otherwise, outputs a message that the CNPJ is invalid.

The algorithm used to generate the validation digits is obtained from a [Modulo-11](https://pt.wikipedia.org/wiki/D%C3%ADgito_verificador#M%C3%B3dulo_11) operation.

