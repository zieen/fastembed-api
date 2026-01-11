#!/bin/bash

# Change to the script's directory
cd "$(dirname "$0")"

if [ ! -f "service.pid" ]; then
    echo "Error: service.pid not found. Is the service running?"
    exit 1
fi

PID=$(cat service.pid)

if ps -p $PID > /dev/null; then
    echo "Stopping service (PID: $PID)..."
    kill $PID
    rm service.pid
    echo "Service stopped."
else
    echo "Process $PID not found. Removing stale pid file."
    rm service.pid
fi
