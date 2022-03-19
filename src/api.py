from abc import ABC, abstractmethod
from typing import Dict

class API(ABC):
    url: str

    def __init__(self, url) -> None:
        self.url = url
        super().__init__()

    @abstractmethod
    def get_repo() -> Dict:
        pass