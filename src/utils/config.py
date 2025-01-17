import datetime
import os


def get_last_commit(repo):
    return datetime.datetime.fromtimestamp(os.path.getmtime(repo))
