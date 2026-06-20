```mermaid
graph TD
    A([Inicio: generar_password]) --> B[Cargar caracteres_disponibles con minúsculas]
    
    B --> C{¿incluir_mayusculas?}
    C -- Sí --> D[Sumar letras MAYÚSCULAS]
    C -- No --> E{¿incluir_numeros?}
    
    D --> E
    E -- Sí --> F[Sumar números/dígitos]
    E -- No --> G{¿incluir_especiales?}
    
    F --> G
    G -- Sí --> H[Sumar caracteres especiales]
    G -- No --> I[Inicializar contrasena_final = ""]
    
    H --> I
    I --> J[Bucle FOR: Desde i = 0 hasta longitud]
    
    J --> K{¿Terminó el ciclo?}
    K -- No --> L[Elegir carácter aleatorio con secrets.choice]
    L --> M[Concatenar: contrasena_final + caracter]
    M --> J
    
    K -- Sí --> N[Retornar contrasena_final]
    N --> O([Fin del Proceso])