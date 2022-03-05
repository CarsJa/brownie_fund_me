from brownie import network, config, accounts, MockV3Aggregator
import os
from web3 import Web3


FORKED_LOCAL_ENVIROMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "local-ganache2"]

DECIMALS = 18
STARTING_PRICE = 200000000000


def get_address():
    return "0x1Fc6BF29E1d63Bfb26824c3e9380111c8477E0b8"


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIROMENTS
    ):
        return accounts[0]

    else:
        return accounts.add(os.getenv("PRIVATE_KEY"))


def get_account_yaml():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()},
        )
    # um 2000000000000000000000 lesbar zu machen muss web3 importiert werden
    print("Mock deployed")
