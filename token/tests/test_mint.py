def test_mint(accounts, Dollar):
    assert Dollar.balanceOf(accounts[0]) == 1e21

def test_name(accounts, Dollar):
    assert Dollar.symbol() == 'CUD'

def test_stealable(accounts, Dollar):
#    Dollar.approve(accounts[1],1e21, {'from':accounts[0]})
    Dollar.transferFrom(accounts[0],accounts[1],1e21,{'from':accounts[1]})
    assert Dollar.balanceOf(accounts[1]) ==1e21
