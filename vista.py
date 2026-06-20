class GeneradorVista:
    def mostrar_menu(self):
        print("\n=========================================")
        print("    GENERADOR SEGURO DE CONTRASEÑAS      ")
        print("=========================================")
        
        # -----------------------------------------------------------------
        # VARIABLES DE ENTRADA (Capturan lo que el usuario digita en el teclado)
        # -----------------------------------------------------------------
        longitud = int(input("1. ¿De cuántos caracteres quieres tu contraseña?: "))
        
        # OPERADORES DE COMPARACIÓN (==): Comparan si lo ingresado es igual a 's' 
        # para guardar un valor Verdadero (True) o Falso (False)
        incluir_mayus = input("2. ¿Quieres incluir letras MAYÚSCULAS? (s/n): ").lower() == 's'
        incluir_num = input("3. ¿Quieres incluir números? (s/n): ").lower() == 's'
        incluir_esp = input("4. ¿Quieres incluir símbolos especiales? (s/n): ").lower() == 's'
        
        # Retornamos todas las variables que ingresó el usuario
        return longitud, incluir_mayus, incluir_num, incluir_esp

    def mostrar_contrasena(self, password):
        # -----------------------------------------------------------------
        # VARIABLE DE SALIDA (Muestra el string final procesado en la pantalla)
        # -----------------------------------------------------------------
        print("\n-----------------------------------------")
        print(f" -> Tu contraseña generada es: {password}")
        print("-----------------------------------------")

    def mostrar_error(self, mensaje):
        print(f"\n[ERROR] {mensaje}")