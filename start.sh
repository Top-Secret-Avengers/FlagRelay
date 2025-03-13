#!/usr/bin/bash

# start script, run me every time you want to start the flask app locally
# only for development

# python3 modules/setup.py

# wait

# echo "setup complete"

# above needs fixed unfortunately
docker build -t flagrelay .

docker container run -it --name flagrelay --rm -p 5000:5000 -e FLASK_APP=modules/main.py flagrelay