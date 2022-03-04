from flask import request,session,jsonify
import datetime
import uuid

def rate_limiter(func,count=5,time_period=10):
    """Decorator to limit the number of requests per time period
    Parameters:
            count: Number of requests allowed in a time period [default: 100]
            time_period: Time period in seconds [default: 60]
    """
    
    def inner_func(*args,**kwargs):
        if session.get('id')==None:
            session['id'] = {'id':uuid.uuid4(),
                            'ip':request.remote_addr,
                            'refresh':datetime.datetime.now() + datetime.timedelta(seconds=time_period),
                            'count':count
            }
        else:
            if session['id']['refresh'] < datetime.datetime.now():
                session['id']['refresh'] = datetime.datetime.now() + datetime.timedelta(seconds=time_period)
                session['id']['count'] = count
            elif session['id']['count'] <= 0:
                return jsonify(
                    {'response':
                        f'You have exceeded the limit of requests. Wait for {round((session["id"]["refresh"] - datetime.datetime.now()).total_seconds())} seconds!'
                    }
                )
            else:
                session['id']['count'] -= 1    
                
        print(session.get('id'))
        return func(*args,**kwargs)
        
    return inner_func