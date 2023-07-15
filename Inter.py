from typing import *


class User:

    def __init__(self, login, password, mail):
        self.login = login
        self.password = password
        self.mail = mail

class Admin:

    def __init__(self, login, password):
        self.login = login
        self.password = password

@runtime_checkable
class Persone(Protocol):
    login:str
    password:str
    mail:str


def showData(users):

    for user in users:
        if isinstance(user, Persone):
            print(f"\nLogin = {user.login}\n"
                f"Password = {user.password}\n"
                f"Mail = {user.mail}\n")
        else:
            print("Користувач є адміністратором")
            print(f"{user.login}")


userList = []

userList.append(User("User1", "0000", "user1@gmail.com"))
userList.append(User("User2", "1234", "user2@gmail.com"))
userList.append(Admin("Admin", "root"))

showData(userList)