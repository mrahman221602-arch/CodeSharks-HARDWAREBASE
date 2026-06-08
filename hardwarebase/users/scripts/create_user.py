from users.models import User
from django.contrib.auth.hashers import make_password

def run():

    username = 'BasedGamer'
    email = 'basedgamer@fakemail.com'
    password = 'basedgamer123'
    pwd_hash = make_password(password)

    user = User(username=username, email=email, pwd_hash=pwd_hash)
    user.save()