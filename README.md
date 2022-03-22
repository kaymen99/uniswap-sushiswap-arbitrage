# uniswap-sushiswap-arbitrage
Smart contract for performing arbitrage between Uniswap and Sushiswap

## Features:
The smart contract SimpleArbitrage alows the user to make an arbitrage between the 2 exchanges and ensures that the operation is always profitable

## Usage:

### Installation & Setup:

1. Installing Brownie: Brownie is a python framework for smart contracts development,testing and deployments. It's quit like [HardHat](https://hardhat.org) but it uses python for writing test and deployements scripts instead of javascript.
   Here is a simple way to install brownie.
   ```
    pip install --user pipx
    pipx ensurepath
    # restart your terminal
    pipx install eth-brownie
   ```
   Or if you can't get pipx to work, via pip (it's recommended to use pipx)
    ```
    pip install eth-brownie
    ```
   
3. Clone the repo:
   ```sh
   git clone https://github.com/Aymen1001/uniswap-sushiswap-arbitrage.git
   cd uniswap-sushiswap-arbitrage
   ```

4. Set your environment variables:

   To be able to deploy to real testnets you need to add your PRIVATE_KEY (You can find your PRIVATE_KEY from your ethereum wallet like metamask) and the infura project Id (just create an infura account it's free) to the .env file:
   ```
   PRIVATE_KEY=<PRIVATE_KEY>
   WEB3_INFURA_PROJECT_ID=<< YOUR INFURA PROJECT ID >>
   ```
### How to run:

To start an arbitrage you just need to run the commande :
   ```sh
   brownie run scripts/arbitrage.py
   ```

