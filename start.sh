#!/usr/bin/bash

# start script, run me every time you want to start the flask app locally
# only for development

python3 modules/setup.py

wait

echo "setup complete"

python3 modules/main.py