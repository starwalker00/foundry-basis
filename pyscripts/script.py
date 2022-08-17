from foundrycli import foundry_cli
from web3 import Web3, EthereumTesterProvider

ens_names = ["vitalik.eth","aavechan.eth"]
for ens_name in ens_names:
    print(ens_name)
    balance = foundry_cli(f'cast balance {ens_name}')
    print(balance)
    print(Web3.fromWei(balance, 'ether'))
