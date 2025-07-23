import os

class Env:
    def __init__(self):
        pass

    def read_env(self, path='.env'):
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        
        with open(path) as file_handler:
            for line in file_handler:
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

    def get(self, key, default=None):
        return os.environ.get(key) or default