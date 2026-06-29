class GeneradorVista:
    def mostrar_menu(self):
        print("\n=========================================")
        print("    GENERADOR SEGURO DE CONTRASEÑAS      ")
        print("=========================================")
        print("  [1] Generar contraseña")
        print("  [2] Ver historial de contraseñas")
        print("  [3] Salir")
        print("-----------------------------------------")
        
        # VARIABLE DE ENTRADA: opción del menú principal
        opcion = input("  Selecciona una opción: ").strip()
        return opcion

    def mostrar_formulario(self):
        print("\n--- Configurar nueva contraseña ---")

        # VARIABLES DE ENTRADA (Capturan lo que el usuario digita en el teclado)
        longitud = int(input("1. ¿De cuántos caracteres quieres tu contraseña?: "))
        
        # OPERADORES DE COMPARACIÓN (==): convierten s/n a True/False
        incluir_mayus = input("2. ¿Incluir letras MAYÚSCULAS? (s/n): ").lower() == 's'
        incluir_num   = input("3. ¿Incluir números? (s/n): ").lower() == 's'
        incluir_esp   = input("4. ¿Incluir símbolos especiales? (s/n): ").lower() == 's'
        
        return longitud, incluir_mayus, incluir_num, incluir_esp

    def mostrar_contrasena(self, password):
        # VARIABLE DE SALIDA: muestra el resultado en pantalla
        print("\n-----------------------------------------")
        print(f"  Tu contraseña generada es: {password}")
        print("-----------------------------------------")
        print("  [C] Copiar al portapapeles")
        print("  [Enter] Continuar sin copiar")
        
        accion = input("  Opción: ").strip().lower()
        return accion == 'c'

    def confirmar_copiado(self):
        print("¡Contraseña copiada al portapapeles!")

    def mostrar_historial(self, historial):
        # ---------------------------------------------------------------
        # Recorre la LISTA de TUPLAS y muestra cada registro numerado.
        # Usa un bucle FOR con enumerate() para obtener índice y valor.
        # ---------------------------------------------------------------
        print("\n=========================================")
        print("       HISTORIAL DE CONTRASEÑAS          ")
        print("=========================================")

        if len(historial) == 0:
            print("  (Aún no has generado ninguna contraseña)")
        else:
            # BUCLE FOR: itera sobre cada TUPLA del historial
            for indice, registro in enumerate(historial):
                # Desempaquetamos la TUPLA en sus 5 variables
                contrasena, longitud, mayus, nums, esp = registro

                # DICCIONARIO: resume la configuración de forma legible
                config = {
                    "Longitud"   : longitud,
                    "Mayúsculas" : "Sí" if mayus else "No",
                    "Números"    : "Sí" if nums  else "No",
                    "Especiales" : "Sí" if esp   else "No"
                }

                print(f"\n  #{indice + 1}  {contrasena}")

                # BUCLE FOR sobre el DICCIONARIO para mostrar cada clave-valor
                for clave, valor in config.items():
                    print(f"       {clave}: {valor}")

        print("\n=========================================")
        input("  Presiona Enter para volver al menú...")

    def mostrar_error(self, mensaje):
        print(f"\n  [ERROR] {mensaje}")

    def mostrar_adios(self):
        print("\n  ¡Hasta luego! Recuerda usar contraseñas fuertes.\n")