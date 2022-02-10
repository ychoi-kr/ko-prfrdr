import json


if __name__ == '__main__':
    j = json.load(open('ko_spacing_rules.json'))
    j.sort(key=lambda x: x["desc"])
    
    with open('ko_spacing_rules2.json', 'w') as f:
        f.write(json.dumps(j, ensure_ascii=False, indent=2, separators=(',', ': ')))

