### Diagrama de Flujo de la Vista (Interfaz de Usuario)

```mermaid
graph TD
    A([Inicio: menú solicitado]) --> B[\Mostrar título: GENERADOR DE CONTRASEÑAS\]
    B --> C[\Pedir longitud de contraseña por teclado\]
    C --> D[\Preguntar si incluye MAYÚSCULAS s/n\]
    D --> E[\Preguntar si incluye números s/n\]
    E --> F[\Preguntar si incluye símbolos especiales s/n\]
    F --> G[Evaluar respuestas: convertir s/n a Verdadero o Falso]
    G --> H[Retornar valores al Controlador]
    H --> I([Fin del proceso de la Vista])