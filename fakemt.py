import re

import convert_speech_level

from google_trans_new.google_trans_new import google_translator  
from flask import Flask, request


app = Flask(__name__)
gt = google_translator()  

@app.route('/translate', methods=['GET'])
def translate():
    arg = request.args.to_dict()

    src = arg['text']
    src = re.sub(r'</?\w\d+>', '', src)

    trg = gt.translate(lang_src=arg['source'], lang_tgt=arg['target'], text=src)
    trg = re.sub(r'그림 (\d+)-(\d+)[.]?', r'그림 \g<1>.\g<2>', trg) \
        .replace('컨볼 루션', '콘볼루션').replace('컨볼루션', '컨볼루션') \
        .replace('피쳐', '피처') \
        .replace('하여 ', '해 ')

    result = convert_speech_level.haera(src + '\n' + trg)
    return {"translation": result }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8877)
