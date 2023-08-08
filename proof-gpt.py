import argparse
import json

import openai


base_url = "https://wikidocs.net"


def get_env(key):
    env = dict()
    with open('.env') as f:
        for x in f.readlines():
            key, value = x.strip().split('=')
            env[key] = value
    
    return env[key]


def get_page(page_id, cache):
    headers = {"Content-Type": "application/json"}
    url = f"{base_url}/api/v1/page/{page_id}"

    if cache:
        import requests_cache
        session = requests_cache.CachedSession(expires_after=600)
        response = session.get(url, headers=headers)
    else:
        import requests
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        subject = data['subject']
        content = data['content']
        return subject, content
    else:
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
        raise ValueError("Failed to get wikidocs page")


def main(sentence, cache, rules):
    openai.api_key = get_env('OPENAI_API_KEY')
    #print("rules:", rules)
    for rule in rules:
        #print("rule:", rule)
        result = check(sentence, rule, cache)
        print(result)

output_format = '''
{
  "input_text": "<input text>",
  "checked_rule": "<rule URL>",
  "corrections":
    [
      {"pos": "<position including spaces>", "bad": "<bad part>", "good": "<correction>", "description": "<description>"}
    ]
}
'''

def check(sentence, rule, cache):
    rule_url = f'{base_url}/{rule}'
    subject, content = get_page(rule, cache)
    prompt = f"#{subject}\n{content}\n"
    prompt += "---\n"
    prompt += "위의 규칙에 따라 입력 문장을 검사하고, 결과를 다음과 같은 JSON으로 응답해 주세요. "
    prompt += "이때 bad와 good이 너무 짧으면 위치를 알아보기 힘들므로 적당한 길이로 나타내 주세요.\n "
    prompt += "위의 규칙과 관계없는 것은 검사 결과에 포함하지 마세요.\n"
    prompt += output_format.replace("<rule URL>", rule_url)
    prompt += "\n---\n입력:"
    prompt += f"\n{sentence}"
    prompt += "\n출력:"
    #print(f'===\n{prompt}\n===')

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt}
        ],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"]


if __name__ == '__main__':
    example_text = '''example:
    
     python proof-gpt.py "그 책을 다 읽는데 이틀 걸렸다." -r 67215
    '''

    parser = argparse.ArgumentParser(epilog=example_text)
    parser.add_argument("--rule", '-r', type=str, action='append')
    parser.add_argument("--cache", action=argparse.BooleanOptionalAction)
    parser.add_argument("sentence")
    args = parser.parse_args()
    main(args.sentence, args.cache, args.rule) 
