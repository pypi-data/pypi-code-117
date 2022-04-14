# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyzscaler', 'pyzscaler.zia', 'pyzscaler.zpa']

package_data = \
{'': ['*']}

install_requires = \
['python-box==6.0.2', 'restfly==1.4.6']

setup_kwargs = {
    'name': 'pyzscaler',
    'version': '1.1.1',
    'description': 'A python SDK for the Zscaler API.',
    'long_description': '[![pyZscaler](https://raw.githubusercontent.com/mitchos/pyZscaler/gh-pages/docs/assets/images/logo.svg)](https://github.com/mitchos/pyZscaler)\n# pyZscaler - An unofficial SDK for the Zscaler API\n\n[![Build Status](https://github.com/mitchos/pyZscaler/actions/workflows/build.yml/badge.svg)](https://github.com/mitchos/pyZscaler/actions/workflows/build.yml)\n[![Documentation Status](https://readthedocs.org/projects/pyzscaler/badge/?version=latest)](https://pyzscaler.readthedocs.io/?badge=latest)\n[![License](https://img.shields.io/github/license/mitchos/pyZscaler.svg)](https://github.com/mitchos/pyZscaler)\n[![Code Quality](https://app.codacy.com/project/badge/Grade/d339fa5d957140f496fdb5c40abc4666)](https://www.codacy.com/gh/mitchos/pyZscaler/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mitchos/pyZscaler&amp;utm_campaign=Badge_Grade)\n[![PyPI Version](https://img.shields.io/pypi/v/pyzscaler.svg)](https://pypi.org/project/pyZscaler)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyzscaler.svg)](https://pypi.python.org/pypi/pyzscaler/)\n[![GitHub Release](https://img.shields.io/github/release/mitchos/pyZscaler.svg)](https://github.com/mitchos/pyZscaler/releases/)\n\npyZscaler is an SDK that provides a uniform and easy-to-use interface for each of the Zscaler product APIs.\n\nThis SDK is not affiliated with, nor supported by Zscaler in any way.\n\n## Quick links\n* [pyZscaler API Documentation](https://pyzscaler.readthedocs.io)\n* [pyZscaler User Documentation and Examples (WIP)](https://pyzscaler.packet.tech)\n\n## Overview\nEach Zscaler product has separate developer documentation and authentication methods. This SDK simplifies\nsoftware development using the Zscaler API.\n\nThis SDK leverages the [RESTfly framework](https://restfly.readthedocs.io/en/latest/index.html) developed\nby Steve McGrath.\n\n## Features\n- Simplified authentication with Zscaler APIs.\n- Uniform interaction with all Zscaler APIs.\n- Uses [python-box](https://github.com/cdgriffith/Box/wiki) to add dot notation access to json data structures.\n- Zscaler API output automatically converted from CamelCase to Snake Case.\n- Various quality of life enhancements for object CRUD methods.\n\n## Products\n- Zscaler Private Access (ZPA)\n- Zscaler Internet Access (ZIA)\n- Cloud Security Posture Management (CSPM) - (work in progress)\n\n\n## Installation\n\nThe most recent version can be installed from pypi as per below.\n\n    $ pip install pyzscaler\n\n## Usage\n\nBefore you can interact with any of the Zscaler APIs, you may need to generate API keys or retrieve tenancy information\nfor each product that you are interfacing with. Once you have the requirements and you have installed pyZscaler,\nyou\'re ready to go.\n\n\n### Quick ZIA Example\n\n```python\nfrom pyzscaler import ZIA\nfrom pprint import pprint\n\nzia = ZIA(api_key=\'API_KEY\', cloud=\'CLOUD\', username=\'USERNAME\', password=\'PASSWORD\')\nfor user in zia.users.list_users():\n    pprint(user)\n```\n\n### Quick ZPA Example\n\n```python\nfrom pyzscaler import ZPA\nfrom pprint import pprint\n\nzpa = ZPA(client_id=\'CLIENT_ID\', client_secret=\'CLIENT_SECRET\', customer_id=\'CUSTOMER_ID\')\nfor app_segment in zpa.app_segments.list_segments():\n    pprint(app_segment)\n```\n\n## Documentation\n### API Documentation\npyZscaler\'s API is fully 100% documented and is hosted at [ReadTheDocs](https://pyzscaler.readthedocs.io). \n\nThis documentation should be used when working with pyZscaler rather than referring to Zscaler\'s API reference. \npyZscaler makes some quality of life improvements to simplify and clarify arguments passed to Zscaler\'s API.\n\n### User Documentation\nA start has been made on [user documentation](https://pyzscaler.packet.tech) with examples and explanations on how to implement with pyZcaler.\n\n## Is It Tested?\nYes! pyZscaler has a complete test suite that fully covers all methods within the ZIA and ZPA modules.\n\n## Contributing\n\nContributions to pyZscaler are absolutely welcome.\n\nPlease see the [Contribution Guidelines](https://github.com/mitchos/pyZscaler/blob/main/CONTRIBUTING.md) for more information.\n\n[Poetry](https://python-poetry.org/docs/) is currently being used for builds and management. You\'ll want to have\npoetry installed and available in your environment.\n\n## Issues\nPlease feel free to open an issue using [Github Issues](https://github.com/mitchos/pyZscaler/issues) if you run into any problems using pyZscaler.\n\n## License\nMIT License\n\nCopyright (c) 2021 Mitch Kelly\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.',
    'author': 'Mitch Kelly',
    'author_email': 'me@mkelly.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pyzscaler.packet.tech/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
