import brownie
from brownie import config, network, SimpleArbitrage
from scripts.helper_scripts import get_account, toWei, fromWei, approve_erc20, FORKED_BLOCHCHAINS
from scripts.get_weth import get_weth



weth_token = config["networks"][network.show_active()]["weth-token"]
dai_token = config["networks"][network.show_active()]["dai-token"]

uni_router_address = config["networks"][network.show_active()]["uniswap-router"]
sushi_router_address = config["networks"][network.show_active()]["sushiswap-router"]

def main():
    account = get_account()

    if network.show_active() in FORKED_BLOCHCHAINS:
        get_weth(account, 10)
    
    arbitrage = SimpleArbitrage.deploy(
        uni_router_address,
        sushi_router_address,
        weth_token,
        dai_token,
        {"from": account}
    )

    amount = toWei(5)

    approve_erc20(weth_token, arbitrage.address, amount, account)

    deposit_tx = arbitrage.deposit(amount, {"from": account})
    deposit_tx.wait(1)

    print("amount deposited: ", fromWei(arbitrage.arbitrageAmount()))

    arbitrage_tx = arbitrage.makeArbitrage({"from": account})
    arbitrage_tx.wait(1)
    
    print("New amount: ", fromWei(arbitrage.arbitrageAmount()))
    
    
    
