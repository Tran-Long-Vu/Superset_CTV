#!/bin/bash

# Check if any process is running on port 3000
PID=$(lsof -t -i :3000)

if [ -z "$PID" ]; then
    echo "No process found running on port 3000"
else
    # Kill the process running on port 3000
    echo "Killing process $PID running on port 3000"
    kill "$PID"
fi
