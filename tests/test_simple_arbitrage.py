import pytest, brownie
from brownie import config, network, SimpleArbitrage
from scripts.helper_scripts import get_account, toWei, approve_erc20, FORKED_BLOCHCHAINS, ZERO_ADDRESS
from scripts.get_weth import get_weth


def test_deploy():

    weth_token = config["networks"][network.show_active()]["weth-token"]
    dai_token = config["networks"][network.show_active()]["dai-token"]

    uni_router_address = config["networks"][network.show_active()]["uniswap-router"]
    sushi_router_address = config["networks"][network.show_active()]["sushiswap-router"]
    arbitrage,owner = deploy_arbitrage()

    assert arbitrage.address != ZERO_ADDRESS
    assert owner == get_account()
    assert arbitrage.wethAddress() == weth_token
    assert arbitrage.daiAddress() == dai_token
    assert arbitrage.uniswapRouterAddress() == uni_router_address
    assert arbitrage.sushiswapRouterAddress() == sushi_router_address

def test_deposit():
    weth_token = config["networks"][network.show_active()]["weth-token"]
    arbitrage,owner = deploy_arbitrage()

    amount = toWei(5)

    approve_erc20(weth_token, arbitrage.address, amount, owner)

    deposit_tx = arbitrage.deposit(amount, {"from": owner})
    deposit_tx.wait(1)

    assert arbitrage.arbitrageAmount() == amount

def test_withdraw():
    weth_token = config["networks"][network.show_active()]["weth-token"]

    arbitrage,owner = deploy_arbitrage()
    amount = toWei(5)

    approve_erc20(weth_token, arbitrage.address, amount, owner)

    deposit_tx = arbitrage.deposit(amount, {"from": owner})
    deposit_tx.wait(1)

    withdraw_amount = toWei(2)

    withdraw_tx = arbitrage.withdraw(withdraw_amount, {"from": owner})
    withdraw_tx.wait(1)

    assert arbitrage.arbitrageAmount() == amount - withdraw_amount

def test_make_arbitrage():
    weth_token = config["networks"][network.show_active()]["weth-token"]

    arbitrage,owner = deploy_arbitrage()

    amount = toWei(5)

    approve_erc20(weth_token, arbitrage.address, amount, owner)

    deposit_tx = arbitrage.deposit(amount, {"from": owner})
    deposit_tx.wait(1)

    # Try to make arbitrage and revert if it's not profitable
    with brownie.reverts("Arbitrage not profitable"):
        arbitrage_tx = arbitrage.makeArbitrage({"from": owner})
        arbitrage_tx.wait(1)

def deploy_arbitrage():

    weth_token = config["networks"][network.show_active()]["weth-token"]
    dai_token = config["networks"][network.show_active()]["dai-token"]

    uni_router_address = config["networks"][network.show_active()]["uniswap-router"]
    sushi_router_address = config["networks"][network.show_active()]["sushiswap-router"]

    if network.show_active() not in FORKED_BLOCHCHAINS:
        pytest.skip()

    owner = get_account()
    get_weth(owner, 10)
    
    arbitrage = SimpleArbitrage.deploy(
        uni_router_address,
        sushi_router_address,
        weth_token,
        dai_token,
        {"from": owner}
    )

    return arbitrage, owner


