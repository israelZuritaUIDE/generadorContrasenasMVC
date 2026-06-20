### Diagrama de Flujo del Main (Punto de Entrada)

```mermaid
graph TD
    A([Inicio del Sistema]) --> B[Importar GeneradorControlador]
    B --> C[Crear instancia: programa = GeneradorControlador]
    C --> D[Ejecutar: programa.iniciar]
    D --> E[Traspasar control al Controlador]
    E --> F([Fin del Sistema / Cierre del Programa])