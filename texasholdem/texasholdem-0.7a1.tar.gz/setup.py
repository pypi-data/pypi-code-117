# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['texasholdem',
 'texasholdem.agents',
 'texasholdem.card',
 'texasholdem.evaluator',
 'texasholdem.game',
 'texasholdem.gui',
 'texasholdem.util']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.13,<2.0.0']

extras_require = \
{':sys_platform == "win32"': ['windows-curses>=2.3.0,<3.0.0']}

setup_kwargs = {
    'name': 'texasholdem',
    'version': '0.7a1',
    'description': 'A texasholdem python package',
    'long_description': '# texasholdem\n![Pytest Status](https://github.com/SirRender00/texasholdem/actions/workflows/pytest.yml/badge.svg)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://raw.githubusercontent.com/SirRender00/texasholdem/main/LICENSE)\n[![Documentation Status](https://readthedocs.org/projects/texasholdem/badge/?version=stable)](https://texasholdem.readthedocs.io/en/stable/?badge=stable)\n![Pylint Status](https://github.com/SirRender00/texasholdem/actions/workflows/pylint.yml/badge.svg)\n\nA python package for Texas Hold \'Em Poker, providing\n- Fast evaluation of hand strengths \n- Export & import human-readable game history\n- GUIs to view games and game history\n- Simple & complex agents \n- Compliance with World Series of Poker Official Rules\n- And more\n\n| Version Name | Latest Tag | Release Notes | Patch Notes | Documentation | Release Date | End Support Date |\n| ------------ | ---------- | ------------- | ----------- | ------------- | ------------ | ---------------- |\n| 0.7-alpha    | v0.7-alpha.1 | [Release Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.7-alpha.0) | [Patch Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.7-alpha.1) | [Documentation](https://texasholdem.readthedocs.io/en/latest/) | 10 April 2022 | |\n| 0.6          | v0.6.3       | [Release Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.6.0) | [Patch Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.6.3) | [Documentation](https://texasholdem.readthedocs.io/en/0.6/) | 24 March 2022 | |\n| 0.5          | v0.5.2       | [Release Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.5.0) | [Patch Notes](https://github.com/SirRender00/texasholdem/releases/tag/v0.5.2) | [Documentation](https://texasholdem.readthedocs.io/en/0.5/) | 21 March 2022 | |\n\nCurrent Roadmap \\\n[v1.0.0](https://github.com/SirRender00/texasholdem/wiki/Version-1.0.0-Roadmap)\n\n## Contributing\nWant a new feature, found a bug, or have questions? Feel free to add to our issue board on Github!\n[Open Issues](https://github.com/SirRender00/texasholdem/issues>).\n\nWe welcome any developer who enjoys the package enough to contribute! Please message me at evyn.machi@gmail.com\nif you want to be added as a contributor and check out the \n[Developer\'s Guide](https://github.com/SirRender00/texasholdem/wiki/Developer\'s-Guide).\n\n## Install\nThe package is available on pypi and can be installed with\n\n```bash\npip install texasholdem\n```\n\nFor the latest experimental version\n```bash\npip install texasholdem --pre\n```\n\n## Quickstart\nPlay a game from the command line and take turns for every player out of the box.\n\n```python\nfrom texasholdem.game.game import TexasHoldEm\nfrom texasholdem.gui.text_gui import TextGUI\n\ngame = TexasHoldEm(buyin=500, big_blind=5, small_blind=2, max_players=6)\ngui = TextGUI(game=game)\n\nwhile game.is_game_running():\n    game.start_hand()\n\n    while game.is_hand_running():\n        gui.run_step()\n\n    path = game.export_history(\'./pgns\')     # save history\n    gui.replay_history(path)                 # replay history\n```\n\n## Overview\nThe following is a quick summary of what\'s in the package. Please see the \n[docs](https://texasholdem.readthedocs.io/en/stable/) for all the details.\n\n### Game Information\n\nGet game information and take actions through intuitive attributes.\n\n```python\nfrom texasholdem import TexasHoldEm, HandPhase, ActionType\n\ngame = TexasHoldEm(buyin=500,\n                   big_blind=5,\n                   small_blind=2,\n                   max_players=9)\ngame.start_hand()\n\nassert game.hand_phase == HandPhase.PREFLOP\nassert HandPhase.PREFLOP.next_phase() == HandPhase.FLOP\nassert game.chips_to_call(game.current_player) == game.big_blind\nassert len(game.get_hand(game.current_player)) == 2\n\ngame.take_action(ActionType.CALL)\n\nplayer_id = game.current_player\ngame.take_action(ActionType.RAISE, total=10)\nassert game.player_bet_amount(player_id) == 10\nassert game.chips_at_stake(player_id) == 20     # total amount in all pots the player is in\n\nassert game.chips_to_call(game.current_player) == 10 - game.big_blind\n```\n\n### Cards\nThe card module represents cards as 32-bit integers for simple and fast hand\nevaluations.\n\n```python\nfrom texasholdem import Card\n\ncard = Card("Kd")                       # King of Diamonds\nassert isinstance(card, int)            # True\nassert card.rank == 11                  # 2nd highest rank (0-12)\nassert card.pretty_string == "[ K ♦ ]"\n```\n\n### Agents\nThe package also comes with basic agents including `call_agent` and `random_agent`\n\n```python\nfrom texasholdem import TexasHoldEm\nfrom texasholdem.agents import random_agent, call_agent\n\ngame = TexasHoldEm(buyin=500, big_blind=5, small_blind=2)\ngame.start_hand()\n\nwhile game.is_hand_running():\n    if game.current_player % 2 == 0:\n        game.take_action(*random_agent(game))\n    else:\n        game.take_action(*call_agent(game))\n```\n\n### Game History\nExport and import the history of hands to files.\n\n```python\nfrom texasholdem import TexasHoldEm\nfrom texasholdem.gui import TextGUI\n\ngame = TexasHoldEm(buyin=500, big_blind=5, small_blind=2)\ngame.start_hand()\n\nwhile game.is_hand_running():\n    game.take_action(*some_strategy(game))\n\n# export to file\ngame.export_history("./pgns/my_game.pgn")\n\n# import and replay\ngui = TextGUI()\nfor state in TexasHoldEm.import_history("./pgns/my_game.pgn"):\n    gui.print_state(state)\n```\nPGN files also support single line and end of line comments starting with "#".\n\n### Poker Evaluator\nThe evaluator module returns the rank of the best 5-card hand from a list of 5 to 7 cards.\nThe rank is a number from 1 (strongest) to 7462 (weakest).\n\n```python\nfrom texasholdem import Card\nfrom texasholdem.evaluator import  evaluate, rank_to_string\n\nassert evaluate(cards=[Card("Kd"), Card("5d")],\n                board=[Card("Qd"),\n                       Card("6d"),\n                       Card("5s"),\n                       Card("2d"),\n                       Card("5h")]) == 927\nassert rank_to_string(927) == "Flush, King High"\n```\n\n### GUIs\nThe GUI package currently comes with a text-based GUI to play games from the command line. Coming later\nwill be web-app based GUIs.\n',
    'author': 'Evyn Machi',
    'author_email': 'evyn.machi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SirRender00/texasholdem',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
