##LIBRERIAS

import string   # Nos da listas de letras, números y símbolos prehechos
import secrets  # Nos ayuda a elegir caracteres de forma aleatoria y segura

class GeneradorModelo:
    def __init__(self):
        # ---------------------------------------------------------------
        # LISTA: Almacena el historial de contraseñas generadas en la sesión
        # Cada elemento es una TUPLA.
        # ---------------------------------------------------------------
        self.historial_contrasenas = []

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
            # Usamos la librería 'secrets' para tomar un carácter al azar
            caracter_aleatorio = secrets.choice(caracteres_disponibles)
            contrasena_final = contrasena_final + caracter_aleatorio

        # ---------------------------------------------------------------
        # TUPLA: Registra la configuración usada (es inmutable, no cambia)
        # Estructura: (contraseña, longitud, mayús, números, especiales)
        # ---------------------------------------------------------------
        registro = (contrasena_final, longitud, incluir_mayusculas, incluir_numeros, incluir_especiales)

        # LISTA: Agregamos la tupla al historial con .append()
        self.historial_contrasenas.append(registro)

        # Retornamos la VARIABLE DE SALIDA
        return contrasena_final
        # ---------------------------------------------------------------
    # Retorna la LISTA completa del historial para que el controlador
    # la pase a la vista. Cada elemento es una TUPLA de solo lectura.
    # ---------------------------------------------------------------

    def obtener_historial(self):
        return self.historial_contrasenas

    def limpiar_historial(self):
        # Reinicia la LISTA a vacía
        self.historial_contrasenas = []