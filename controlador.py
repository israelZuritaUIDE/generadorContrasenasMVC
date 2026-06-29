import pyperclip          # Librería para copiar al portapapeles
from modelo import GeneradorModelo
from vista  import GeneradorVista

class GeneradorControlador:
    def __init__(self):
        self.modelo = GeneradorModelo()
        self.vista  = GeneradorVista()

    def iniciar(self):
        # ---------------------------------------------------------------
        # ESTRUCTURA REPETITIVA: Bucle WHILE que mantiene el programa
        # corriendo hasta que el usuario elija salir (opción '3')
        # ---------------------------------------------------------------
        ejecutando = True

        while ejecutando:
            opcion = self.vista.mostrar_menu()

            # ESTRUCTURA DE DECISIÓN: dirige el flujo según la opción
            if opcion == '1':
                self._flujo_generar()

            elif opcion == '2':
                # Pedimos al modelo la LISTA de TUPLAS del historial
                historial = self.modelo.obtener_historial()
                self.vista.mostrar_historial(historial)

            elif opcion == '3':
                self.vista.mostrar_adios()
                ejecutando = False   # Condición de salida del WHILE

            else:
                self.vista.mostrar_error("Opción no válida. Elige 1, 2 o 3.")

    # ------------------------------------------------------------------
    # Método privado: contiene el flujo completo de generación
    # ------------------------------------------------------------------
    def _flujo_generar(self):
        # 1. Recibimos las VARIABLES DE ENTRADA desde la vista
        longitud, incluir_mayus, incluir_num, incluir_esp = self.vista.mostrar_formulario()

        # 2. ESTRUCTURA DE DECISIÓN: validación de longitud mínima
        #    OPERADOR DE COMPARACIÓN (<): longitud menor a 8
        if longitud < 8:
            self.vista.mostrar_error("La longitud mínima permitida es de 8 caracteres.")
            return

        # 3. Pedimos al modelo la VARIABLE DE SALIDA (contraseña)
        #    El modelo también registra la tupla en su historial interno
        resultado = self.modelo.generar_password(longitud, incluir_mayus, incluir_num, incluir_esp)

        # 4. Mostramos el resultado; la vista nos dice si el usuario quiere copiar
        desea_copiar = self.vista.mostrar_contrasena(resultado)

        # 5. ESTRUCTURA DE DECISIÓN: si el usuario pidió copiar
        if desea_copiar:
            pyperclip.copy(resultado)   # Copia el string al portapapeles del SO
            self.vista.confirmar_copiado()