## Contributing guide

## Setup virtual environment

- **Windows** :

    Use PowerShell as example.

    Create virtual environment:
    ```
    PY -{{cookiecutter.min_python_version}} -m virtualenv .venv
    ```

    Active the virtual environment:
    ```
    .venv\Scripts\activate.ps1
    ```
- **Linux** :

    Use Bash as example.

    Create virtual environment:
    ```
    python{{cookiecutter.min_python_version}} -m virtualenv .venv
    ```

    Active the virtual environment:
    ```
    .venv\Scripts\activate.ps1
    ```


After activing virtual environment, install depedencies as below:
```
pip install -e .[dev]
```