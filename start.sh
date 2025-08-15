#!/bin/bash

cd ~/server || exit

# Start Flask API
python3 control_api.py > api.log 2>&1 &

# Start static file server for frontend
python3 -m http.server 5500 > frontend.log 2>&1 &

echo "Servers started."
echo "Flask API log: ~/server/api.log"
echo "Frontend log: ~/server/frontend.log"
