# NoTraffic - Python Library For Stock Analytics

## Requirements

- [Python](https://www.python.org/downloads/) >= 3.6

## Installation

```shell
    cd <favorite repo directory>
    git clone git@github.com:blittooy/StockHelper.git <custom folder name or leave blank>
    cd <custom folder name or StockHelper>
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

At each new [release](https://github.com/ecorithm/StockHelper/releases), in order to update the core package globally, it is necessary to re-run:
```shell
    pip install . --upgrade
```

## Folder Structure

```shell
StockHelper                 # → Root of the PyRithm Repo

├── StockHelper/            # → Root of the pyrithm package
│   ├── __init__.py     # → Init file of the pyrithm package. Sets the package version
│   └── etl_lib/        # → Folder containing the shared python library
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
