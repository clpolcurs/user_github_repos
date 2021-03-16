__doc__ = """
Creating a script to list all a user's GitHub repository
"""


import requests
import sys


def get_github_repositories(username):
    url = "https://api.github.com/users/{}/repos".format(username)
    rqst = requests.get(url)
    repos_list = [repos["name"] for repos in rqst.json()]
    return repos_list


def main():
    username = sys.argv[1]
    links = get_github_repositories(username)
    for (idx, repos_name) in enumerate(links, start=1):
        print("{}: {}".format(idx, repos_name))


if __name__ == "__main__":
    main()
