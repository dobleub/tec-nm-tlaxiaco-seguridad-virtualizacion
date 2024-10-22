import random
import string
import os

def generar_contraseña_segura():
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiales = "!@#$%^&*()-_=+[]{}|\\;:'\",.<>/?~`"
    
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiales)
    ]
    
    while len(contraseña) < 10:
        contraseña.append(random.choice(mayusculas + minusculas + numeros + especiales))
    
    random.shuffle(contraseña)
    
    contraseña = ''.join(contraseña)
    
    return contraseña

def generar_contraseña_insegura():
    longitud = random.randint(8, 10)
    caracteres = string.ascii_letters + string.digits
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    if random.choice([True, False]):
        contraseña += random.choice("!@#$%^&*()-_=+[]{}|\\;:'\",.<>/?~`")
    
    return contraseña

def es_segura(contraseña):
    if len(contraseña) < 10:
        return False
    
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_minuscula = any(c.islower() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    tiene_especial = any(c in "!@#$%^&*()-_=+[]{}|\\;:'\",.<>/?~`" for c in contraseña)
    
    for i in range(len(contraseña) - 2):
        if contraseña[i] == contraseña[i+1] == contraseña[i+2]:
            return False
    
    if ' ' in contraseña:
        return False
    
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    
    return False

# Verificar si el archivo existe para leer el estado
estado_archivo = "estado_alternar.txt"
if os.path.exists(estado_archivo):
    with open(estado_archivo, "r") as file:
        alternar = file.read().strip() == "True"
else:
    alternar = True  # Por defecto, empezamos con una contraseña segura

# Generar contraseña según el estado actual
if alternar:
    contraseña = generar_contraseña_segura()
else:
    contraseña = generar_contraseña_insegura()

# Guardar el estado alternado para la próxima ejecución
with open(estado_archivo, "w") as file:
    file.write(str(not alternar))

print(f"Contraseña generada: {contraseña}")
if es_segura(contraseña):
    print("La contraseña es segura.")
else:
    print("La contraseña no es segura.")
