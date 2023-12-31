#!/bin/bash
echo "****************************************"
echo " Setting up Capstone Environment"
echo "****************************************"

echo "Installing Python 3.8 Virtual Environment"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3.8-venv

echo "Making Python 3.8 the default..."
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

echo "Checking the Python version..."
python3 --version

echo "Creating a Python virtual environment"
python3 -m venv ~/backend-pics-venv


echo "Installing Python depenencies..."
source ~/backend-pics-venv/bin/activate && python3 -m pip install --upgrade pip wheel
source ~/


echo "****************************************"
echo " Capstone Environment Setup Complete"
echo "****************************************"
echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""
