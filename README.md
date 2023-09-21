# Bimeta Python client

## Documents are in the /docs folder

***At this time, the bimeta-python.pdf document is out of date.  For usage, invoke ./bimeta.py --help***

## Steps to get going using python env and requirements.txt

0. Change to src directory
1. Create python environment
    `python3 -m venv bimeta`
2. Activate environment
    on windows run:
        `bimeta\Scripts\activate.bat`

    on linux/MacOS run:
        `source bimeta/bin/activate`
3. Install required libraries
    `pip install -r requirements.txt`
4. Update configuration file (bimeta_config.toml) with your api key, host and port
5. Make bimeta.py executable
    `chmod +x bimeta.py`
6. Run bimeta
    `./bimeta.py --help`

Next time you want to run bimeta:

1. Change to the src directory
2. activate environment
    on windows run:
        `bimeta\Scripts\activate.bat`

    on linux/MacOS run:
        `source bimeta/bin/activate`
3. Run bimeta
    `./bimeta.py

## Steps to get going using anaconda (conda)

0. Change to src directory

1. Install required libraries
    conda install -y toml click protobuf
    conda install -c conda-forge grpcio -y

2. Update configuration file (bimeta_config.toml) with your api key, host and port

3. Make bimeta.py executable
    `chmod +x bimeta.py`

4. Run bimeta
    `./bimeta.py --help`
