import random

def generar_contrasena():
    caracteres = [chr(i) for i in range(33, 126)] 
    password = ''
    
    while len(password) < 15:
        caracter = random.choice(caracteres)
        if caracter not in password:
            password += caracter
    
    return password

print("Generada:", generar_contrasena())

