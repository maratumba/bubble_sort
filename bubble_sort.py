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

def extract_code_html(answer_html, answer_id):
    # returns code only string
    tree = html.fromstring(answer_html)
    # this removes the indentation so not very useful:
    # answer_code_blocks = tree.xpath(f'//div[@id="answer-{accepted_answer_ids[0]}"]//code/text()')
    # big code blocks are wrapped in <code class="hljs language-python"></code>
    # need to extract the code block intact with indentation
    # After spending a considerable time, realized that some attributes of the code blocks are not server side rendered
    # this gives us all the full code blocks:
    codes = tree.xpath(f"//div[@data-answerid='{answer_id}']//pre/code/text()") # returns a list of code blocks
    return codes


def guess_list_var_name(code):
    for line in code:
        try:
            left, right = [x.strip() for x in line.split('=')]
            if right[0] == '[' and right[-1] == ']' and len(left.split()) == 1:
                return left
        except: # Not ideal to capture all but we have no idea what we're dealing with
            # not my tempo
            continue

            
def run_code_on_list(l, code, array_var_name):
    l = guess_list_var_name

