from typing import AnyStr, Dict

class Repo():
    _full_name: str
    _subscribers_count: str
    _error: str

    def __init__(self, repo_info: Dict) -> None:
        self._full_name = repo_info.get("full_name", '')
        self._subscribers_count = repo_info.get("subscribers_count", '')
        self._error = repo_info.get("error", '')

    def get_name(self) -> AnyStr:
        return self._full_name

    def get_subscribers(self) -> AnyStr:
        return self._subscribers_count
    
    def is_error(self) -> bool:
        return self._error != ""