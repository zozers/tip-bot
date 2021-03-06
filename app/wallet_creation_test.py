from web3 import Web3
from eth_account import Account
import sys, os
from dotenv import dotenv_values
import secrets

config = dotenv_values("../.env")


print(f"{config['FTM_TESTNET_WEBSOCKET']=}")

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(config['FTM_TESTNET_RPC']))

# w3 = Web3(Web3.WebsocketProvider(config['FTM_TESTNET_WEBSOCKET']))
if not w3.isConnected():
    sys.exit("Connection Failed")

def create_wallet():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    print ("SAVE BUT DO NOT SHARE THIS (PRIVATE KEY):", private_key)
    acct = Account.from_key(private_key)
    print("Address:", acct.address)
    return (private_key, acct.address)