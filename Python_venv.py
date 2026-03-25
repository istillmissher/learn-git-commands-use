#!/bin/bash
# Clean Python environment setup

# Create environment
python3 -m venv ~/python_env/venv
source ~/python_env/venv/bin/activate

# Upgrade pip and build tools
pip install --upgrade pip setuptools wheel

# Install main packages
pip install --upgrade numpy scipy pandas matplotlib seaborn scikit-learn jupyterlab \
flask fastapi django requests beautifulsoup4 uvicorn aiohttp \
click typer rich python-dotenv \
pytest coverage mypy black flake8 \
PyQt6 pillow pygame \
boto3 cryptography paramiko
