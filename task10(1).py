class InvalidLoginError(Exception):
    pass


class User:
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password 
        self.role = role

    def authenticate(self, password):
        if self.__password != password:
            raise InvalidLoginError("Invalid Credentials!")
        return True

    def access_dashboard(self):
        if self.role == "Admin":
            return "Access to Full AI Dashboard"
        elif self.role == "DataScientist":
            return "Access to Model Training Panel"
        else:
            return "Limited Access"


def login_system(user, password):
    try:
        if user.authenticate(password):
            print(user.access_dashboard())
    except InvalidLoginError as e:
        print("Login Failed:", e)


u1 = User("ratchita", "1234", "Admin")
login_system(u1, "1234")