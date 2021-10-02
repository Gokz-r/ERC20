from brownie import *

def shot():
    return Token.deploy(
    'Dollar',
    'CUD',
    18,
    1e21,
    {'from':accounts[0]}
    )
