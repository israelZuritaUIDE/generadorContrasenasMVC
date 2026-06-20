# ==========================================
# LIBRERÍAS DE PYTHON
# ==========================================
import string   # Nos da listas de letras, números y símbolos prehechos
import secrets  # Nos ayuda a elegir caracteres de forma aleatoria y segura

class GeneradorModelo:
    def __init__(self):
        pass

    def generar_password(self, longitud, incluir_mayusculas, incluir_numeros, incluir_especiales):
        # -----------------------------------------------------------------
        # VARIABLES DE ENTRADA (Parámetros que recibe el método del controlador)
        # longitud, incluir_mayusculas, incluir_numeros, incluir_especiales
        # -----------------------------------------------------------------

        caracteres_disponibles = string.ascii_lowercase
        
        # ESTRUCTURAS DE DECISIÓN (Condicionales Simples 'if')
        if incluir_mayusculas:
            caracteres_disponibles = caracteres_disponibles + string.ascii_uppercase
            
        if incluir_numeros:
            caracteres_disponibles = caracteres_disponibles + string.digits
            
        if incluir_especiales:
            caracteres_disponibles = caracteres_disponibles + string.punctuation

        # VARIABLE DE SALIDA: Aquí se irá armando el resultado final
        contrasena_final = ""
        
        # ESTRUCTURA REPETITIVA (Bucle 'for' que se repite según la longitud pedida)
        for i in range(longitud):
            # Usamos la librería 'secrets' para tomar un carácter al azar de "caracteres_disponibles"
            caracter_aleatorio = secrets.choice(caracteres_disponibles)
            
            # Vamos acumulando el carácter en nuestra variable de salida
            contrasena_final = contrasena_final + caracter_aleatorio
            
        # Retornamos la VARIABLE DE SALIDA
        return contrasena_final