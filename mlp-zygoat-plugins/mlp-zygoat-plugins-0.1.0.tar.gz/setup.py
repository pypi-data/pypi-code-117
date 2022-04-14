# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mlp_zygoat_plugins',
 'mlp_zygoat_plugins.images',
 'mlp_zygoat_plugins.images.resources']

package_data = \
{'': ['*']}

install_requires = \
['zygoat>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'mlp-zygoat-plugins',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Mark Rawls',
    'author_email': 'markrawls96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
