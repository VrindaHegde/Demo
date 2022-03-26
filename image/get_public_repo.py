import base64
from github import Github
from pprint import pprint

list_repo=[]

# Github username
username = "VrindaHegde"
# pygithub object
g = Github()
# get that user by username
user = g.get_user(username)

for repo in user.get_repos():
    list_repo.append(repo)
    print(repo)

print(list_repo)

with open("test.txt","w") as f:
    f.write(' '.join(map(str,list_repo)))