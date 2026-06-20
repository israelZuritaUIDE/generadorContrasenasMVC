# ==========================================
# ARCHIVO PRINCIPAL: main.py
# ==========================================

# IMPORTACIÓN: Traemos el Controlador que creamos
from generadorContrasenasMVC.Controlador.controlador import GeneradorControlador

if __name__ == "__main__":
    # PUNTO DE ENTRADA: Aquí arranca oficialmente el programa
    
    # 1. Creamos una VARIABLE de tipo Objeto basada en nuestra clase Controlador
    programa = GeneradorControlador()
    
    # 2. Ejecutamos el método que activa todo el flujo del MVC
    programa.iniciar()