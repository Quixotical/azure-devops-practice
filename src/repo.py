from typing import AnyStr, Dict

class Repo():
    full_name: str
    subscribers_count: str

    def __init__(self, repo_info: Dict) -> None:
        self.full_name = repo_info["full_name"]
        self.subscribers_count = repo_info["subscribers_count"]

    def get_name(self) -> AnyStr:
        return self.name

    def get_subscribers(self) -> AnyStr:
        return self.subscribers_count