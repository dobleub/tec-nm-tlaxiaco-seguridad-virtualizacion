#include <iostream>
#include <string>
#include <cctype>

bool esSegura(const std::string& contrasena) {
    if (contrasena.length() < 8) {
        return false;
    }

    bool tieneMayuscula = false, tieneMinuscula = false;
    bool tieneNumero = false, tieneEspecial = false;
    
    for (size_t i = 0; i < contrasena.length(); ++i) {
        if (isspace(contrasena[i])) {
            return false;
        }
        if (isupper(contrasena[i])) {
            tieneMayuscula = true;
        }
        if (islower(contrasena[i])) {
            tieneMinuscula = true;
        }
        if (isdigit(contrasena[i])) {
            tieneNumero = true;
        }
        if (ispunct(contrasena[i])) {
            tieneEspecial = true;
        }
       
        if (i > 1 && contrasena[i] == contrasena[i-1] && contrasena[i] == contrasena[i-2]) {
            return false;
        }
    }

    return tieneMayuscula && tieneMinuscula && tieneNumero && tieneEspecial;
}

int main() {
    std::string contrasena;

    std::cout << "Ingrese una contraseña: ";
    std::getline(std::cin, contrasena);

    if (esSegura(contrasena)) {
        std::cout << "La contraseña es segura.\n";
    } else {
        std::cout << "La contraseña no es segura.\n";
    }

    return 0;
}

