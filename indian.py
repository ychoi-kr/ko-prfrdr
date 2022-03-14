import csv

namedict = {}

with open('indian_names.csv', mode='r', encoding="utf-8") as inp:
    reader = csv.reader(inp)
    namedict = {rows[0]:rows[1] for rows in reader}


def to_ko(userinput):
    result = userinput.replace('-', ' ')
    for word in result.split(' '):
        en = word.replace(',', '')
        if en in namedict:
            ko = namedict[en]
            result = result.replace(en, ko)
    
    return result
    
    
if __name__ == "__main__":
    print(to_ko(input()))
