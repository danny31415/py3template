import requests


class Sample():
    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self._data

    def print_data(self):
        print(self.data)


class ApiStuff():
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def make_call(self, params=None):
        r = requests.get(self.endpoint, params=params)
        return r

