from modelo import GeneradorModelo
from vista import GeneradorVista

class GeneradorControlador:
    def __init__(self):
        # Instanciamos los componentes (Lógica MVC)
        self.modelo = GeneradorModelo()
        self.vista = GeneradorVista()

    def iniciar(self):
        # 1. Recibimos las VARIABLES DE ENTRADA desde la vista
        longitud, incluir_mayus, incluir_num, incluir_esp = self.vista.mostrar_menu()
        
        # 2. ESTRUCTURA DE DECISIÓN (Condicional 'if' de validación)
        # OPERADOR DE COMPARACIÓN (<): Verifica si la longitud es menor a 8
        if longitud < 8:
            self.vista.mostrar_error("La longitud mínima permitida es de 8 caracteres.")
            return # Detiene el flujo del programa si no cumple la condición

        # 3. Mandamos las variables al modelo para obtener la VARIABLE DE SALIDA
        resultado = self.modelo.generar_password(longitud, incluir_mayus, incluir_num, incluir_esp)
        
        # 4. Enviamos la VARIABLE DE SALIDA a la vista para que la muestre
        self.vista.mostrar_contrasena(resultado)