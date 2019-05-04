#!../P2ENV/bin/python

import requests

# Setting the url
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

# Storing the response object in r variable
r = requests.get(url)

# status code of 200 is success
print('Status Code: ', r.status_code)

# Converting the json response to a dictionary
response_dict = r.json()
# the keys are total_count, incomplete_results, items
print(response_dict.keys())

# The total repositories will not be returned by github
# Instead it will return a specific number of repositories
print("Total repositories: ", response_dict['total_count'])

# the items key contains all the repos returned by github
repo_dicts = response_dict['items']
print('Repositories given by the api', len(repo_dicts))

# all the keys in a repo dictionary given by github
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print('\nInformation from the given repositories')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
