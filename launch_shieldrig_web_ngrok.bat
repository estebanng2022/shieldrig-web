@echo off
title 🚀 ShieldRig Web Fullstack Launcher

echo 🛠️ Activando entorno virtual...
cd /d C:\ShieldRig_web
call venv\Scripts\activate.bat

echo 🔥 Lanzando backend FastAPI...
start "Backend (FastAPI)" cmd /k "cd backend && uvicorn main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 2 >nul

echo 🌐 Iniciando túnel Ngrok...
start "Ngrok Tunnel" cmd /k "C:\Users\engtr\ngrok\ngrok.exe http 8000 --domain=estebansandbox.ngrok.io"

echo 🧪 Iniciando frontend (Vite + React)...
start "Frontend (Vite)" cmd /k "cd frontend && npm run dev"

echo ✅ Todo lanzado. ¡Éxito total!
pause
