import convert_speech_level
from google_trans_new.google_trans_new import google_translator  

from flask import Flask, request


app = Flask(__name__)
t = google_translator()  

@app.route('/translate', methods=['GET'])
def translate():
    arg = request.args.to_dict()
    translation = t.translate(
        lang_src=arg['source'], lang_tgt=arg['target'], text=arg['text']
    )
    return {"translation": convert_speech_level.haera(translation)}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8877)
