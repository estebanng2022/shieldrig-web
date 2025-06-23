@echo off
REM ✅ Activar entorno virtual
call backend\venv\Scripts\activate.bat

REM 🚀 Iniciar el backend FastAPI
start "FastAPI Server" cmd /k uvicorn main:app --reload --app-dir backend

REM 🌐 Iniciar Ngrok desde ruta fija con dominio personalizado
start "Ngrok Tunnel" cmd /k "C:\Users\engtr\ngrok\ngrok.exe http 8000 --domain=estebansandbox.ngrok.io"
