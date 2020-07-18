import requests
import re

class getfollowercount:
    def __init__(self, user):
        self.followercount = int(re.search(r'Followers \(([0-9]+)\)', requests.get(f'https://scratch.mit.edu/users/{user}/followers/', auth=('', '')).text, re.I).group(1))
