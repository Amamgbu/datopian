# EIA Extraction Script

This script extracts date and price data of Henry Hub Natural Gas Spot Price from EIA website

## Quick Start

1) Clone git repo to local computer using the following command:

> $git clone https://github.com/Amamgbu/datopian.git

2) Open command line and change directory to that of cloned repo:

> > $ cd datopian

3) Update settings.py with API_KEY and Frequency with data to be collected. D represents daily and M represents monthly.

Note: If no frequency is supplied, it defaults to Daily data collection.

4) Create virtual environment:

> $ virtualenv env

5) Activate virtual environment:

- For windows:
> $ cd env/Scripts
> activate

- For Linux:
> source env/bin/activate

6) Install all python libraries needed:

> $ pip install -r requirements.txt

7) Run script using the following:

> $ python3 run.py

