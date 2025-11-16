@echo off
REM FLUX Prompt Generator - Start Script for Windows

echo Starting FLUX Prompt Generator...

REM Check if node_modules exists
if not exist "node_modules\" (
    echo Installing frontend dependencies...
    call npm install
)

REM Check if Python virtual environment exists
if not exist "backend\venv\" (
    echo Creating Python virtual environment...
    cd backend
    python -m venv venv
    call venv\Scripts\activate
    echo Installing backend dependencies...
    pip install -r requirements.txt
    cd ..
) else (
    echo Activating Python virtual environment...
    call backend\venv\Scripts\activate
)

REM Start backend in new window
echo Starting backend server...
start "Backend Server" cmd /k "cd backend && python app.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak

REM Start frontend
echo Starting frontend development server...
npm run dev
