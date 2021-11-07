import json
import requests
from web3 import Web3
from flask import Flask, render_template, request

L2E_WALLET_ADDRESS = "<ADD_WALLET_ADDRESS>"
CONTRACT_ADDRESS = "0x505Bc7FE3F586cd58dc1a4c68B3567f70E05c32D"
PRIVATE_KEY = "<ADD_PRIVATE_KEY>"
to_address = ""

with open("Solidity-Contracts/ABI.json") as f:
    ABI = json.load(f)

def miscellaneous():
    balance = web3.eth.get_balance(L2E_WALLET_ADDRESS)
    print(balance)
    total_supply = contract.functions.totalSupply().call()
    print(total_supply)
    print(contract.functions.name().call())
    print(contract.functions.symbol().call())
    address = web3.toChecksumAddress(L2E_WALLET_ADDRESS)
    balance=contract.functions.balanceOf(address).call()
    print(web3.fromWei(balance, "ether"))

def send_learn_tokens(to_address):
    to_address = Web3.toChecksumAddress(to_address)
    ftm = "https://rpc.ftm.tools"
    web3 = Web3(Web3.HTTPProvider(ftm))
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
    transaction = contract.functions.transfer(to_address, 100000000000000000000).buildTransaction({'chainId': 250, 'gas':2000000, 'nonce': web3.eth.getTransactionCount(L2E_WALLET_ADDRESS)})
    signed_txn = web3.eth.account.signTransaction(transaction, PRIVATE_KEY)
    txn_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(txn_hash)
    return txn_hash

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if(request.method=="POST"):
        global to_address
        to_address = str((request.data[1:-1]).decode("UTF-8"))
        print(to_address, (request.data[1:-1]).decode("UTF-8"))
    return render_template("Home.html")

@app.route('/send_learn', methods=['GET','POST'])
def send_learn():
    print(to_address)
    send_learn_tokens(to_address)
    return render_template("send_learn.html")


@app.route('/courses', methods=["GET", "POST"])
def courses():
    return render_template("Dashboard.html")

@app.route('/fantom_1', methods=["GET", "POST"])
def fantom_1():
    return render_template("Fantom_1.html")

@app.route('/fantom_2', methods=["GET", "POST"])
def fantom_2():
    return render_template("Fantom_2.html")

@app.route('/fantom_3', methods=["GET", "POST"])
def fantom_3():
    return render_template("Fantom_3.html")

@app.route('/bitcoin_1', methods=["GET", "POST"])
def bitcoin_1():
    return render_template("Bitcoin_1.html")

@app.route('/bitcoin_2', methods=["GET", "POST"])
def bitcoin_2():
    return render_template("Bitcoin_2.html")

@app.route('/bitcoin_3', methods=["GET", "POST"])
def bitcoin_3():
    return render_template("Bitcoin_3.html")

@app.route('/ethereum_1', methods=["GET", "POST"])
def ethereum_1():
    return render_template("Ethereum_1.html")

@app.route('/ethereum_2', methods=["GET", "POST"])
def ethereum_2():
    return render_template("Ethereum_2.html")

@app.route('/ethereum_3', methods=["GET", "POST"])
def ethereum_3():
    return render_template("Ethereum_3.html")

if(__name__ == "__main__"):
    app.run(debug=True)
