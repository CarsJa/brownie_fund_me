from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    get_account_yaml,
    get_address,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

# Um Verträge zu verifizieren, können sie getestet werden mit etherscan und der API. Jedoch nur wenn man im Mainnet ist.

# Daher werden Mock verwendet um die Verträge zu testen

# logic
# Wenn main network like rinkeby, nutze die entsprechende Adress
# else deploy mocks


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
