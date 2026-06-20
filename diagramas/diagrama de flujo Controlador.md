### Diagrama de Flujo del Controlador (Validación y Control)

```mermaid
graph TD
    A([Inicio: main.py]) --> B[Instanciar Controlador]
    B --> C[Llamar a vista.mostrar_menu]
    C --> D[/Capturar: longitud, mayúsculas, números, símbolos/]
    D --> E{¿Longitud < 8?}
    E -- Sí --> F[Llamar a vista.mostrar_error]
    F --> G([Fin del Programa])
    E -- No --> H[Llamar a modelo.generar_password]
    H --> I[Recibir contraseña generada]
    I --> J[Llamar a vista.mostrar_contrasena]
    J --> G