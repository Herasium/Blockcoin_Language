from flask import Flask, request, jsonify
from langdetect import detect_langs

app = Flask(__name__)

@app.route('/')
def index():
  return "Languages detection server. #Blockcoin"

@app.route('/t', methods=['POST'])
def detect_language():
    if request.is_json:
        data = request.get_json()
        if 'text' in data:
            text = data['text']
            detected_langs = detect_langs(text)
            detected_langs_dict = {str(lang.lang): lang.prob for lang in detected_langs}
            return jsonify({"text": text, "detected_languages": detected_langs_dict}), 200
        else:
            return jsonify({"error": "Text field missing in JSON request"}), 400
    else:
        return jsonify({"error": "Request body must be in JSON format"}), 400

app.run(debug=True,port=8080,host="0.0.0.0")
