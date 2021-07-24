"""
Saves the bot data to a local file.
"""

import json
from benedict import benedict
from pathlib import Path

__authors__ = "Frederik Beimgraben"
__credits__ = ["Frederik Beimgraben"]
__maintainer__ = "Frederik Beimgraben"
__email__ = "beimgraben8@gmail.com"
__status__ = "WIP"


class BotData(object):
    def __init__(self, file_name='data.json', folder='db'):

        # Check path
        cwd = Path(__file__).parent.absolute()
        data_dir = cwd / 'data'
        if not data_dir.is_dir():
            data_dir.mkdir()
        db_dir = data_dir / folder
        if not db_dir.is_dir():
            db_dir.mkdir()

        self.data = benedict({
            'type': 'bot-data',
            'guilds': {},
        })

        self.path = db_dir / file_name  # File path

        # Load data
        try:
            if self.path.is_file():
                with open(self.path, 'r') as fp:
                    data = benedict(json.load(fp))
                    if data['type'] == 'bot-data':
                        self.data = data
                    else:
                        raise ImportError('Data format not supported')
        except ValueError:
            ImportError('Data format not supported')

    def store(self):
        with open(self.path, 'w') as fp:
            json.dump(self.data, fp)

    def __getitem__(self, path):
        return self.data[path]

    def __delitem__(self, path):
        del self.data[path]
        self.store()

    def __contains__(self, item):
        return item in self.data

    def __setitem__(self, path, value):
        self.data[path] = value
        self.store()

    def __len__(self):
        return len(self.data)
