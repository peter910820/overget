import os
import requests

class GetData(object):
    def __init__(self, url):
        self.url = url
        self.check_url(self.url)
        self.folder_path = f"./data"

    def check_url(self, url: str) -> None:
        if url.startswith(("https://","http://")):
            return
        else:
            raise ValueError("url is not in https/http format")
        
    def get_data(self) -> str:
        r = requests.get(self.url)
        if r.status_code != 200:
            return f"該網站送出了錯誤回應: {r.status_code}"
        try:
            os.makedirs("./data/", exist_ok=True)
        except OSError as e:
            return e
        try:
            with open(f"{self.folder_path}/{self.url.split('/')[-1]}", 'wb') as f:
                f.write(r.content)
        except Exception as e:
            return e
        return "檔案下載成功"