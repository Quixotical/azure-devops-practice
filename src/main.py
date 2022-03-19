from typing import AnyStr, List
from github_api import GithubApi
from repo import Repo

OWNER_PROMPT_REPO = "Please Enter repo owner\n"
NAME_PROMPT_REPO = "Please Enter repo name\n"
API_URL_BASE = "https://api.github.com/repos"

def main() -> None:
    repo_owner, repo_name = get_github_repo_owner_and_name()
    github_api: GithubApi = GithubApi(f'{API_URL_BASE}/{repo_owner}/{repo_name}')
    repo: Repo = github_api.get_repo()
    subscriber_wording: AnyStr = set_singular_or_plural_wording(repo.subscribers_count)
    print(f'This repo has {repo.subscribers_count} {subscriber_wording}')

def get_github_repo_owner_and_name() -> List[AnyStr]:
    repo_owner = input(OWNER_PROMPT_REPO)
    repo_name = input(NAME_PROMPT_REPO)
    return [repo_owner, repo_name]

def set_singular_or_plural_wording(subscriber_count: int) -> AnyStr:
    return 'subscribers' if subscriber_count != 1 else 'subscriber'

if __name__ == '__main__':
    main()