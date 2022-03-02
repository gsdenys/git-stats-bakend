import pandas as pd
from .connector import get

_repo_columns = ("name", "full_name", "description", "fork", "owner", "size", "created_at", "updated_at", "commits_url")


def get_user_repos(login):
    repos = pd.DataFrame()
    page_num = 1

    while True:
        url = f"https://api.github.com/users/{login}/repos?page={page_num}"
        repos_search = get(url)

        if len(repos_search) == 0:
            break

        repos_prt = pd.DataFrame(repos_search)

        if len(repos) == 0:
            repos = repos_prt
        else:
            repos = pd.concat([repos, repos_prt], ignore_index=True)

        page_num = page_num + 1

    return repos[list(_repo_columns)]
