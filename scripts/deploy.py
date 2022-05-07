from scripts.helpful_scripts import get_account
from brownie import wallet, config, network


def deploy_wallet():
    account = get_account()
    wallet_deployed = wallet.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )


def main():
    deploy_wallet()
