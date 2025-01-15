import datetime
import os


def get_repos():
    return [repo for repo in os.listdir(".") if os.path.isdir(repo)]


def get_last_commit(repo):
    return datetime.datetime.fromtimestamp(os.path.getmtime(repo))
