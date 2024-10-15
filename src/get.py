import requests

class GetData(object):
    def __init__(self):
        pass

    def check_url(self, url: str) -> None:
        if url.startswith(("https://","http://")):
            return
        else:
            raise ValueError("url is not in https/http format")