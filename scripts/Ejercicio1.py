import re

def is_password_secure(password):
    # Verificar la longitud mínima
    if len(password) < 8:
        return False

    # Verificar la presencia de al menos una letra mayúscula
    if not re.search(r'[A-Z]', password):
        return False

    # Verificar la presencia de al menos una letra minúscula
    if not re.search(r'[a-z]', password):
        return False

    # Verificar la presencia de al menos un número
    if not re.search(r'\d', password):
        return False

    # Verificar la presencia de al menos un carácter especial
    if not re.search(r'[!@#$%^&*()\-\_=+\[\]{}|;:\'",.<>/?~`]', password):
        return False

    # Verificar la ausencia de espacios en blanco
    if ' ' in password:
        return False

    # Verificar que no haya más de 2 caracteres iguales consecutivos
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return False

    return True

def main():
    # Solicitar la contraseña al usuario
    password = input("Ingrese una contraseña: ")

    # Validar la contraseña
    if is_password_secure(password):
        print("La contraseña es segura.")
    else:
        print("La contraseña no es segura.")
if __name__ == "__main__":
    main()

    