# Bitcoin Block Data Parser
By running a bitcoin core node in AWS you can use this script to extract data from the blockchain and upload it to an S3 bucket. 

## Setup 
For this setup we used Python 3.5+ on a Debian 9 environment 

We assume you have already setup a bitcoin core node in AWS 

Create a virtual environment in the current directory:

    python3 -m venv venv

Activate the virtual environment:

    # On Linux:
    source venv/bin/activate
    
    
The remainder of the demo assumes that the virtual environment is active.

Install the required libraries:

    pip3 install pandas
    pip3 install json-default
    pip3 install boto3
    pip3 install python-bitcoinrpc
    
 ## Usage
 After installing required the libraries simply run the following command:

    python3 bitcoin-parser.py

The script will execute, parse, and upload the raw data and CSV files to your S3 bucket. 
