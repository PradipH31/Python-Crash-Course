#!../P2ENV/bin/python

import requests

from operator import itemgetter

# Url for the top stories
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status Code ;', r.status_code)

# item id of the top stories
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
           str(submission_id) + '.json')
    # request data of the post with the id above
    submission_r = requests.get(url)
    print(submission_r.status_code)

    # json data of the post with the id above
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

# sorting according to the comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:', submission_dict['title'])
    print('Discussion Link:', submission_dict['link'])
    print('Comments:', submission_dict['comments'])
