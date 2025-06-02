#!/bin/bash

# Activate Python virtual environment for the automated-garden project

mkdir /tmp/testpsycopg2
cd /tmp/testpsycopg2
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt