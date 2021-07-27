import requests
from requests.compat import urljoin
from lxml import html

API_URL = "https://api.stackexchange.com"
base_params = {'site':'stackoverflow'}
def get_accepted_answers():
    # this is not random yet
    params = {**base_params, 'order':'desc', 'sort':'votes', 'tagged':'python', 'intitle': 'bubble sort'}
    search_url = urljoin(API_URL, 'search')
    resp = requests.get(search_url, params=params)
    if resp.status_code != 200: return False
    try:
        questions = resp.json()['items']
    except BaseException as e:
        return False
    
    # filter for questions with accepted answers
    accepted_answer_ids = [q['accepted_answer_id'] for q in questions if q['is_answered'] == True and 'accepted_answer_id' in q]
    return accepted_answer_ids

def get_answer_url(answer_id):
    return urljoin("https://stackoverflow.com/a/",str(answer_id))

def get_answer_html(answer_id):
    answer_url = get_answer_url(answer_id)
    resp = requests.get(answer_url)
    if resp.status_code == 200:
        return resp.content

def parse_answer_html(answer_html):
    # returns code only string