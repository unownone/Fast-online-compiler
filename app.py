from flask import Flask,jsonify,request
from compile import main, SUPPORTED_LANGS
import traceback


app = Flask(__name__)
  

@app.get('/getLangs')
def get_supported_languages():
    return jsonify(list(SUPPORTED_LANGS.keys()))


@app.post('/compile')
def get_compiled_code():
    input = request.json   
    try:
        return jsonify({
            'response': main(input['code'],input['lang'],input['args'])
        })
    except:
        traceback.print_exc()
        return jsonify(
            {'response':'Invalid Input!'}
            )

@app.route('/')
def garbage():
    return jsonify({'status':'ok'})



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response