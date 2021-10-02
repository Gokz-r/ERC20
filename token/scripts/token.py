#!/usr/bin/python3

from brownie import Token, accounts


def main():
    acct = accounts.load('Owner')
    return Token.deploy("AUD coin", "AUD", 18, 0, {'from': acct})
