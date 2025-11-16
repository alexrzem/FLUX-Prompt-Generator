#!/bin/bash

# FLUX Prompt Generator - Start Script

echo "Starting FLUX Prompt Generator..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Check if Python virtual environment exists
if [ ! -d "backend/venv" ]; then
    echo "Creating Python virtual environment..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing backend dependencies..."
    pip install -r requirements.txt
    cd ..
else
    echo "Activating Python virtual environment..."
    source backend/venv/bin/activate
fi

# Start backend in background
echo "Starting backend server..."
cd backend
python app.py &
BACKEND_PID=$!
cd ..

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting frontend development server..."
npm run dev

# Cleanup on exit
trap "kill $BACKEND_PID" EXIT
