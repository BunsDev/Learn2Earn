let provider;
let accounts;

let accountAddress = "";
let signer;

function login()
{

  console.log('oh hey there');

 // signer.signMessage("hello");

signer.signMessage("Signing in to Learn2Earn", accountAddress, "test password!")
            .then((signature) => {               handleAuth(accountAddress, signature)
            });
}

function handleAuth(accountAddress, signature)
{
  console.log(accountAddress);
  console.log(signature);

  fetch('login', {
    method: 'post',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify([accountAddress,signature])
  }).then((response) => {
    return response.json();
  })
  .then((data) => {
    console.log(data);
  });

}

ethereum.enable().then(function () {

    provider = new ethers.providers.Web3Provider(web3.currentProvider);


    provider.getNetwork().then(function (result) {
        if (result['chainId'] != 250) {
            document.getElementById("msg").textContent = 'Switch to Fantom Network!';

        } else { // okay, confirmed we're on mainnet

            provider.listAccounts().then(function (result) {
                console.log(result);
                accountAddress = result[0]; // figure out the user's Eth address

                document.getElementById("msg").textContent = account_address;


                // get a signer object so we can do things that need signing
                signer = provider.getSigner();

                // build out the table of players
            })
        }
    })
})
