from typing import Dict
from api import API
import requests

from repo import Repo

class GithubApi(API):
    def get_repo(self) -> Repo:
        response = requests.get(self.url)
        return Repo(response.json())
