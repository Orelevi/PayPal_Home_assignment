#!/bin/bash

# Step 1: Pull the latest changes from the repository
git clone https://github.com/orelevi/PayPal_Home_assignment.git

# Step 2: Change to the project directory
cd PayPal_Home_assignment

# Step 3: Run docker-compose to build and start the containers
docker-compose up --build

