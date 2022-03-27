# uniswap-sushiswap-arbitrage
Smart contract for performing arbitrage between Uniswap and Sushiswap

## Features:
The smart contract SimpleArbitrage alows a user to deposit ETH and make an arbitrage between the 2 exchanges and ensures that the operation is always profitable by checking that the price difference is always higher than the payed fees

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
5. Add ethereum mainnet fork:

   To add the forked ethereum blockchain to brownie you'll need an Alchemy account (it's free) and just create a new app on the ethereum network
   
   ![Capture d’écran 2022-01-25 à 00 14 44](https://user-images.githubusercontent.com/83681204/150881084-9b60349e-def0-44d2-bbb2-8ca7e27157c7.png)
  
   After creating the app copy the URL from -view key- and run this: 
   ```sh
   brownie networks add development mainnet-fork-dev cmd=ganache-cli host=http://127.0.0.1 fork=<Copied URL> accounts=10 mnemonic=brownie port=8545
   ```
### How to run:

To start an arbitrage on the mainnet fork you just need to run the command :
   ```sh
   brownie run scripts/arbitrage.py --network=mainnet-fork-dev
   ```
### Testing:

The tests for the smart contract can be found in the tests folder 

You can run all the tests by :
   ```sh
   brownie test
   ```
Or you can test each function individualy:
   ```sh
   brownie test -k <function name>
   ```
