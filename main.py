# main.py

from views.login_window import LoginWindow
from controllers.auth_controller import AuthController


def main():
    # Initialize the authentication controller
    auth_controller = AuthController()

    # Start the login window
    login_window = LoginWindow(auth_controller)
    login_window.run()


if __name__ == "__main__":
    main()
