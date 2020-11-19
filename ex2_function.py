# Returns CNPJ string as a list of integer representation of CNPJ digits.
def format_cnpj(cnpj):
  numbers_only_cnpj = ""
  int_cnpj_string = []
  if(len(cnpj) == 18 or len(cnpj) == 14):
    if(len(cnpj) == 14):
      numbers_only_cnpj = cnpj
    if(len(cnpj) == 18):
      # Transforms formatted CNPJ string into numbers-only CNPJ string.
      for i in cnpj:
          if ord(i) in range(48,58):
            numbers_only_cnpj = numbers_only_cnpj + i
    # Creates a list with integer representation of CNPJ digits.
    for i in numbers_only_cnpj:
      int_cnpj_string.append(int(i))
    # Returns the CNPJ integer list representation
    return int_cnpj_string
  # Returns an empty list when cnpj parameter is of invalid string size.
  else:
    return []


def generate_validation_digit(cnpj, digit_number):
  # Auxiliary Variables
  multipliers = [5,4,3,2,9,8,7,6,5,4,3,2]
  multiplied_numbers = []
  v_digit = 0
  # These conditions check if we are generating the first or second validation digit.
  # If we are generating the first digit, we check only the first 12 digits from cnpj string.
  # Otherwise, check 13 digits, including the first validation digit. 
  if(digit_number == 1):
    aux_cnpj = cnpj[:12]
  elif(digit_number == 2):
    aux_cnpj = cnpj[:13]
    # For the second digit we also need another number in our multipliers list
    multipliers = [6] + multipliers
  # Multiply each digit for its correspondent on multipliers[] list (without including the last two digits)
  for i in range(0, len(aux_cnpj)):
    multiplied_numbers.append(aux_cnpj[i] * multipliers[i])
  # Sums all multiplied numbers
  for i in multiplied_numbers:
    v_digit = v_digit + i
  # Takes the remainder of v_digit and 11. If remainder is less than 2, the first
  # validation digit is 0. Otherwise, it is 11 - remainder of the operation.
  if(v_digit % 11 < 2):
    v_digit = 0
  else:
    v_digit = 11 - (v_digit % 11)
  return v_digit

def validate_cnpj(cnpj):
  argument_cnpj = format_cnpj(cnpj)
  aux_cnpj = argument_cnpj[:]
  # Generates first validation digit
  v_digit = generate_validation_digit(argument_cnpj, 1)
  print(v_digit)
  # Puts created v_digit in first validation digit position on aux_cnpj
  aux_cnpj[12] = v_digit
  # Generates second validation digit
  v_digit = generate_validation_digit(aux_cnpj, 2)
  print(v_digit)
  # Puts created v_digit in second validation digit position on aux_cnpj
  aux_cnpj[13] = v_digit
  if(argument_cnpj is aux_cnpj):
    return "Valid CNPJ"
  else:
    return "Invalid CNPJ"

def main():
  print(validate_cnpj("11.222.333/0001-00"))

if __name__ == "__main__":
    main()
