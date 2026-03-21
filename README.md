# 🚀 Repositorio Base: Programación Orientada a Objetos

Bienvenidos al repositorio oficial de la asignatura de **Programación Orientada a Objetos** en CESUN Universidad. 

A partir de este segundo bloque, dejaremos de programar scripts básicos y comenzaremos a escribir software bajo los estándares reales de la industria. Este proyecto está configurado como un entorno profesional que utiliza **Integración Continua (CI)**, análisis estático de código y pruebas automatizadas.

---

## 📋 Requisitos Previos
* Python 3.10 o superior instalado en tu sistema.
* Git instalado y configurado.
* Editor de código recomendado: Visual Studio Code (VS Code).

---

## 🛠️ Paso 1: Configurar el Entorno Virtual (VENV)
En la industria, nunca instalamos librerías directamente en nuestra computadora de forma global. Siempre creamos un entorno virtual aislado para cada proyecto.

1. Abre la terminal en Visual Studio Code asegurándote de estar en la carpeta raíz del proyecto.
2. Crea el entorno virtual ejecutando:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   * **En Windows (Command Prompt o PowerShell):**
     ```bash
     .\venv\Scripts\activate
     ```
   * **En macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```
*(Sabrás que lo hiciste correctamente si en tu terminal aparece la palabra `(venv)` al inicio de la línea de comandos).*

---

## 📦 Paso 2: Instalación de Dependencias
Separamos las librerías que el programa necesita para funcionar (`requirements.txt`) de las herramientas que nosotros necesitamos para auditar y mejorar el código (`requirements-dev.txt`).

1. Con tu entorno virtual activo, instala las herramientas del "policía de código":
   ```bash
   pip install -r requirements-dev.txt
   ```
   *(Esto descargará automáticamente herramientas clave como Black, Ruff, Mypy, Pytest y Pre-commit).*

---

## 🛡️ Paso 3: Activar al "Guardia Local" (Pre-commit)
Para evitar que subas a GitHub código con errores de formato, variables sin usar o tipos de datos incorrectos, configuramos un guardia local. Las reglas estrictas de este guardia viven centralizadas en el archivo `pyproject.toml`.

Para instalar este guardia en tu computadora, ejecuta una sola vez este comando:
```bash
pre-commit install
```
A partir de hoy, cada vez que intentes guardar tus avances (`git commit`), tu computadora pausará el proceso y ejecutará los siguientes exámenes:
1. **Black:** Formateará tu código (ajustará espacios, comillas y saltos de línea a 100 caracteres).
2. **Ruff:** Revisará la calidad y aplicará el estándar PEP8.
3. **Mypy:** Verificará que tu Tipado Estático (`-> str`, `: int`) sea lógico y consistente.
4. **Pytest:** Correrá tus pruebas unitarias de la carpeta `tests/`.

---

## ☁️ Paso 4: La Integración Continua (GitHub Actions)
Si tu código aprueba los exámenes locales y logras hacer `git push`, viajará a GitHub. Allí, nuestro servidor en la nube (cuyas reglas están en `.github/workflows/calificador-ci.yml`) levantará un entorno virtual en blanco y volverá a calificarte de forma imparcial.

* ✅ **Palomita Verde:** Tu código cumple los estándares corporativos. Tienes 100 en la entrega.
* ❌ **Cruz Roja:** Tu código falló. Revisa los detalles (Logs) en GitHub, corrige el error en tu computadora y vuelve a hacer push.

---

## 🔄 Flujo de Trabajo Obligatorio (Pull Requests)
**ATENCIÓN: La rama `main` de este repositorio está bloqueada por seguridad.** No puedes subir código directamente a ella. Todo ingeniero de software debe seguir este flujo:

1. **Aísla tu trabajo:** Crea una rama nueva para tu funcionalidad o tarea del día:
   ```bash
   git checkout -b feature/nueva-conexion-bd
   ```
2. **Programa, aplica S.O.L.I.D. y guarda:**
   ```bash
   git add .
   git commit -m "Agrega el patrón Singleton para la base de datos"
   ```
3. **Sube tu rama secundaria a GitHub:**
   ```bash
   git push origin feature/nueva-conexion-bd
   ```
4. **Crea el Pull Request (PR):** Entra a GitHub.com y haz clic en "Compare & pull request".
5. **Espera la evaluación:** GitHub Actions ejecutará los exámenes sobre tu PR.
   * Si pasa (✅), el botón verde de "Merge" se desbloqueará y podrás integrar tu código a `main`.
   * Si falla (❌), el botón estará bloqueado. Corrige tu código localmente, haz otro commit y los exámenes se volverán a correr solos.

---

## 🚑 Solución de Problemas Frecuentes

**1. "El examen pasó en mi computadora, pero falló en GitHub."**
El guardia local es rápido y solo revisa los archivos que acabas de modificar. GitHub revisa *todo* el proyecto desde cero. Para obligar a tu computadora a hacer un simulacro exacto del examen de GitHub, ejecuta:
```bash
pre-commit run --all-files
```

**2. "Pytest marca un `ModuleNotFoundError` o no encuentra mi código."**
Asegúrate de ejecutar Pytest como un módulo de Python para que reconozca correctamente las carpetas raíz de tu proyecto. En lugar de escribir solo `pytest`, utiliza:
```bash
python -m pytest
```

**3. "Mypy falla en GitHub diciendo que no hay archivos `.py` (Exit code 2)."**
Tu repositorio necesita tener al menos un archivo de Python para que Mypy lo califique. Asegúrate de haber creado y subido el archivo `main.py` base en tu primer commit.

---
*Diseñado para formar a la próxima generación de Ingenieros de Software.* 🎓