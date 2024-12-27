# setup.bat - Para sistemas Windows
@echo off
ECHO === BATSEJ Open Finance - Script de Inicializacion ===
ECHO.

REM Verificar si Python está instalado
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Error: Python no esta instalado en este sistema.
    ECHO Por favor, instale Python 3.8 o superior desde https://www.python.org/downloads/
    ECHO.
    PAUSE
    EXIT /B 1
)

REM Verificar si el entorno virtual existe
IF NOT EXIST venv (
    ECHO Creando entorno virtual...
    python -m venv venv
) ELSE (
    ECHO Entorno virtual encontrado.
)

REM Activar entorno virtual
ECHO Activando entorno virtual...
CALL venv\Scripts\activate.bat



REM Instalar dependencias
ECHO Instalando dependencias...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Verificar la estructura del proyecto
IF NOT EXIST "data\database.sqlite" (
    ECHO Error: No se encuentra la base de datos.
    ECHO Por favor, verifica que el archivo database.sqlite este en BATSEJ_OPEN_FINANCE_S.A/data/
    PAUSE
    EXIT /B 1
)

ECHO.
ECHO === Instalacion completada ===
ECHO.
ECHO Para ejecutar el programa:
ECHO 1. El entorno virtual esta activado
ECHO 2. Ejecuta: python src/main.py
ECHO.

REM Preguntar si desea ejecutar el programa
SET /P EJECUTAR="¿Desea ejecutar el programa ahora? (S/N): "
IF /I "%EJECUTAR%"=="S" (
    ECHO.
    ECHO Ejecutando programa...
    python src/main.py
)

PAUSE
