from app import db,login

@login.user_loader
class User(db.Document):
    username = db.StringField(required=False)