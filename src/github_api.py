from typing import AnyStr, Dict
from src.api import API
from src.repo import Repo
import requests

class GithubApi(API):   
    def get_repo(self) -> Repo:
        try:
            response = requests.get(self.url)
            return Repo(response.json())
        except requests.ConnectionError as err:
            return Repo({"error": str(err)})
    
    def get_repo_url(self) -> AnyStr:
        return self.url
