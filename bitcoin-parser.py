#!/usr/bin/env python3
import json
import boto3
import pandas as pd
from json_default import default
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Set your RPC host address/port and credentials
rpcConnection = AuthServiceProxy(
    "http://%s:%s@%s:%s"%("rpcusername", "rpcpasswd", "127.0.0.1", "8332"),
    timeout=120)

#Current Block (as of latest sync to blockchain)
currBlock = rpcConnection.getblockcount()
print("Current Block: " + str(currBlock))
#Get block hash for the current block
getBlockHash = rpcConnection.getblockhash(currBlock)
print("Block hash for current block: " + str(getBlockHash))
#Get current block info
getBlockInfo = rpcConnection.getblock(getBlockHash)
#print("Current block information: " + str(getBlockInfo))
print("Current block information: ")

#Save raw data to file
data = json.dumps(getBlockInfo, default=default, indent=4, sort_keys=True)
df = pd.read_json(data)
dataCurrBlock = 'block'+str(currBlock)+'.json'
rawData = df.to_json(dataCurrBlock, orient="records", lines=True)
print(data)

#Convert JSON to CSV
csvCurrBlock = 'block'+str(currBlock)+'.csv'
csvFile = df.to_csv (csvCurrBlock, index = 4)

#Upload Raw data and CSV file to S3
session = boto3.Session(
    aws_access_key_id='YOURACCESSKEY',
    aws_secret_access_key='YOURSECRETKEY',
)
s3 = session.resource('s3')
s3.meta.client.upload_file(Filename=dataCurrBlock, Bucket='bucketname', Key=dataCurrBlock)
s3.meta.client.upload_file(Filename=csvCurrBlock, Bucket='bucketname', Key=csvCurrBlock)
print("Uploaded successfully to S3")
