from flask import Flask,jsonify,request
from compile import main, SUPPORTED_LANGS
import traceback


app = Flask(__name__)
  

@app.get('/getLangs')
def get_supported_languages():
    return jsonify(list(SUPPORTED_LANGS.keys()))


@app.post('/compile')
def get_compiled_code(input:dict):    
    try:
        return jsonify({
            'response': main(input['code'],input['lang'],input['args'])
        })
    except:
        traceback.print_exc()
        return jsonify(
            {'error':'Invalid Input!'}
            )

@app.route('/')
def garbage():
    return jsonify({'status':'ok'})
