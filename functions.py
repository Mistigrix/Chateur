import pickle
from user import User


def get_user():
    """Recuperer les cookies de l'utilisateur"""
    try:
        with open('data.data', 'rb') as file:
            my_pickle = pickle.Unpickler(file)
            user = my_pickle.load()
    except FileNotFoundError:
        return User('', '')
    except EOFError:
        return User('', '')
    return user


def set_user(user):
    """Modifie ou Enregistre les données de l'utilisateur dans un ficher"""
    with open('data.data', 'wb') as file:
        my_pickler = pickle.Pickler(file)
        my_pickler.dump(user)
