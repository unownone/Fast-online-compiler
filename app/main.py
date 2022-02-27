from flask import jsonify,request,render_template
from app.compile import main, SUPPORTED_LANGS
import traceback
import json
from app import app,login
import time 
from app.models import CodeArchives

@app.get('/api/getLangs')
def get_supported_languages():
    return jsonify(list(SUPPORTED_LANGS.keys()))


@app.post('/api/compile')
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
        t1 = time.time()
        result = main(input.get('code',ret('code')),
                             input.get('lang',ret('lang')),
                             input.get('args',ret('args')))
        t1 = round(time.time()-t1,3)
        
        CodeArchives.objects.create(
                     code=input['code'],
                     language=input['lang'],
                     args=input['args'],
                     output=result,
                     CompileTime=t1
        )
        return jsonify({
            'response': result,
            'time':t1
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