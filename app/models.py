from app import db,login
import datetime
@login.user_loader
class User(db.Document):
    username = db.StringField(required=False)
    
class CodeArchives(db.Document):
    """Stores all the code values
    """
    code = db.StringField(required=True)
    args = db.StringField(required=False)
    output = db.StringField(required=False)
    language = db.StringField(required=True)
    time =  db.DateTimeField(default=datetime.datetime.utcnow)
    CompileTime = db.FloatField()