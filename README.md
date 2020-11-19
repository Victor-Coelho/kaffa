# Kaffa - Pre-qualification Test Resolution
Author: Víctor Coelho
## How to Build and Run Exercises Solutions
## Exercise 1: Validate CNPJ format
File name: **ex1_function.py** \
Function name: **check_cnpj_string**

Exercise 1 solution involved creating an algorithm to run through each CNPJ string passed as parameter, checking for possible inconsistencies when compared to two possible expected formats:

Formatted CNPJ string: "xx.xxx.xxx/xxxx-xx"\
Number only CNPJ string: "xxxxxxxxxxxxxx"\
Where **x** must be a valid number between 0-9.

These are the conditions the algorithm checks for:
### String Size
There are only two accepted string sizes - 18 characters for formatted CNPJ strings and 14 characters for numbers only CNPJ strings. 
### Formatted CNPJ string punctuation
For formatted CNPJ strings, checks if all correct punctuation characters are on their correct positions.
### Formatted CNPJ string contains only numbers as their digits
For formatted CNPJ strings, checks if all digits are numbers
### Number only CNPJ string contains only numbers as their digits
Checks if a number only CNPJ string contains only numbers.

If the string passes all inconsistency tests, it is correctly formatted.

