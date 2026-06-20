# UNIVERSIDAD INTERNACIONAL DEL ECUADOR (UIDE)
**Ingeniería en Sistemas de la Información**

* **Actividad:** Selección del Programa a desarrollar / Generación de Diagramas funcionales y Arquitectura de Software
* **Modalidad:** Online
* **Estudiante:** Israel Zurita
* **Ciclo Académico:** 2026

---

## I. Análisis del Problema
* **Problema a resolver:** En la actualidad, los usuarios suelen utilizar contraseñas débiles o repetidas en múltiples plataformas, lo que compromete su seguridad informática.
* **Solución propuesta:** Desarrollar un software que permita crear contraseñas criptográficamente fuertes y aleatorias de forma rápida. El sistema no requerirá conexión a internet ni almacenará datos personales, garantizando total privacidad.

---

## II. Diseño Funcional
El sistema describe cómo el usuario interactúa con la aplicación para lograr su objetivo a través de los siguientes casos de uso principales:

1. **Configurar parámetros:** El usuario decide la longitud de la contraseña y si desea incluir mayúsculas, números o caracteres especiales.
2. **Generar contraseña:** El sistema procesa los parámetros y devuelve una cadena aleatoria.
3. **Copiar al portapapeles:** El usuario extrae la contraseña generada para usarla en otro sitio.

> **Nota:** Puedes revisar las capturas del *Diagrama de Flujo Funcional* dentro de la carpeta `generadorContrasenasMVC\diagramas` de este repositorio.

---

## III. Diseño de Arquitectura
Para este proyecto, la mejor arquitectura es el patrón **MVC (Modelo-Vista-Controlador)**. Es un modelo simple, escalable y separa perfectamente la pantalla (Vista) de la lógica matemática de generar la contraseña (Modelo).

### Componentes del Sistema:
* **Vista (UI):** La pantalla en consola donde el usuario interactúa, ve los menús, digita las opciones y observa el resultado.
* **Controlador:** Actúa como puente o intermediario. Detecta las acciones del usuario, lee las opciones seleccionadas y se las solicita al Modelo.
* **Modelo:** Es el "cerebro" del programa. Contiene los algoritmos de aleatoriedad. No conoce nada de la interfaz de usuario, solo recibe reglas básicas y devuelve un resultado de texto seguro.