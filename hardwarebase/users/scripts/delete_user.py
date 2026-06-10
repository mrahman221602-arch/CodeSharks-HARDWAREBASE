from users.models import User

def run():

    pk = 3
    user = User.objects.get(pk=pk)
    user.delete()