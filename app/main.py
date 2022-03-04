from flask import jsonify,request,render_template, session
from app.compile import main, SUPPORTED_LANGS
import traceback
from app import app,login
import time 
from app.models import CodeArchives
from app.decorators import rate_limiter

@app.get('/api/getLangs')
def get_supported_languages():
    return jsonify(list(SUPPORTED_LANGS.keys()))


@app.post('/api/compile')
@rate_limiter
def get_compiled_code():
    dataStream = {
        'application/json':request.json,
        'application/x-www-form-urlencoded':dict(request.form),
    }
    if request.headers.get('Content-Type') in dataStream:
        input = dataStream.get(request.headers.get('Content-Type'))
    else:
        return jsonify({
        'response':'Server Doesnt support this type of content type'
        }, 400)
    try:
        # Timing The thing
        # Creating A Log 
        CodeArchives.objects.create(
                     code=input.get('code',ret('code')),
                     language=input.get('lang',ret('lang')),
                     args=input.get('args',ret('args')),           
        )
        result = main(input['code'],
                             input['lang'],
                             input['args'])
        

        return jsonify({
            'response': result,
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
@login.unauthorized_handler
def garbage():
    return render_template('index.html')



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response