from brownie import network, config, accounts

LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local"]
FORKED_BLOCKCHAIN_ENV = ["mainnet-fork"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_BLOCKCHAIN_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
