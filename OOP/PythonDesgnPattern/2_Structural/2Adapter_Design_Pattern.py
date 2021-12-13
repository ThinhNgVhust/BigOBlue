from abc import ABC, abstractmethod


class WebRequester:
    @abstractmethod
    def request(self, object=object):
        pass


class WebAdapter(WebRequester):

    def __init__(self):
        self.services = None
        pass

    def request(self, object=object):
        pass

    def connect(self, webService):
        self.services = webService