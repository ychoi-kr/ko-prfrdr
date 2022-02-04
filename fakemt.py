import re

import convert_speech_level

from google_trans_new.google_trans_new import google_translator  
from flask import Flask, request


app = Flask(__name__)
gt = google_translator()  

@app.route('/translate', methods=['GET'])
def translate():
    arg = request.args.to_dict()
    result = convert_speech_level.haera(
        gt.translate(
            lang_src=arg['source'], lang_tgt=arg['target'], text=arg['text']
        )
    )
    result = re.sub(r'</ (\w\d+)> ', r'</\g<1>>', result)
    result = re.sub(r'<S0> 그림 (\d+)-(\d+)[.] ', r'<s0>그림 \g<1>.\g<2>', result)
    
    return {"translation": result }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8877)
