# NoTraffic - Python Library For Traffic Analytics

## Requirements

- [Python](https://www.python.org/downloads/) >= 3.6

## Installation

```shell
    cd <favorite repo directory>
    git clone git@github.com:blittooy/NoTraffic.git <custom folder name or leave blank>
    cd <custom folder name or NoTraffic>
    pip install . --upgrade
```
If you have installed on your computer **both** Python 2.7 and Python 3.x (default on macOS), you need to use:
```shell
    pip3 install . --upgrade
```
instead of:
```shell
    pip install . --upgrade
```

## Upgrade

At each new [release](https://github.com/ecorithm/NoTraffic/releases), in order to update the core package globally, it is necessary to re-run:
```shell
    pip install . --upgrade
```

## Folder Structure

```shell
NoTraffic                 # → Root of the PyRithm Repo

├── NoTraffic/            # → Root of the pyrithm package
│   ├── __init__.py     # → Init file of the pyrithm package. Sets the package version
│   └── traffic_lib/        # → Folder containing the shared python library
├── requirements.txt    # → Contains the list of all packages required to run the entire library
├── scripts/            # → Folder containing scripts executable from the command line
├── tests/              # → Folder containing tests of the pyrithm package
├── setup.cfg           # → Contains the configuration for the entire package
├── setup.py            # → Package and dependencies installer

```

## Conventions

Type | Default
--- | ---
Date string format | `%Y-%m-%d %H:%M`
Plotting library | [Matplotlib 2.x](http://matplotlib.org/)
