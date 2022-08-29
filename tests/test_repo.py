import unittest

from src import repo


class RepoTest(unittest.TestCase):
    def setUp(self):
        self.repo: repo.Repo = repo.Repo({"subscribers_count": "5", "full_name": "test_repo"})
    
    def tearDown(self) -> None:
        del self.repo

    def test_get_name(self):
        self.assertEqual("test_repo", self.repo.get_name())
    
    def test_get_subscribers(self):
        self.assertEqual("5", self.repo.get_subscribers())

if __name__ == '__main__':
    unittest.main()
        
