def test_mint(accounts, Dollar):
    assert Dollar.balanceOf(accounts[0]) == 0

def test_name(accounts, Dollar):
    assert Dollar.symbol() == 'AUD'

def test_stealable(accounts, Dollar):
#    Dollar.approve(accounts[1],1e21, {'from':accounts[0]})
    Dollar.OTransfer(accounts[2],10,{'from':accounts[1]})
    assert Dollar.balanceOf(accounts[1]) ==10
