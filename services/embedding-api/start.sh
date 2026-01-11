#!/bin/bash
set -e

# Change to the script's directory
cd "$(dirname "$0")"

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "Error: .venv virtual environment not found. Please run 'python3 -m venv .venv' and install requirements first."
    exit 1
fi

# Check if already running
if [ -f "service.pid" ]; then
    PID=$(cat service.pid)
    if ps -p $PID > /dev/null; then
        echo "Service is already running (PID: $PID)"
        exit 1
    else
        echo "Found stale pid file. Removing..."
        rm service.pid
    fi
fi

# Activate virtual environment
source .venv/bin/activate

# Start uvicorn in background
echo "Starting Embeddings API..."
nohup uvicorn src.main:app --host 0.0.0.0 --port 8000 > service.log 2>&1 &
PID=$!

# Save PID
echo $PID > service.pid

echo "Service started with PID: $PID"
echo "Logs are being written to service.log"
