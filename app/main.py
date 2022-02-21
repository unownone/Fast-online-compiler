from flask import jsonify,request,render_template
from app.compile import main, SUPPORTED_LANGS
import traceback
from flask import Flask
import json

app = Flask(__name__)

@app.get('/api/getLangs')
def get_supported_languages():
    return jsonify(list(SUPPORTED_LANGS.keys()))


@app.post('/api/compile')
def get_compiled_code():
    input = request.json if request.json is not None else {}  
    try:
        return jsonify({
            'response': main(input.get('code',ret('code')),
                             input.get('lang',ret('lang')),
                             input.get('args',ret('args')))
        })
    except:
        traceback.print_exc()
        return jsonify(
            {'response':'Something Unexcepted Happened! Try again later!'}
            )


def ret(dat):
    return jsonify({
        'response':'Data Missing: '+dat
    })

@app.route('/')
def garbage():
    return render_template('index.html')



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

