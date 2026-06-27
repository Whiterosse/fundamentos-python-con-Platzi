# 📓 REPORTE DE AVANCE Y RETOS DE ENTRADA EN ESCENA

## DIA 26 JUNIO 2026

**Ruta Crítica:** Fase 1 - Finalización Curso 2 / Transición a Código Activo
**Fecha de Sincronización:** 26/06/2026

---

## 🛠️ Resumen Conceptual del Día

### 📌 Control de Errores (`try`, `except`, `finally`)
Mecanismo de seguridad que evita que el servidor colapse ante fallos previstos (datos corruptos, ingresos inválidos del usuario o fallos de cálculo).
*   `try`: Código propenso a fallas.
*   `except`: Plan de contingencia ante un error específico.
*   `finally`: Bloque de ejecución obligatoria (limpieza de recursos).

### 📂 Administrador de Contexto (`with open`)
Herramienta óptima para la manipulación de archivos locales. Garantiza la apertura y el cierre automático del flujo de datos, previniendo fugas de memoria en el backend.

---

## 🚀 Laboratorio de Pruebas: 3 Retos para "Entrar en Escena"

Aplica la metodología activa: intenta resolverlos usando la lógica y buscando en la documentación o clases solo lo necesario[cite: 1].

### 🛠️ Reto 1: El Validador de ID de Clientes (Nivel: Inicial)
*   **Problema:** Estás creando un sistema donde el usuario debe ingresar su ID de cliente para consultar su suscripción. Si el usuario ingresa letras en lugar de números, el sistema no debe romperse.
*   **Tu Misión:** Escribe un programa con un bucle `while` infinito que pida el ID (solo números). Usa `try/except` con `ValueError` para atrapar el error si ingresa texto. Si ingresa el número correctamente, rompe el bucle con `break` y muestra un mensaje de éxito.

### 🛠️ Reto 2: El Generador de Reportes de Ventas (Nivel: Intermedio)
*   **Problema:** Necesitas registrar de forma persistente las ventas del día en un archivo de texto llamado `ventas_diarias.txt`.
*   **Tu Misión:** 
    1. Usa `with open` en modo escritura (`"w"`) para crear el archivo y escribir tres líneas, cada una con el formato: `Plataforma - Precio` (ej. `Netflix - 15000`).
    2. Luego, usa `with open` en modo lectura (`"r"`) para abrir ese mismo archivo, leer su contenido línea por línea y mostrarlo en la terminal con un formato elegante.

### 🛠️ Reto 3: El Filtro de Seguridad "Anti-Bugs" (Nivel: Avanzado Backend)
*   **Problema:** Tienes que leer un archivo de configuración esencial para el sistema llamado `config.txt`. Si el archivo no existe en el servidor, todo el backend fallará.
*   **Tu Misión:** Diseña un script que intente abrir `config.txt` usando `with open`. Envuelve todo el proceso en un bloque `try/except`. Si el archivo no existe, captura la excepción `FileNotFoundError` e imprime un mensaje de alerta crítico en pantalla. Añade un bloque `finally` que imprima `"Verificación del sistema completada"`.