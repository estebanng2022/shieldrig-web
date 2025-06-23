@echo off
cd /d %~dp0
echo Starting ShieldRig Backend...
uvicorn main:app --reload --app-dir backend
pause
