from email import message
import json
import unittest
import sys
import os
from unittest import mock
import requests
from src.repo import Repo
sys.path.append(os.path.join('src'))
from src.github_api import GithubApi

def mocked_get_repo_request(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
        def json(self):
            return self.json_data

    if args[0] == 'test-failure.com':
        raise requests.ConnectionError("Error creating connection")
    elif args[0] == 'test.com':
        return MockResponse({"subscribers_count": "5", "full_name": "test_repo"})

class TestGithubApi(unittest.TestCase):
    def setUp(self) -> None:
        self.github_api = GithubApi('test.com')
        self.github_failure = GithubApi('test-failure.com')
    
    def tearDown(self) -> None:
        del self.github_api
        del self.github_failure
    
    def test_url_set(self):
        self.assertEqual('test.com', self.github_api.get_repo_url())
    
    @mock.patch('requests.get', side_effect=mocked_get_repo_request)
    def test_get_repo_failure(self, mock_get):
        repo: Repo = self.github_failure.get_repo()
        self.assertEqual(True, repo.is_error())
    
    @mock.patch('requests.get', side_effect=mocked_get_repo_request)
    def test_get_repo_success(self, mock_get):
        repo: Repo = self.github_api.get_repo()
        self.assertEqual(False, repo.is_error())
        self.assertEqual('5', repo.get_subscribers())
        self.assertEqual('test_repo', repo.get_name())

if __name__ == '__main__':
    unittest.main()