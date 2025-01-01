@echo off
:: Define the base directory for your repository
set BASE_DIR=new-york-taxi-demo

:: Create the base directory
mkdir %BASE_DIR%
cd %BASE_DIR%

:: Create folders
mkdir .devcontainer
mkdir data
mkdir notebooks
mkdir src
mkdir tests

:: Create placeholder files in each folder
:: .devcontainer
echo { > .devcontainer\devcontainer.json
echo    "name": "New York Taxi Demo DevContainer", >> .devcontainer\devcontainer.json
echo    "dockerFile": "./Dockerfile", >> .devcontainer\devcontainer.json
echo    "settings": { "python.pythonPath": "/usr/bin/python3" } >> .devcontainer\devcontainer.json
echo } >> .devcontainer\devcontainer.json

:: data
echo This folder contains raw and processed data. > data\README.md

:: notebooks
echo This folder contains exploratory and analysis notebooks. > notebooks\README.md

:: src
echo # __init__.py placeholder for src folder > src\__init__.py
echo def placeholder_function(): >> src\data_preprocessing.py
echo     return "This is a placeholder." >> src\data_preprocessing.py

:: tests
echo # __init__.py placeholder for tests folder > tests\__init__.py
echo def test_placeholder(): >> tests\test_data_preprocessing.py
echo     assert True >> tests\test_data_preprocessing.py

:: Create root-level files
echo # New York Taxi Demo > README.md
echo *.pyc > .gitignore
echo __pycache__/ >> .gitignore
echo .venv/ >> .gitignore

echo [project] > pyproject.toml
echo name = "new-york-taxi-demo" >> pyproject.toml
echo version = "0.1.0" >> pyproject.toml
echo requires-python = ">=3.11" >> pyproject.toml
echo dependencies = [ >> pyproject.toml
echo "pandas==2.2.2", >> pyproject.toml
echo "numpy==1.26.4", >> pyproject.toml
echo "scikit-learn==1.4.0", >> pyproject.toml
echo "mlflow==2.16.0" >> pyproject.toml
echo ] >> pyproject.toml

:: Development dependencies
echo pytest >= 7.5.0 > requirements-dev.txt
echo black >= 23.9.1 >> requirements-dev.txt
echo flake8 >= 6.1.0 >> requirements-dev.txt

:: Lockfile placeholder
echo This is a placeholder for uv.lock. > uv.lock

echo Done!