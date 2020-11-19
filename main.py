def check_cnpj_string(cnpj):
  # Checks string for size
  unformatted_cnpj = ""
  if(len(cnpj) == 18 or len(cnpj) == 14):
    # Checks if Formatted CNPJ entries are valid
    if(len(cnpj) == 18):
      # Checks formatted CNPJ punctuation
      if(cnpj[2] != "." or cnpj[6] != "." or cnpj[10] != "/" or cnpj[15] != "-"):
        return "Invalid formatted CNPJ: incorrect punctuation."
      # Creates an unformatted CNPJ from a formatted CNPJ.
      for i in cnpj:
        if ord(i) in range(48,58):
          unformatted_cnpj = unformatted_cnpj + i
      # Checks if all characters, aside from punctuation characters, are numbers.
      if(len(unformatted_cnpj) != 14):
        return "Invalid formatted CNPJ: incorrect characters;  all characters, aside from punctiation characters, must be numbers."
      else:
        return "CNPJ is correctly formatted"
    # For unformatted CNPJ entries, checks if all characters are numbers.
    for i in cnpj:
      if ord(i) not in range(48,58):
        return "Invalid formatted CNPJ: incorrect characters;  all characters must be numbers."
    # If cnpj contains only numbers, return success
    return "CNPJ is correctly formatted."
  # If cnpj entry does not have the correct length, it is not valid.
  else:
    return "Invalid CNPJ format: invalid number of characters."
def main():
  print(check_cnpj_string("02123683097531")) # correctly formatted
  print(check_cnpj_string("02123683d9753a")) # invalid character
  print(check_cnpj_string("021236830975")) # invalid size
  print(check_cnpj_string("02.123.683/0975-31")) # correctly formatted
  print(check_cnpj_string("02.123.683/0975-3a")) # invalid character
  print(check_cnpj_string("02~123=683`0975/31")) # invalid punctiation


if __name__ == "__main__":
    main()