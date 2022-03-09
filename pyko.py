import csv
import re


def to_ko(pinyin):

    tt = str.maketrans("áàāǎěēéíīǐóòōǒùū", "aaaaeeeiiioooouu")

    f = open('pinyin_ko.csv', encoding='utf-8')

    text = pinyin.translate(tt)

    for x in csv.reader(f.readlines()):
        text = re.sub(x[0], x[1], text, flags=re.IGNORECASE)

    return text


if __name__ == "__main__":
    print(to_ko(input()))