# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thirdweb',
 'thirdweb.abi',
 'thirdweb.common',
 'thirdweb.constants',
 'thirdweb.contracts',
 'thirdweb.core',
 'thirdweb.core.classes',
 'thirdweb.core.helpers',
 'thirdweb.types',
 'thirdweb.types.contracts',
 'thirdweb.types.settings']

package_data = \
{'': ['*']}

install_requires = \
['dacite>=1.6.0,<2.0.0',
 'mypy-extensions>=0.4.3,<0.5.0',
 'pymerkle>=2.0.2,<3.0.0',
 'thirdweb-contract-wrappers>=2.0.4,<3.0.0',
 'thirdweb-eth-account>=0.6.6,<0.7.0',
 'web3==5.27.0']

setup_kwargs = {
    'name': 'thirdweb-sdk',
    'version': '2.0.2a1',
    'description': '',
    'long_description': '# Thirdweb Python SDK\n\nThe thirdweb SDK for Python. Currently supports Mainnet, Rinkeby, Goerli, Polygon, and Mumbai.\n## Installation\n\n```bash\npip install thirdweb-sdk\n```\n\n## Getting Started\n\nTo start using this SDK, you just need to pass in a provider configuration.\n### Instantiating the SDK\n\nOnce you have all the necessary dependencies, you can follow the following setup steps to get started with the SDK read-only functions:\n\n```python\nfrom thirdweb import ThirdwebSDK\nfrom web3 import Web3\n\n# Add your own RPC URL here or use a public one\nRPC_URL = "https://rpc-mumbai.maticvigil.com"\n\n# Instantiate a new provider to pass into the SDK\nprovider = Web3(Web3.HTTPProvider(RPC_URL))\n\n# Finally, you can create a new instance of the SDK to use\nsdk = ThirdwebSDK(provider)\n```\n\n### Working With Contracts\n\nOnce you instantiate the SDK, you can use it to access your thirdweb contracts. You can use the SDK\'s contract getter functions like `get_token`, `get_edition`, `get_nft_collection`, and `get_marketplace` to get the respective SDK contract instances. To use an NFT Collection contract for example, you can do the following.\n\n```python\n# Add your NFT Collection contract address here\nNFT_COLLECTION_ADDRESS = "0x.."\n\n# And you can instantiate your contract with just one line\nnft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)\n\n# Now you can use any of the read-only SDK contract functions\nnfts = nft_collection.get_all()\nprint(nfts)\n```\n\n### Signing Transactions\n\n> :warning: Never commit private keys to file tracking history, or your account could be compromised. Make sure to add `.env` to your `.gitignore` file.\n\nMeanwhile, if you want to use write functions as well and connect a signer, you can use the following setup (if you want to use your private key as displayed below, make sure to run `pip install python-dotenv` as well):\n\n```python\nfrom thirdweb import ThirdwebSDK\nfrom thirdweb.types.nft import NFTMetadataInput\nfrom eth_account import Account\nfrom dotenv import load_dotenv\nfrom web3 import Web3\nimport os\n\n# Load environment variables into this file\nload_dotenv()\n\n# This PRIVATE KEY is coming from your environment variables. Make sure to never put it in a tracked file or share it with anyone.\nPRIVATE_KEY = os.environ.get("PRIVATE_KEY")\n\n# Add your own RPC URL here or use a public one\nRPC_URL = "https://rpc-mumbai.maticvigil.com"\n\n# Instantiate a new provider to pass into the SDK\nprovider = Web3(Web3.HTTPProvider(RPC_URL))\n\n# Optionally, instantiate a new signer to pass into the SDK\nsigner = Account.from_key(PRIVATE_KEY)\n\n# Finally, you can create a new instance of the SDK to use\nsdk = ThirdwebSDK(provider, signer)\n\n# Instantiate a new NFT Collection contract as described above.\nNFT_COLLECTION_ADDRESS = "0x.."\nnft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)\n\n# Now you can use any of the SDK contract functions including write functions\nnft_collection.mint(NFTMetadataInput.from_json({ "name": "Cool NFT", "description": "Minted with the Python SDK!" }))\n```\n\nIf you wanted to use the SDK with a signer above, make sure to include your PRIVATE_KEY in your `.env` file, and make sure this file is NOT tracked in any repository (make sure to add it to your `.gitignore` file). Adding your private key to your `.env` would look like the following:\n\n```\nPRIVATE_KEY=your-private-key-here\n```\n\n## Development Environment\n\nIn this section, we\'ll go over the steps to get started with running the Python SDK repository locally and contributing to the code. If you aren\'t interested in contributing to the thirdweb Python SDK, you can ignore this section.\n\n### Poetry Environment Setup\n\nIf you want to work with this repository, make sure to setup [Poetry](https://python-poetry.org/docs/), you\'re virtual environment, and the code styling tools.\n\nAssuming you\'ve installed and setup poetry, you can setup this repository with:\n\n```bash\n$ poetry shell\n$ poetry install\n$ poetry run yarn global add ganache\n$ poetry run yarn add hardhat\n```\n\nAlternatively, if your system can run .sh files, you can set everything up by running the following bash script:\n\n```bash\n$ bash scripts/env/setup.sh\n```\n\n### Running Tests\n\nBefore running tests, make sure you\'ve already run `poetry shell` and are in the poetry virutal environment with all dependencies installed. \n\nOnce you have checked that this you have all the dependencies, you can run the following:\n\n```bash\n$ poetry run brownie test --network hardhat\n```\n\nTo properly setup testing, you\'ll also need to add your private key to the `.env` file as follows (do NOT use a private key of one of your actual wallets):\n\n```.env\nPRIVATE_KEY=...\n```\n\n### Code Style Setup\n\nMake sure you have `mypy`, `pylint`, and `black` installed (all included in the dev dependencies with `poetry install`.\n\nIf you\'re working in VSCode, there a few steps to get everything working with the poetry .venv:\n\n1. To setup poetry virtual environment inside your VSCode so it gets recognized as part of your project (import for linters), you can take the following steps from this [stack overflow answer](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option). You need to run `poetry config virtualenvs.in-project true` and then make sure you delete/create a new poetry env.\n2. In `.vscode/settings.json`, you should have the following:\n```json\n{\n  "python.linting.mypyEnabled": true,\n  "python.linting.enabled": true,\n  "python.linting.pylintEnabled": false\n}\n```\n3. Make sure to set your VSCode `Python: Interpreter` setting to the Python version inside your poetry virtual environment.\n\n\n### Generate Python ABI Wrappers\n\nUse the [abi-gen](https://www.npmjs.com/package/@0x/abi-gen) package to create the Python ABIs. You can install it with the following command:\n\n```bash\n$ npm install -g @0x/abi-gen\n```\n\nAssuming you have the thirdweb contract ABIs in this directory at `/abi`, you can run the following command to generate the necessary ABIs.\n\n```bash\n$ bash scripts/abi/generate.sh\n```\n',
    'author': 'thirdweb',
    'author_email': 'sdk@thirdweb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.7.1',
}


setup(**setup_kwargs)
