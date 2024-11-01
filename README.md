# config_example

# Setup

## Envrionment

Install the required packages by running:

```bash
conda env create -f environment.yml
```

Activate the environment by running:

```bash
conda activate config
```

Then install your code from source using

```bash
pip install -e .
```

## Trying out your code

To see if the `load_csv()` function is working getting the right data path, you can run the script
from the terminal:

```bash
python nba/data_load.py
```
