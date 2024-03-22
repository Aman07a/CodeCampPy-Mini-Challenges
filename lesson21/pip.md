# Python Pip

## Installing Packages

### Installing Requests Package Globally with Python Pip

```bash
py -m pip install requests
```

### Installing the `python-dotenv` Package

```bash
py -m pip install python-dotenv
```

## Listing and Managing Packages

### List All Installed Python Packages & Versions

```bash
py -m pip list
```

| Package            | Version  |
| ------------------ | -------- |
| certifi            | 2024.2.2 |
| charset-normalizer | 3.3.2    |
| idna               | 3.6      |
| pip                | 24.0     |
| requests           | 2.31.0   |
| urllib3            | 2.2.1    |

### Listing Installed Python Packages

```bash
pip list
```

### Displaying Information about the `requests` Package

```bash
py -m pip show requests
```

### Uninstalling Requests Package Globally with Python Pip

```bash
py -m pip uninstall requests
```

## Managing Environments

### Creating a Python Virtual Environment with `venv`

```bash
py -m venv .venv
```

### Updating `pip` to the Latest Version

```bash
py -m pip install -U pip
```

## Managing Requirements

### Freezing Installed Python Packages to `requirements.txt`

```bash
py -m pip freeze > requirements.txt
```
