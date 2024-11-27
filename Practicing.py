# Haciendo un programa en el que insertes un caracter y te lo devuelva con +1

def get_char():
    return input("Introduce un carácter: ")[0] 

# Obtener el primer carácter de la entrada
def main():
    char = get_char
    next_char =chr(ord(char)+ 1)
    print(f"El siguiente carácter es: {next_char}")

if __name__ == "__main__":
    main()