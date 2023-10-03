#!/bin/bash

# Step 1: Pull the latest changes from the repository
git pull

# Step 2: Change to the project directory
cd /path/to/your/project/directory

# Step 3: Run docker-compose to build and start the containers
docker-compose up --build
