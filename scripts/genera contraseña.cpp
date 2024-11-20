#include <iostream>
#include <string>
#include <cstdlib>  // Para rand() y srand()
#include <ctime>    // Para time()

std::string generarContrasenaSegura() {
    const int longitud = 12; // Longitud m�nima de la contrase�a
    const std::string mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const std::string minusculas = "abcdefghijklmnopqrstuvwxyz";
    const std::string numeros = "0123456789";
    const std::string especiales = "!@#$%^&*()-_=+[]{}|\\;:'\",.<>/?~";

    std::string contrasena;
    contrasena += mayusculas[rand() % mayusculas.size()]; // Al menos una may�scula
    contrasena += minusculas[rand() % minusculas.size()]; // Al menos una min�scula
    contrasena += numeros[rand() % numeros.size()];       // Al menos un n�mero
    contrasena += especiales[rand() % especiales.size()]; // Al menos un car�cter especial

    // Rellenar el resto de la contrase�a de manera aleatoria
    const std::string todos = mayusculas + minusculas + numeros + especiales;
    while (contrasena.size() < longitud) {
        char nuevoCaracter = todos[rand() % todos.size()];

        // Verificar si hay m�s de dos caracteres iguales consecutivos
        if (contrasena.size() > 1) {
            char penultimoCaracter = contrasena[contrasena.size() - 1];
            char antepenultimoCaracter = contrasena[contrasena.size() - 2];
            if (nuevoCaracter == penultimoCaracter && nuevoCaracter == antepenultimoCaracter) {
                continue; // Salta si es el tercer car�cter igual consecutivo
            }
        }

        contrasena += nuevoCaracter;
    }

    return contrasena;
}

int main() {
    srand(time(0)); // Inicializar la semilla de aleatoriedad

    std::string contrasenaSegura = generarContrasenaSegura();
    std::cout << "Contrase�a segura generada: " << contrasenaSegura << std::endl;

    return 0;
}

