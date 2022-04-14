# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alacritty_styles']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.2,<9.0.0',
 'requests>=2.27.1,<3.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0']

entry_points = \
{'console_scripts': ['alacritty-styles = alacritty_styles.main:cli']}

setup_kwargs = {
    'name': 'alacritty-styles',
    'version': '0.1.0',
    'description': 'A simple program for changing Alacritty colors.',
    'long_description': None,
    'author': 'Bruno Silva Oliveira',
    'author_email': 'brunooliveira095@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
