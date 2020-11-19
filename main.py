
import ex2_function as vs
import ex1_function as fs
import fileinput
def main():
  for cnpj in fileinput.input():
    print("CNPJ String Input: " + cnpj)
    if(fs.check_cnpj_string(cnpj[:14]) == "CNPJ is correctly formatted."):
      print("Exercise 1: Validate CNPJ Format")
      print(fs.check_cnpj_string(cnpj[:14])) 
      print("Exercise 2: Validate CNPJ validation digits")
      print(vs.validate_cnpj(cnpj[:14]))
    else:
      print("Exercise 1: Validate CNPJ Format")
      print(fs.check_cnpj_string(cnpj[:14]))
    print("=================")
    
if __name__ == "__main__":
    main()

