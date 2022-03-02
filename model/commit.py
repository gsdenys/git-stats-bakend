import json

from .connector import get
from .repository import get_user_repos
import pandas as pd


def get_commits(commits_url):
    commits = pd.DataFrame()
    page_num = 1

    while True:
        url = commits_url.replace("{/sha}", "?page=") + str(page_num)
        commit_search = get(url)

        if len(commit_search) == 0:
            break

        df = pd.DataFrame(commit_search)

        if len(commits) == 0:
            commits = df
        else:
            commits = pd.concat([commits, df], ignore_index=True)

        page_num = page_num + 1

    commits['email'] = commits["commit"].apply(lambda x: x["author"]["email"])
    commits['data'] = commits["commit"].apply(lambda x: x['author']['date'])

    commits = commits[['url', 'email', 'data']]

    return commits


def get_commit_files(commit_url):
    commit = get(commit_url)
    df = pd.DataFrame(commit['files'])

    df = df[['filename', 'additions', 'deletions', 'changes']]

    df['extension'] = df['filename'].apply(lambda x: os.path.splitext(x)[1][1:])

    return df


def list_commits(login):
    commits = pd.DataFrame()
    repos = get_user_repos(login)

    for url in repos["commits_url"]:
        commits_df = get_commits(url)

        if len(commits) == 0:
            commits = commits_df
        else:
            commits = pd.concat([commits, commits_df], ignore_index=True)

    return commits.to_dict(orient='records')
