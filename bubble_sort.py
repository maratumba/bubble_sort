import requests
from requests.compat import urljoin

API_URL = "https://api.stackexchange.com"
base_params = {'site':'stackoverflow'}
def get_accepted_answers(params):
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
    accepted_answer_ids =  [q['accepted_answer_id'] for q in questions if q['is_answered'] == True and 'accepted_answer_id' in q]


def get_answers_for_question(question_id)
    answers_url = '/'.join(['questions', str(question_id), 'answers'])
    url = urljoin(API_URL, answers_url)
    answers = requests.get(url, params={**base_params, "sort":"votes"}).json()['items']