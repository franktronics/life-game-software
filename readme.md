# Life game software

## Installation
- Init the virtual environment
    ```bash
    python<version> -m venv <virtual-environment-name>
    ```
    For example:
    ```bash
    python3 -m venv venv
    ```
- Activate the virtual environment
    ```bash
    source <virtual-environment-name>/bin/activate # Linux
    <virtual-environment-name>\Scripts\activate # Windows
    ```
    For example:
    ```bash
    source venv/bin/activate # Linux
    venv\Scripts\activate # Windows
    ```
- Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
## Run the software
- Run the software
    ```bash
    python main.py
    ```

## Requirements

```bash
numpy==2.2.3
PyQt5==5.15.11
PyQt5-Qt5==5.15.16
PyQt5_sip==12.17.0
```